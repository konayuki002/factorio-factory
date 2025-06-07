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

    def load(self):
        all_names = []
        seen = set()

        for fname in self.json_filenames:
            path = f"{self.intermediate_dir}/{fname}"
            data = self.load_json(path)
            for entry in data:
                name = entry.get("name")
                if name:
                    lname = name.lower()
                    if lname not in seen:
                        all_names.append(lname)
                        seen.add(lname)

        self.gen_enum(
            "Material", all_names, f"{self.enum_dir}/{self.enum_material_path}"
        )
