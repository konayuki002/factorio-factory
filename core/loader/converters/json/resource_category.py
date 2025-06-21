from core.loader.converters.base import BaseConverter  # 共通ユーティリティ
from core.loader.registry import register
from core.utils.lua_parser import parse_lua_file


@register("json:resource_category")
class ResourceCategoryJsonConverter(BaseConverter):
    """
    資源カテゴリに関するLua -> JSONファイルの変換.
    具体的には、以下のファイルを処理します:
    raw/resource-category.lua -> intermediate/resource_category.json
    """

    dependencies = []
    lua_filename = "resource-category.lua"
    json_categories_path = "resource_category.json"

    def load(self) -> None:
        # 1) Lua -> dict
        lua_file = f"{self.raw_dir}/{self.lua_filename}"
        data = parse_lua_file(lua_file)

        # 2) 必要なら前処理

        # 3) dict -> JSON
        json_path = f"{self.intermediate_dir}/{self.json_categories_path}"
        self.dump_json(data, json_path)
