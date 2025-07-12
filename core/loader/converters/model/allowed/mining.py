from pathlib import Path

from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("allowed:mining")
class MiningAllowedConverter(BaseConverter):
    """
    資源採掘に関するJSON -> submodelのEnumのallowedセット 定義の生成.
    具体的には、以下のファイルを処理します:
    intermediate/resources.json -> allowed/mining.py
    """

    dependencies = ["json:resource", "enum:operation"]
    json_filename = "resources.json"
    allowed_filename = "mining.py"

    def load(self) -> None:
        from core.enums.operation import Operation

        # 1) JSON load
        json_resource_path = f"{self.intermediate_dir}/{self.json_filename}"
        resources = self.load_json(json_resource_path)

        # 2) Enum をimportして直接利用
        # Operation Enumの値は mining-<name> なので注意
        ret = [Operation(f"mining-{res['name']}") for res in resources]

        out = [
            "from core.enums.operation import Operation",
            "",
            "mining_allowed: set[Operation] = {",
            *[f"    {op}," for op in ret],
            "}",
        ]

        (Path(self.allowed_dir) / self.allowed_filename).write_text("\n".join(out))
