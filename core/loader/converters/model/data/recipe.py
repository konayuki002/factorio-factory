from pathlib import Path

from sympy import Rational, srepr

from core.enums.material import Material
from core.enums.operation import Operation
from core.enums.operation_category import OperationCategory
from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("data:recipe")
class RecipeDataConverter(BaseConverter):
    """
    レシピに関するJSON -> Data 辞書の生成.
    intermediate/recipe.json -> data/recipe.py
    """

    dependencies = [
        "json:recipe",
        "enum:operation",
        "enum:material",
        "enum:operation_category",
    ]
    json_filename = "recipe.json"
    data_path = "recipe.py"

    def load(self) -> None:
        json_recipe_path = f"{self.intermediate_dir}/{self.json_filename}"
        recipes = self.load_json(json_recipe_path)

        ingredients = {}
        results = {}
        energy_required = {}
        category_of_recipe = {}

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
            # energy_required
            energy_required[op] = Rational(
                recipe.get("energy_required", 0.5)
            ).limit_denominator(100)
            # category
            cat = recipe.get("category")
            if cat is not None:
                try:
                    category_of_recipe[op] = OperationCategory(cat)
                except Exception:
                    category_of_recipe[op] = OperationCategory.Crafting
            else:
                category_of_recipe[op] = OperationCategory.Crafting

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
