from pathlib import Path

from sympy.core import Integer
from sympy.printing import srepr

from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("data:material")
class MaterialDataConverter(BaseConverter):
    """
    Materialに関するJSON -> Data 辞書の生成.
    具体的には、以下のファイルを処理します:
    intermediate/{items.json, fluid.json} -> data/material.py
    """

    dependencies = ["json:item", "json:fluid", "enum:material"]
    json_filenames = ["item.json", "fluid.json", "resources.json", "technology.json"]
    json_item_filename = "item.json"
    json_fluid_filename = "fluid.json"
    json_resources_filename = "resources.json"
    json_technology_filename = "technology.json"
    enum_filenames = ["material.py", "item_subgroup.py"]
    enum_material_filename = "material.py"
    enum_item_subgroup_filename = "item_subgroup.py"
    data_path = "material.py"

    def load(self) -> None:
        # 1) JSON load
        json_item_path = f"{self.intermediate_dir}/{self.json_item_filename}"
        items = self.load_json(json_item_path)

        json_fluid_path = f"{self.intermediate_dir}/{self.json_fluid_filename}"
        fluids = self.load_json(json_fluid_path)

        json_resources_path = f"{self.intermediate_dir}/{self.json_resources_filename}"
        resources = self.load_json(json_resources_path)

        json_technology_path = (
            f"{self.intermediate_dir}/{self.json_technology_filename}"
        )
        technologies = self.load_json(json_technology_path)

        # 2) Enum load
        enum_material_path = f"{self.enum_dir}/{self.enum_material_filename}"
        EnumMaterialClass = self.load_enum("Material", enum_material_path)

        enum_item_subgroup_path = f"{self.enum_dir}/{self.enum_item_subgroup_filename}"
        EnumItemSubgroupClass = self.load_enum("ItemSubgroup", enum_item_subgroup_path)

        # 3) Data 辞書を生成して保存
        ret_item = {
            EnumMaterialClass(item["name"]): EnumItemSubgroupClass(item["subgroup"])
            for item in items
        }
        ret_fluid = {
            EnumMaterialClass(fluid["name"]): EnumItemSubgroupClass(fluid["subgroup"])
            for fluid in fluids
        }

        ret_resources = {}
        for resource in resources:
            category = resource.get("category", "basic-solid")
            subgroup = EnumItemSubgroupClass(f"unmined-resource-{category}")
            ret_resources[EnumMaterialClass(f"resource-{resource['name']}")] = subgroup

        ret_technology = {
            EnumMaterialClass(
                f"technology-{technology['name']}"
            ): EnumItemSubgroupClass("technology")
            for technology in technologies
        }
        ret = {**ret_item, **ret_fluid, **ret_resources, **ret_technology}

        out = [
            "from enums.item_subgroup import ItemSubgroup",
            "from enums.material import Material",
            "",
            "ITEM_SUBGROUP_OF_MATERIAL: dict[Material, ItemSubgroup] = {",
            *[f"    {material}: {subgroup}," for material, subgroup in ret.items()],
            "}",
        ]

        # 2) Data 辞書を生成して保存
        (Path(self.data_dir) / self.data_path).write_text("\n".join(out))
