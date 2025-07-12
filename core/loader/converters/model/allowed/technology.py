from pathlib import Path

from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("allowed:technology")
class TechnologyAllowedConverter(BaseConverter):
    """
    アイテムに関するJSON -> submodelのEnumのallowedセット 定義の生成.
    具体的には、以下のファイルを処理します:
    intermediate/technology.json -> allowed/technology.py
    """

    dependencies = ["json:technology", "enum:material"]
    json_filename = "technology.json"
    allowed_filename = "technology.py"

    def load(self) -> None:
        from core.enums.material import Material

        # 1) JSON load
        json_technology_path = f"{self.intermediate_dir}/{self.json_filename}"
        technologies = self.load_json(json_technology_path)

        # 2) Enumをimportして直接利用
        ret = [
            Material(f"technology-{technology['name']}") for technology in technologies
        ]

        out = [
            "from core.enums.material import Material",
            "",
            "technology_allowed: set[Material] = {",
            *[f"    {technology}," for technology in ret],
            "}",
        ]

        # 4) 出力ファイルに書き込み
        (Path(self.allowed_dir) / self.allowed_filename).write_text("\n".join(out))
