from core.loader.converters.base import BaseConverter
from core.loader.registry import register
from core.utils.lua_parser import parse_lua_file


@register("json:fluid")
class FluidJsonConverter(BaseConverter):
    """
    液体(Fluid)に関するLua -> JSONファイルの変換.
    具体的には、以下のファイルを処理します:
    raw/fluid.lua -> intermediate/fluid.json
    """

    dependencies = []
    lua_path = "fluid.lua"
    json_fluids_path = "fluid.json"

    def load(self):
        # 1) Lua -> dict
        lua_file = f"{self.raw_dir}/{self.lua_path}"
        data = parse_lua_file(lua_file)

        # 2) 必要なら前処理
        fluids = []
        for entry in data:
            if entry.get("subgroup") == "parameters":
                continue

            if entry.get("type") == "fluid":
                fluids.append(entry)

        # 3) dict -> JSON
        json_fluids_path = f"{self.intermediate_dir}/{self.json_fluids_path}"
        self.dump_json(fluids, json_fluids_path)
