from core.loader.converters.base import BaseConverter
from core.loader.registry import register
from core.utils.lua_parser import parse_lua_file


@register("json:recipe_category")
class RecipeCategoryJsonConverter(BaseConverter):
    """
    recipe-category.lua -> recipe_category.json
    """

    dependencies = []
    lua_filename = "recipe-category.lua"
    json_path = "recipe_category.json"

    def load(self) -> None:
        lua_file = f"{self.raw_dir}/{self.lua_filename}"
        data = parse_lua_file(lua_file)
        # type=="recipe-category"のみ抽出
        categories = [entry for entry in data if entry.get("type") == "recipe-category"]
        json_path = f"{self.intermediate_dir}/{self.json_path}"
        self.dump_json(categories, json_path)
