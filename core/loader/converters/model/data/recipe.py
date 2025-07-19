from pathlib import Path

from sympy import Rational, srepr

from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("data:recipe")
class RecipeDataConverter(BaseConverter):
    """
    Recipe (レシピ) に関するJSON -> Data 辞書の生成.
    intermediate/recipe.json -> data/recipe.py
    """

    dependencies = [
        "json:recipe",
        "enum:operation",
    ]
    json_filename = "recipe.json"
    data_path = "recipe.py"

    def load(self) -> None:
        """
        Recipeに関するデータを生成する。
        Operation共通の属性以外を取り出す。
        """
        from core.enums.operation import Operation

        json_recipe_path = f"{self.intermediate_dir}/{self.json_filename}"
        recipes = self.load_json(json_recipe_path)

        energy_required = {}

        for recipe in recipes:
            op = Operation(recipe["name"])
            # energy_required
            energy_required[op] = Rational(
                recipe.get("energy_required", 0.5)
            ).limit_denominator(100)

        out = [
            "from core.enums.operation import Operation",
            "from sympy import Integer, Rational",
            "",
            "ENERGY_REQUIRED: dict[Operation, Rational] = {",
            *[
                f"    {op}: {srepr(energy)},"
                for op, energy in sorted(
                    energy_required.items(), key=lambda x: str(x[0])
                )
            ],
            "}",
        ]
        (Path(self.data_dir) / self.data_path).write_text("\n".join(out))
