from core.loader.converters.base import BaseConverter  # 共通ユーティリティ
from core.loader.registry import register
from core.enums.manual_item_group import MANUAL_MEMBERS


@register("enum:item_group")
class ItemGroupEnumConverter(BaseConverter):
    """
    アイテムグループに関するJSON -> Enum クラスの生成.
    具体的には、以下のファイルを処理します:
    intermediate/item-groups.json, intermediate/item-subgroups.json
     -> enums/item_group.py, enums/item_subgroup.py
    """

    dependencies = ["json:item_group"]
    json_groups_path = "item_groups.json"
    json_subgroups_path = "item_subgroups.json"
    enum_group_path = "item_group.py"
    enum_subgroup_path = "item_subgroup.py"

    def load(self):
        # 1) JSON load
        json_groups_path = f"{self.intermediate_dir}/{self.json_groups_path}"
        groups = self.load_json(json_groups_path)

        json_subgroups_path = f"{self.intermediate_dir}/{self.json_subgroups_path}"
        subgroups = self.load_json(json_subgroups_path)

        # 2) Enum 生成用に名前一覧を返す
        # ここで小文字に変換している理由:
        # - Lua/JSON側のnameは大文字・小文字・ハイフンなど表記揺れがあるため、まずlower()で正規化する
        # - この後のmerge_uniqueで重複排除を正しく行うためにも、ここで正規化しておく
        # - Enumクラス生成時（gen_enum）でCamelCaseに変換されるので、ここではlower-caseで統一しておくと
        #   「kebab-case→lower-case→CamelCase」の一貫した変換フローになる
        enum_group_members = [g["name"].lower() for g in groups]
        enum_subgroup_members = [sg["name"].lower() for sg in subgroups]

        # 2.5) 手動で追加するメンバーを統合（重複排除・順序維持）
        enum_group_members = self.merge_unique(
            enum_group_members,
            [m.lower() for m in MANUAL_MEMBERS["item_group"]],
            "ItemGroup",
        )
        enum_subgroup_members = self.merge_unique(
            enum_subgroup_members,
            [m.lower() for m in MANUAL_MEMBERS["item_subgroup"]],
            "ItemSubgroup",
        )

        # 3) Enum クラスを生成して保存
        enum_group_path = f"{self.enum_dir}/{self.enum_group_path}"
        enum_subgroup_path = f"{self.enum_dir}/{self.enum_subgroup_path}"

        self.gen_enum("ItemGroup", enum_group_members, enum_group_path)
        self.gen_enum("ItemSubgroup", enum_subgroup_members, enum_subgroup_path)
