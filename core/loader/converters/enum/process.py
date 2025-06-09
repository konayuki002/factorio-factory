from core.loader.converters.base import BaseConverter
from core.loader.registry import register

@register("enum:process")
class ProcessEnumConverter(BaseConverter):
    """
    recipe.json, technology.json, resources.json からカテゴリごとにプレフィックスを付与し、CamelCaseの列挙子名で Process Enum を生成
    """
    dependencies = [
        "json:recipe",
        "json:technology",
        "json:resource",
    ]
    json_filenames = [
        "recipe.json",
        "technology.json",
        "resources.json",
    ]
    enum_process_path = "process.py"

    def load(self):
        all_members = []
        seen = set()
        for idx, fname in enumerate(self.json_filenames):
            path = f"{self.intermediate_dir}/{fname}"
            data = self.load_json(path)
            for entry in data:
                name = entry.get("name")
                if not name:
                    continue
                if idx == 0:  # recipe
                    value = name
                elif idx == 1:  # technology
                    value = f"research-{name}"
                else:  # resources
                    value = f"mining-{name}"
                if value not in seen:
                    all_members.append(value)
                    seen.add(value)
        self.gen_enum(
            "Process", all_members, f"{self.enum_dir}/{self.enum_process_path}"
        )
