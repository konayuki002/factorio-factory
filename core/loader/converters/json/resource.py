from core.loader.converters.base import BaseConverter
from core.loader.registry import register
from core.utils.lua_parser import parse_lua_file


@register("json:resource")
class ResourceJsonConverter(BaseConverter):
    """
    資源に関するLua -> JSONファイルの変換.
    具体的には、以下のファイルを処理します:
    raw/resource.lua -> intermediate/resource.json
    """

    dependencies = []
    lua_path = "resources.lua"
    json_items_path = "resources.json"

    def load(self):
        # 1) Lua -> dict
        lua_file = f"{self.raw_dir}/{self.lua_path}"
        data = parse_lua_file(lua_file)

        # 2) 必要なら前処理
        items = []
        # テーブルの0番目はparameterなので1番目から処理
        for entry in data:
            items.append(entry)

        # 3) dict -> JSON
        json_items_path = f"{self.intermediate_dir}/{self.json_items_path}"
        self.dump_json(items, json_items_path)
