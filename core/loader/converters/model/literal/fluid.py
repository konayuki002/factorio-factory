from pathlib import Path

from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("literal:fluid")
class FluidLiteralConverter(BaseConverter):
    """
    アイテムに関するJSON -> Literal 定義の生成.
    具体的には、以下のファイルを処理します:
    intermediate/fluids.json -> literal/fluid.py
    """

    dependencies = ["json:fluid", "enum:material"]
    json_filename = "fluid.json"
    enum_filename = "material.py"
    literal_filename = "fluid.py"

    def load(self) -> None:
        # 1) JSON load
        json_fluid_path = f"{self.intermediate_dir}/{self.json_filename}"
        fluids = self.load_json(json_fluid_path)

        # 2) Enum load
        enum_material_path = f"{self.enum_dir}/{self.enum_filename}"
        EnumMaterialClass = self.load_enum("Material", enum_material_path)

        # 3) Literal 定義を生成して保存
        ret = [EnumMaterialClass(fluid["name"]) for fluid in fluids]

        out = [
            "from typing import Literal",
            "",
            "from enums.material import Material",
            "",
            "Fluid = Literal[",
            *[f"    {fluid}," for fluid in ret],
            "]",
        ]

        # 2) Data 辞書を生成して保存
        (Path(self.literal_dir) / self.literal_filename).write_text("\n".join(out))
