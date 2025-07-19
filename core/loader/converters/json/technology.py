from core.loader.converters.base import BaseConverter
from core.loader.registry import register
from core.utils.lua_parser import parse_lua_file


@register("json:technology")
class TechnologyJsonConverter(BaseConverter):
    """
    テクノロジーに関するLua -> JSONファイルの変換.
    具体的には、以下のファイルを処理します:
    raw/technology.lua -> intermediate/technology.json
    """

    dependencies = []
    lua_filename = "technology.lua"
    json_technology_path = "technology.json"

    def load(self) -> None:
        # 1) Lua -> dict
        lua_file = f"{self.raw_dir}/{self.lua_filename}"
        data = parse_lua_file(lua_file)

        # 2) 必要なら前処理
        technologies = []
        for entry in data:
            if entry.get("type") == "technology":
                technologies.append(entry)

        # 3) dict -> JSON
        json_path = f"{self.intermediate_dir}/{self.json_technology_path}"
        self.dump_json(technologies, json_path)
