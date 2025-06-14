from pathlib import Path

from core.enums.material import Material
from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("allowed:fluid")
class FluidAllowedConverter(BaseConverter):
    """
    アイテムに関するJSON -> submodelのEnumのallowedセット 定義の生成.
    具体的には、以下のファイルを処理します:
    intermediate/fluids.json -> allowed/fluid.py
    """

    dependencies = ["json:fluid", "enum:material"]
    json_filename = "fluid.json"
    allowed_filename = "fluid.py"

    def load(self) -> None:
        # 1) JSON load
        json_fluid_path = f"{self.intermediate_dir}/{self.json_filename}"
        fluids = self.load_json(json_fluid_path)

        # 2) Enumをimportして直接利用
        ret = [Material(fluid["name"]) for fluid in fluids]

        out = [
            "from enums.material import Material",
            "",
            "fluid_allowed: set[Material] = {",
            *[f"    {fluid}," for fluid in ret],
            "}",
        ]

        # 4) 出力ファイルに書き込み
        (Path(self.allowed_dir) / self.allowed_filename).write_text("\n".join(out))
