from pathlib import Path

from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("literal:resource")
class ResourceLiteralConverter(BaseConverter):
    """
    アイテムに関するJSON -> Literal 定義の生成.
    具体的には、以下のファイルを処理します:
    intermediate/resources.json -> literal/resource.py
    """

    dependencies = ["json:resource", "enum:material"]
    json_filename = "resources.json"
    enum_filename = "material.py"
    literal_filename = "resource.py"

    def load(self) -> None:
        # 1) JSON load
        json_resource_path = f"{self.intermediate_dir}/{self.json_filename}"
        resources = self.load_json(json_resource_path)

        # 2) Enum load
        enum_material_path = f"{self.enum_dir}/{self.enum_filename}"
        EnumMaterialClass = self.load_enum("Material", enum_material_path)

        # 3) Literal 定義を生成して保存
        ret = [
            EnumMaterialClass(f"resource-{resource['name']}") for resource in resources
        ]

        out = [
            "from typing import Literal",
            "",
            "from enums.material import Material",
            "",
            "Resource = Literal[",
            *[f"    {resource}," for resource in ret],
            "]",
        ]

        # 2) Data 辞書を生成して保存
        (Path(self.literal_dir) / self.literal_filename).write_text("\n".join(out))
