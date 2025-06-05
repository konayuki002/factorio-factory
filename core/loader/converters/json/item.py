from core.loader.converters.base import BaseConverter
from core.loader.registry import register
from core.utils.lua_parser import parse_lua


@register("json:item")
class ItemJsonConverter(BaseConverter):
    """
    アイテムに関するLua -> JSONファイルの変換.
    具体的には、以下のファイルを処理します:
    raw/item.lua -> intermediate/item.json
    """

    dependencies = []
    lua_path = "item.lua"
    json_items_path = "item.json"

    def load(self):
        # 1) Lua -> dict
        lua_file = f"{self.raw_dir}/{self.lua_path}"
        data = parse_lua(lua_file)

        # 2) 必要なら前処理
        items = []
        for entry in data:

            if entry.get("subgroup") == "parameters":
                # パラメータシグナル用アイテムは除外
                continue

            if entry.get("type") == "item":
                items.append(entry)

        # 3) dict -> JSON
        json_items_path = f"{self.intermediate_dir}/{self.json_items_path}"
        self.dump_json(items, json_items_path)
