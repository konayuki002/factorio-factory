from pathlib import Path

from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("allowed:resource")
class ResourceAllowedConverter(BaseConverter):
    """
    アイテムに関するJSON -> submodelのEnumのallowedセット 定義の生成.
    具体的には、以下のファイルを処理します:
    intermediate/resources.json -> allowed/resource.py
    """

    dependencies = ["json:resource", "enum:material"]
    json_filename = "resources.json"
    enum_filename = "material.py"
    allowed_filename = "resource.py"

    def load(self) -> None:
        # 1) JSON load
        json_resource_path = f"{self.intermediate_dir}/{self.json_filename}"
        resources = self.load_json(json_resource_path)

        # 2) Enum load
        enum_material_path = f"{self.enum_dir}/{self.enum_filename}"
        EnumMaterialClass = self.load_enum("Material", enum_material_path)

        # 3) submodelのEnumのallowedセット 定義を生成して保存
        ret = [
            EnumMaterialClass(f"resource-{resource['name']}") for resource in resources
        ]

        out = [
            "from enums.material import Material",
            "",
            "resource_allowed: set[Material] = {",
            *[f"    {resource}," for resource in ret],
            "}",
        ]

        # 4) 出力ファイルに書き込み
        (Path(self.allowed_dir) / self.allowed_filename).write_text("\n".join(out))
