from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("enum:material")
class MaterialEnumConverter(BaseConverter):
    """
    item.json, fluid.json, resources.json, technology.json からMaterial Enumを生成
    """

    dependencies = [
        "json:item",
        "json:fluid",
        "json:resource",
        "json:technology",
    ]
    json_filenames = [
        "item.json",
        "fluid.json",
        "resources.json",
        "technology.json",
    ]
    enum_material_path = "material.py"

    def load(self) -> None:
        all_members = []
        seen = set()
        # prefix mapping for each json file
        prefix_map = {
            "item.json": "",
            "fluid.json": "",
            "resources.json": "resource-",
            "technology.json": "technology-",
        }
        for fname in self.json_filenames:
            path = f"{self.intermediate_dir}/{fname}"
            data = self.load_json(path)
            prefix = prefix_map.get(fname, "")
            for entry in data:
                name = entry.get("name")
                if not name:
                    continue
                value = f"{prefix}{name}"
                if value not in seen:
                    all_members.append(value)
                    seen.add(value)
        # Sort members alphabetically for consistent output
        all_members.sort()
        self.gen_enum(
            "Material", all_members, f"{self.enum_dir}/{self.enum_material_path}"
        )
