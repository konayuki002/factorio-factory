from pathlib import Path

from core.loader.converters.base import BaseConverter
from core.loader.registry import register
from core.models.data.manual_item_subgroup import ITEM_SUBGROUP_MANUAL


@register("data:item_subgroup")
class ItemSubgroupDataConverter(BaseConverter):
    """
    アイテムサブグループに関するJSON -> Data 辞書の生成.
    具体的には、以下のファイルを処理します:
    intermediate/item_subgroups.json -> data/item_subgroup.py
    """

    dependencies = ["json:item_group", "enum:item_subgroup", "enum:item_group"]
    json_filename = "item_subgroups.json"
    data_subgroup_path = "item_subgroup.py"
    data_group_path = "item_group.py"

    def load(self) -> None:
        # 1) JSON load
        json_subgroups_path = f"{self.intermediate_dir}/{self.json_filename}"
        subgroups = self.load_json(json_subgroups_path)

        # 2) Enum load
        enum_subgroup_path = f"{self.enum_dir}/item_subgroup.py"
        EnumSubgroupsClass = self.load_enum("ItemSubgroup", enum_subgroup_path)

        enum_group_path = f"{self.enum_dir}/item_group.py"
        EnumGroupsClass = self.load_enum("ItemGroup", enum_group_path)

        # 2.5) Merge manual data
        # 手動で定義されたサブグループをマージ
        subgroups = self.merge_unique_dicts(
            subgroups,
            ITEM_SUBGROUP_MANUAL,
            "name",
            "ItemSubgroup",
        )

        # 3) Data 辞書を生成して保存
        ret = {
            EnumSubgroupsClass(subgroup["name"]): EnumGroupsClass(subgroup["group"])
            for subgroup in subgroups
        }

        out = [
            "from core.enums.item_subgroup import ItemSubgroup",
            "from core.enums.item_group import ItemGroup",
            "",
            "GROUP_OF_SUBGROUP: dict[ItemSubgroup, ItemGroup] = {",
            *[f"    {subgroup}: {group}," for subgroup, group in sorted(ret.items(), key=lambda x: str(x[0]))],
            "}",
        ]

        # 2) Data 辞書を生成して保存
        (Path(self.data_dir) / self.data_subgroup_path).write_text("\n".join(out))
