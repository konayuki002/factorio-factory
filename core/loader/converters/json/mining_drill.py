from core.loader.converters.base import BaseConverter
from core.loader.registry import register
from core.utils.lua_parser import parse_lua_file


@register("json:mining_drill")
class MiningDrillJsonConverter(BaseConverter):
    """
    Mining Drillに関するLua -> JSONファイルの変換.
    raw/mining-drill.lua -> intermediate/mining_drill.json
    """

    dependencies = []
    lua_filename = "mining-drill.lua"
    json_items_path = "mining_drill.json"

    def load(self):
        lua_file = f"{self.raw_dir}/{self.lua_filename}"
        data = parse_lua_file(lua_file)
        drills = [entry for entry in data if entry.get("type") == "mining-drill"]
        json_path = f"{self.intermediate_dir}/{self.json_items_path}"
        self.dump_json(drills, json_path)
