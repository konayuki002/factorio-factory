from pathlib import Path
from typing import Any

from sympy import Expr, Integer, srepr, sympify

from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("data:operation")
class OperationDataConverter(BaseConverter):
    """
    Operation (処理) に関するJSON -> Data 辞書の生成.
    intermediate/{recipe, technology, resources}.json -> data/operation.py
    """

    dependencies = [
        "json:recipe",
        "json:technology",
        "json:resource",
        "enum:operation",
        "enum:material",
        "enum:operation_category",
    ]
    json_filenames = ["recipe.json", "technology.json", "resources.json"]
    json_recipe_path = "recipe.json"
    json_technology_path = "technology.json"
    json_resources_path = "resources.json"

    data_path = "operation.py"

    def load(self) -> None:
        """
        Operationに関するデータを生成する。
        レシピ、研究、資源採掘の内、共通となる属性を取り出す。
        """
        from core.enums.material import Material
        from core.enums.operation import Operation
        from core.enums.operation_category import OperationCategory

        json_recipe_path = f"{self.intermediate_dir}/{self.json_recipe_path}"
        recipes = self.load_json(json_recipe_path)

        json_technology_path = f"{self.intermediate_dir}/{self.json_technology_path}"
        technologies = self.load_json(json_technology_path)

        json_resources_path = f"{self.intermediate_dir}/{self.json_resources_path}"
        resources = self.load_json(json_resources_path)

        ingredients = {}
        results = {}
        category_of_recipe = {}

        def _parse_recipe(
            recipe: dict[str, Any],
        ) -> tuple[dict[Material, Integer], dict[Material, Integer], OperationCategory]:
            ing_dict: dict[Material, Integer] = {}
            for ing in recipe.get("ingredients", []):
                try:
                    mat = Material(ing["name"])
                    amt = Integer(ing.get("amount", 1))
                    ing_dict[mat] = amt
                except ValueError as e:
                    # Material enumに存在しないアイテムをスキップ
                    print(f"警告: Material enumに存在しない材料をスキップ: {ing['name']} (レシピ: {recipe.get('name', 'unknown')})")
                    continue

            res_dict: dict[Material, Integer] = {}
            for res in recipe.get("results", []):
                try:
                    mat = Material(res["name"])
                    amt = Integer(res.get("amount", 1))
                    res_dict[mat] = amt
                except ValueError as e:
                    # Material enumに存在しないアイテムをスキップ
                    print(f"警告: Material enumに存在しないアイテムをスキップ: {res['name']} (レシピ: {recipe.get('name', 'unknown')})")
                    continue

            if recipe_category := recipe.get("category", None):
                operation_category = OperationCategory(recipe_category)
            else:
                operation_category = OperationCategory.Crafting

            return ing_dict, res_dict, operation_category

        def _parse_technology(
            tech: dict[str, Any],
        ) -> tuple[dict[Material, Expr], dict[Material, Integer]]:
            ing_dict: dict[Material, Expr] = {}
            res_dict: dict[Material, Integer] = {}

            if unit := tech.get("unit", None):
                # 材料の係数の取得
                coefficient: Expr = Integer(0)

                count: int | dict[str, Any]
                if count := unit.get("count", None):
                    if isinstance(count, int):
                        coefficient = Integer(count)
                    else:
                        if count.get("op") != "mult":
                            raise ValueError(
                                f"Unexpected operation type in count: {count}, expected 'mult'."
                            )
                        coefficient = Integer(count["left"] * count["right"])
                else:  # 係数がレベルに依存する場合
                    count_formula: str = unit["count_formula"]
                    coefficient = sympify(count_formula)

                # 必要なサイエンスパック各1個が列挙された属性と掛け合わせる
                for ing in unit["ingredients"]:
                    mat: Material = Material(ing[0])
                    amt = Integer(ing[1])
                    ing_dict[mat] = amt * coefficient

            # 結果
            mat = Material(f"technology-{tech['name']}")
            res_dict = {mat: Integer(1)}

            return ing_dict, res_dict

        def _parse_resource(
            resource: dict[str, Any],
        ) -> tuple[dict[Material, Expr], dict[Material, Integer]]:
            ing_dict: dict[Material, Expr] = {}
            res_dict: dict[Material, Integer] = {}

            # 材料
            mat = Material(f"resource-{resource['name']}")
            amt = Integer(1)
            ing_dict[mat] = amt

            # 複雑な資源はminable属性を持つ
            if minable := resource.get("minable", None):
                if required_fluid := minable.get("required_fluid", None):
                    # 例: ウラン鉱石の場合は硫酸
                    req_fluid_mat = Material(required_fluid)
                    req_fluid_amt = Integer(minable["fluid_amount"])
                    ing_dict[req_fluid_mat] = req_fluid_amt

                if result := minable.get("result", None):
                    res_mat = Material(result)
                    res_dict[res_mat] = Integer(1)
                elif minable_results := minable.get("results", None):
                    res_mat = Material(minable_results[0]["name"])
                    res_amt = Integer(minable_results[0]["amount_max"])
                    res_dict[res_mat] = res_amt
            else:
                res_mat = Material(resource["name"])
                res_dict = {res_mat: Integer(1)}

            return ing_dict, res_dict

        for recipe in recipes:
            op = Operation(recipe["name"])
            ing_dict, res_dict, category = _parse_recipe(recipe)
            ingredients[op] = ing_dict
            results[op] = res_dict
            category_of_recipe[op] = category

        for tech in technologies:
            op = Operation(f"research-{tech['name']}")
            ing_dict, res_dict = _parse_technology(tech)
            ingredients[op] = ing_dict
            results[op] = res_dict
            category_of_recipe[op] = OperationCategory.Research

        for resource in resources:
            op = Operation(f"mining-{resource['name']}")
            ing_dict, res_dict = _parse_resource(resource)
            ingredients[op] = ing_dict
            results[op] = res_dict
            category_of_recipe[op] = OperationCategory.Mining

        out = [
            "from core.enums.material import Material",
            "from core.enums.operation import Operation",
            "from core.enums.operation_category import OperationCategory",
            "from sympy import Add, Expr, Integer, Mul, Pow, Rational, Symbol",
            "",
            "L = Symbol('L')",
            "",
            "INGREDIENTS: dict[Operation, dict[Material, Integer | Expr]] = {",
            *[
                f"    {op}: {{{', '.join(f'{mat}: {srepr(amt).replace("Symbol('L')", "L")}' for mat, amt in ings.items())}}},"
                for op, ings in ingredients.items()
            ],
            "}",
            "",
            "RESULTS: dict[Operation, dict[Material, Integer]] = {",
            *[
                f"    {op}: {{{', '.join(f'{mat}: {srepr(amt)}' for mat, amt in ress.items())}}},"
                for op, ress in results.items()
            ],
            "}",
            "",
            "CATEGORY_OF_RECIPE: dict[Operation, OperationCategory] = {",
            *[f"    {op}: {cat}," for op, cat in category_of_recipe.items()],
            "}",
        ]
        (Path(self.data_dir) / self.data_path).write_text("\n".join(out))
