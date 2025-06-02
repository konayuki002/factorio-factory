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
        enum_group_members = [g["name"] for g in groups]
        enum_subgroup_members = [sg["name"] for sg in subgroups]

        # 2.5) 手動で追加するメンバーを統合（重複排除・順序維持）
        def merge_unique(base: list[str], extra: list[str]) -> list[str]:
            seen = set(base)
            result = base[:]
            for x in extra:
                if x not in seen:
                    result.append(x)
                    seen.add(x)
            return result

        enum_group_members = merge_unique(
            enum_group_members, MANUAL_MEMBERS["item_group"]
        )
        enum_subgroup_members = merge_unique(
            enum_subgroup_members, MANUAL_MEMBERS["item_subgroup"]
        )

        # 3) Enum クラスを生成して保存
        enum_group_path = f"{self.enum_dir}/{self.enum_group_path}"
        enum_subgroup_path = f"{self.enum_dir}/{self.enum_subgroup_path}"

        self.gen_enum("ItemGroup", enum_group_members, enum_group_path)
        self.gen_enum("ItemSubgroup", enum_subgroup_members, enum_subgroup_path)
