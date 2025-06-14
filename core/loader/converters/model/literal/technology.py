from pathlib import Path

from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("literal:technology")
class TechnologyLiteralConverter(BaseConverter):
    """
    アイテムに関するJSON -> Literal 定義の生成.
    具体的には、以下のファイルを処理します:
    intermediate/technology.json -> literal/technology.py
    """

    dependencies = ["json:technology", "enum:material"]
    json_filename = "technology.json"
    enum_filename = "material.py"
    literal_filename = "technology.py"

    def load(self) -> None:
        # 1) JSON load
        json_technology_path = f"{self.intermediate_dir}/{self.json_filename}"
        technologies = self.load_json(json_technology_path)

        # 2) Enum load
        enum_material_path = f"{self.enum_dir}/{self.enum_filename}"
        EnumMaterialClass = self.load_enum("Material", enum_material_path)

        # 3) Literal 定義を生成して保存
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

        # 2) Data 辞書を生成して保存
        (Path(self.literal_dir) / self.literal_filename).write_text("\n".join(out))
