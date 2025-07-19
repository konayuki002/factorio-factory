from pathlib import Path

from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("allowed:recipe")
class RecipeAllowedConverter(BaseConverter):
    """
    レシピに関するJSON -> submodelのEnumのallowedセット 定義の生成.
    具体的には、以下のファイルを処理します:
    intermediate/recipe.json -> allowed/recipe.py
    """

    dependencies = ["json:recipe", "enum:operation"]
    json_filename = "recipe.json"
    allowed_filename = "recipe.py"

    def load(self) -> None:
        from core.enums.operation import Operation

        # 1) JSON load
        json_recipe_path = f"{self.intermediate_dir}/{self.json_filename}"
        recipes = self.load_json(json_recipe_path)

        # 2) Enum をimportして直接利用
        ret = [Operation(recipe["name"]) for recipe in recipes]

        # Sort items alphabetically for consistent output
        ret.sort(key=str)

        out = [
            "from core.enums.operation import Operation",
            "",
            "recipe_allowed: set[Operation] = {",
            *[f"    {op}," for op in ret],
            "}",
        ]

        # 4) 出力ファイルに書き込み
        (Path(self.allowed_dir) / self.allowed_filename).write_text("\n".join(out))
