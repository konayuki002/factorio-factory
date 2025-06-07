from core.loader.converters.base import BaseConverter
from core.loader.registry import register
from core.enums.manual_item_group import MANUAL_MEMBERS


@register("enum:item_group")
class ItemGroupEnumConverter(BaseConverter):
    """
    アイテムグループに関するJSON -> Enum クラスの生成.
    intermediate/item_groups.json -> enums/item_group.py
    """

    dependencies = ["json:item_group"]
    json_filename = "item_groups.json"
    enum_group_path = "item_group.py"

    # 2) Enum 生成用に名前一覧を返す
    # ここで小文字に変換している理由:
    # - Lua/JSON側のnameは大文字・小文字・ハイフンなど表記揺れがあるため、まずlower()で正規化する
    # - この後のmerge_uniqueで重複排除を正しく行うためにも、ここで正規化しておく
    # - Enumクラス生成時（gen_enum）でCamelCaseに変換されるので、ここではlower-caseで統一しておくと
    #   「kebab-case→lower-case→CamelCase」の一貫した変換フローになる
    def load(self):
        groups = self.load_json(f"{self.intermediate_dir}/{self.json_filename}")
        enum_group_members = [g["name"].lower() for g in groups]
        enum_group_members = self.merge_unique(
            enum_group_members,
            [m.lower() for m in MANUAL_MEMBERS["item_group"]],
            "ItemGroup",
        )
        self.gen_enum(
            "ItemGroup", enum_group_members, f"{self.enum_dir}/{self.enum_group_path}"
        )
