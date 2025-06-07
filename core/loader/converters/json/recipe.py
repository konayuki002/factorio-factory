from core.loader.converters.base import BaseConverter
from core.loader.registry import register
from core.utils.lua_parser import parse_lua_file


@register("json:recipe")
class RecipeJsonConverter(BaseConverter):
    """
    レシピに関するLua -> JSONファイルの変換.
    具体的には、以下のファイルを処理します:
    raw/recipe.lua -> intermediate/recipe.json
    """

    dependencies = []
    lua_filename = "recipe.lua"
    json_recipe_path = "recipe.json"

    def load(self):
        # 1) Lua -> dict
        lua_file = f"{self.raw_dir}/{self.lua_filename}"
        data = parse_lua_file(lua_file)

        # 2) 必要なら前処理
        recipes = []
        for entry in data:
            if entry.get("subgroup", None) == "parameters":
                continue
            if entry.get("type") == "recipe":
                recipes.append(entry)

        # 3) dict -> JSON
        json_path = f"{self.intermediate_dir}/{self.json_recipe_path}"
        self.dump_json(recipes, json_path)
