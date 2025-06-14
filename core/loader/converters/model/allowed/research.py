from pathlib import Path

from core.enums.operation import Operation
from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("allowed:research")
class ResearchAllowedConverter(BaseConverter):
    """
    研究に関するJSON -> submodelのEnumのallowedセット 定義の生成.
    具体的には、以下のファイルを処理します:
    intermediate/technology.json -> allowed/research.py
    """

    dependencies = ["json:technology", "enum:operation"]
    json_filename = "technology.json"
    allowed_filename = "research.py"

    def load(self) -> None:
        # 1) JSON load
        json_technology_path = f"{self.intermediate_dir}/{self.json_filename}"
        technologies = self.load_json(json_technology_path)

        # 2) Enum をimportして直接利用
        # Operation Enumの値は research-<name> なので注意
        ret = [Operation(f"research-{tech['name']}") for tech in technologies]

        out = [
            "from enums.operation import Operation",
            "",
            "research_allowed: set[Operation] = {",
            *[f"    {op}," for op in ret],
            "}",
        ]

        (Path(self.allowed_dir) / self.allowed_filename).write_text("\n".join(out))
