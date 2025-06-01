from core.loader.converters.base import BaseConverter  # 共通ユーティリティ
from core.loader.registry import register
from core.utils.lua_parser import parse_lua


@register("item_group_json")
class ItemGroupJsonConverter(BaseConverter):
    """
    アイテムグループに関するLua -> JSONファイルの変換.
    具体的には、以下のファイルを処理します:
    raw/item-groups.lua -> intermediate/item_groups.json
    """

    lua_path = "item-groups.lua"
    json_groups_path = "item_groups.json"
    json_subgroups_path = "item_subgroups.json"

    def load(self):
        # 1) Lua -> dict
        lua_file = f"{self.raw_dir}/{self.lua_path}"
        # 下記の extract_data_extend_tableとLuaTableTransformerの処理を外部化して呼び出す
        data = parse_lua(lua_file)

        # 2) 必要なら前処理
        groups = []
        subgroups = []

        for entry in data:
            if entry["type"] == "item-group":
                groups.append(entry)
            elif entry["type"] == "item-subgroup":
                subgroups.append(entry)

        # 3) dict -> JSON
        json_groups_path = f"{self.intermediate_dir}/{self.json_groups_path}"
        self.dump_json(groups, json_groups_path)

        json_subgroups_path = f"{self.intermediate_dir}/{self.json_subgroups_path}"
        self.dump_json(subgroups, json_subgroups_path)
