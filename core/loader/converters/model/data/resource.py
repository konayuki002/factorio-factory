from pathlib import Path

from sympy import Integer, srepr

from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("data:resource")
class ResourceDataConverter(BaseConverter):
    """
    Resource (資源) に関するJSON -> Data 辞書の生成.
    intermediate/resources.json -> data/resource.py
    """

    dependencies = [
        "json:technology",
        "enum:operation",
    ]
    json_filename = "resources.json"
    data_path = "resource.py"

    def load(self) -> None:
        """
        Resourceに関するデータを生成する。
        Operation共通の属性以外を取り出す。
        """
        from core.enums.operation import Operation

        json_resource_path = f"{self.intermediate_dir}/{self.json_filename}"
        resources = self.load_json(json_resource_path)

        time: dict[Operation, Integer] = {}

        for resource in resources:
            op = Operation(f"mining-{resource['name']}")
            # 採掘1回当たりにかかる時間
            if minable := resource.get("minable"):
                time[op] = Integer(minable["mining_time"])
            else:
                time[op] = Integer(resource["mining_time"])

        out = [
            "from core.enums.operation import Operation",
            "from sympy import Integer",
            "",
            "TIME: dict[Operation, Integer] = {",
            *[f"    {op}: {srepr(energy)}," for op, energy in sorted(time.items(), key=lambda x: str(x[0]))],
            "}",
        ]
        (Path(self.data_dir) / self.data_path).write_text("\n".join(out))
