from pathlib import Path

from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("allowed:technology")
class TechnologyAllowedConverter(BaseConverter):
    """
    アイテムに関するJSON -> submodelのEnumのallowedセット 定義の生成.
    具体的には、以下のファイルを処理します:
    intermediate/technology.json -> allowed/technology.py
    """

    dependencies = ["json:technology", "enum:material"]
    json_filename = "technology.json"
    enum_filename = "material.py"
    allowed_filename = "technology.py"

    def load(self) -> None:
        # 1) JSON load
        json_technology_path = f"{self.intermediate_dir}/{self.json_filename}"
        technologies = self.load_json(json_technology_path)

        # 2) Enum load
        enum_material_path = f"{self.enum_dir}/{self.enum_filename}"
        EnumMaterialClass = self.load_enum("Material", enum_material_path)

        # 3) submodelのEnumのallowedセット 定義を生成して保存
        ret = [
            EnumMaterialClass(f"technology-{technology['name']}")
            for technology in technologies
        ]

        out = [
            "from enums.material import Material",
            "",
            "technology_allowed: set[Material] = {",
            *[f"    {technology}," for technology in ret],
            "}",
        ]

        # 4) 出力ファイルに書き込み
        (Path(self.allowed_dir) / self.allowed_filename).write_text("\n".join(out))
