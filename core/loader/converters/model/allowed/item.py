from pathlib import Path

from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("allowed:item")
class ItemAllowedConverter(BaseConverter):
    """
    アイテムに関するJSON -> submodelのEnumのallowedセット 定義の生成.
    具体的には、以下のファイルを処理します:
    intermediate/items.json -> allowed/item.py
    """

    dependencies = ["json:item", "enum:material"]
    json_filename = "item.json"
    allowed_filename = "item.py"

    def load(self) -> None:
        from core.enums.material import Material

        # 1) JSON load
        json_items_path = f"{self.intermediate_dir}/{self.json_filename}"
        items = self.load_json(json_items_path)

        # 2) Enumをimportして直接利用
        ret = [Material(item["name"]) for item in items]

        out = [
            "from enums.material import Material",
            "",
            "item_allowed: set[Material] = {",
            *[f"    {item}," for item in ret],
            "}",
        ]

        # 4) 出力ファイルに書き込み
        (Path(self.allowed_dir) / self.allowed_filename).write_text("\n".join(out))
