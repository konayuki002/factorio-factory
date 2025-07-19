from pathlib import Path

from sympy import Integer, srepr

from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("data:research")
class ResearchDataConverter(BaseConverter):
    """
    Research (研究) に関するJSON -> Data 辞書の生成.
    intermediate/technology.json -> data/research.py
    """

    dependencies = [
        "json:technology",
        "enum:operation",
    ]
    json_filename = "technology.json"
    data_path = "research.py"

    def load(self) -> None:
        """
        Researchに関するデータを生成する。
        Operation共通の属性以外を取り出す。
        """
        from core.enums.operation import Operation

        json_technology_path = f"{self.intermediate_dir}/{self.json_filename}"
        technologies = self.load_json(json_technology_path)

        time: dict[Operation, Integer] = {}

        for tech in technologies:
            op = Operation(f"research-{tech['name']}")
            # 研究1ユニット当たりにかかる時間
            if unit := tech.get("unit"):
                time[op] = Integer(unit["time"])

        out = [
            "from core.enums.operation import Operation",
            "from sympy import Integer",
            "",
            "TIME: dict[Operation, Integer] = {",
            *[f"    {op}: {srepr(energy)}," for op, energy in sorted(time.items(), key=lambda x: str(x[0]))],
            "}",
        ]
        (Path(self.data_dir) / self.data_path).write_text("\n".join(out))
