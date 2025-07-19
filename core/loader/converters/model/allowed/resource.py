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
    allowed_filename = "resource.py"

    def load(self) -> None:
        from core.enums.material import Material

        # 1) JSON load
        json_resource_path = f"{self.intermediate_dir}/{self.json_filename}"
        resources = self.load_json(json_resource_path)

        # 2) Enumをimportして直接利用
        ret = [Material(f"resource-{resource['name']}") for resource in resources]

        # Sort items alphabetically for consistent output
        ret.sort(key=str)

        out = [
            "from core.enums.material import Material",
            "",
            "resource_allowed: set[Material] = {",
            *[f"    {resource}," for resource in ret],
            "}",
        ]

        # 4) 出力ファイルに書き込み
        (Path(self.allowed_dir) / self.allowed_filename).write_text("\n".join(out))
