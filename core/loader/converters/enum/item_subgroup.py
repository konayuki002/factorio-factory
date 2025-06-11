from core.enums.manual_item_subgroup import ITEM_SUBGROUP_MANUAL
from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("enum:item_subgroup")
class ItemSubgroupEnumConverter(BaseConverter):
    """
    アイテムサブグループに関するJSON -> Enum クラスの生成.
    intermediate/item_subgroups.json -> enums/item_subgroup.py
    """

    dependencies = ["json:item_group"]
    json_filename = "item_subgroups.json"
    enum_subgroup_path = "item_subgroup.py"

    def load(self) -> None:
        subgroups = self.load_json(f"{self.intermediate_dir}/{self.json_filename}")
        enum_subgroup_members = [sg["name"].lower() for sg in subgroups]
        enum_subgroup_members = self.merge_unique(
            enum_subgroup_members,
            [m.lower() for m in ITEM_SUBGROUP_MANUAL],
            "ItemSubgroup",
        )
        self.gen_enum(
            "ItemSubgroup",
            enum_subgroup_members,
            f"{self.enum_dir}/{self.enum_subgroup_path}",
        )
