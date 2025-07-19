from core.loader.converters.base import BaseConverter
from core.loader.registry import register
from core.utils.lua_parser import parse_lua_file


@register("json:entities")
class EntitiesJsonConverter(BaseConverter):
    """
    entities.lua -> entities.json
    data:extend({...})の中身を全て抽出する基本形
    """

    dependencies = []
    lua_filename = "entities.lua"
    json_entities_path = "entities.json"

    def load(self) -> None:
        lua_file = f"{self.raw_dir}/{self.lua_filename}"
        data = parse_lua_file(lua_file)
        # まずは全て抽出
        json_path = f"{self.intermediate_dir}/{self.json_entities_path}"
        self.dump_json(data, json_path)
