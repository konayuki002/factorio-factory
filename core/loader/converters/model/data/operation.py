from pathlib import Path

from sympy import Rational, srepr

from core.loader.converters.base import BaseConverter
from core.loader.registry import register
from typing import Any
from sympy import Expr, S, sympify, Integer

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
    json_filenames = ["recipe.json"
                      ,"technology.json"
                      ,"resources.json"
    ]
    json_recipe_path = "recipe.json"
    json_technology_path = "technology.json"
    json_resources_path = "resources.json"

    data_path = "operation.py"

    def load(self) -> None:
        from core.enums.material import Material
        from core.enums.operation import Operation
        from core.enums.operation_category import OperationCategory

        json_recipe_path = f"{self.intermediate_dir}/{self.json_filename}"
        recipes = self.load_json(json_recipe_path)

        json_technology_path = f"{self.intermediate_dir}/{self.json_technology_path}"
        technologies = self.load_json(json_technology_path)

        json_resources_path = f"{self.intermediate_dir}/{self.json_resources_path}"
        resources = self.load_json(json_resources_path)

        ingredients = {}
        results = {}
        category_of_recipe = {}

        # Read recipes
        for recipe in recipes:
            op = Operation(recipe["name"])
            # ingredients
            ing_dict = {}
            for ing in recipe.get("ingredients", []):
                mat = Material(ing["name"])
                amt = Rational(ing.get("amount", 1))
                ing_dict[mat] = amt
            ingredients[op] = ing_dict
            # results
            res_dict = {}
            for res in recipe.get("results", []):
                mat = Material(res["name"])
                amt = Rational(res.get("amount", 1))
                res_dict[mat] = amt
            results[op] = res_dict
            # category
            cat = recipe.get("category")
            if cat is not None:
                try:
                    category_of_recipe[op] = OperationCategory(cat)
                except Exception:
                    category_of_recipe[op] = OperationCategory.Crafting
            else:
                category_of_recipe[op] = OperationCategory.Crafting

        # Read technologies
        for tech in technologies:
            op = Operation(f"research-{tech['name']}")

            # ingredients
            unit: dict[str, Any] = tech.get("unit", {})

            # coefficient
            coefficient: Expr = Integer(0)
            if "count" in unit:
                count: int | dict[str, Any] = unit["count"]
                if isinstance(count, int):
                    coefficient = Integer(count)
                else:
                    if count.get("op") != "mult":
                        raise ValueError(
                            f"Unexpected operation type in count: {count}, expected 'mult'."
                        )
                    coefficient = Integer(count["left"] * count["right"])
            else: # count_formula
                count_formula: str = unit.get("count_formula")
                coefficient = sympify(count_formula)

            ing_dict = {}
            # Multiply to the kinds of science_pack
            for ing in unit["ingredients"]:
                mat: Material = Material(ing[0]) 
                amt: int = ing[1]
                ing_dict[mat] = Rational(mat) * coefficient
                ingredients[op] = ing_dict

            # results
            results = {op: Integer(1)}

        out = [
            "from enums.operation import Operation",
            "from enums.material import Material",
            "from enums.operation_category import OperationCategory",
            "from sympy import Integer, Rational",
            "",
            "INGREDIENTS: dict[Operation, dict[Material, Integer]] = {",
            *[
                f"    {op}: {{{', '.join(f'{mat}: {srepr(amt)}' for mat, amt in ings.items())}}},"
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
            "ENERGY_REQUIRED: dict[Operation, Rational] = {",
            *[f"    {op}: {srepr(energy)}," for op, energy in energy_required.items()],
            "}",
            "",
            "CATEGORY_OF_RECIPE: dict[Operation, OperationCategory] = {",
            *[f"    {op}: {cat}," for op, cat in category_of_recipe.items()],
            "}",
        ]
        (Path(self.data_dir) / self.data_path).write_text("\n".join(out))
