from core.loader.converters.base import BaseConverter
from core.loader.registry import register
from core.enums.manual_item_group import MANUAL_MEMBERS


@register("enum:item")
class ItemEnumConverter(BaseConverter):
    """
    アイテムに関するJSON -> Enum クラスの生成.
    具体的には、以下のファイルを処理します:
    intermediate/item.json -> enums/item.py
    """

    dependencies = ["json:item"]
    json_items_path = "item.json"
    enum_item_path = "item.py"

    def load(self):
        # 1) JSON load
        json_items_path = f"{self.intermediate_dir}/{self.json_items_path}"
        items = self.load_json(json_items_path)

        # 2) Enum 生成用に名前一覧を返す
        enum_item_members = [item["name"].lower() for item in items]

        # 2.5) 手動で追加するメンバーを統合（重複排除・順序維持）
        manual = MANUAL_MEMBERS.get("item", [])
        enum_item_members = self.merge_unique(
            enum_item_members,
            [m.lower() for m in manual],
            "Item",
        )

        # 3) Enum クラスを生成して保存
        enum_item_path = f"{self.enum_dir}/{self.enum_item_path}"
        self.gen_enum("Item", enum_item_members, enum_item_path)
