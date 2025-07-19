from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("enum:operation")
class OperationEnumConverter(BaseConverter):
    """
    recipe.json, technology.json, resources.json からカテゴリごとにプレフィックスを付与し、CamelCaseの列挙子名で Operation Enum を生成
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
    enum_operation_path = "operation.py"

    def load(self) -> None:
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
        # Sort members alphabetically for consistent output
        all_members.sort()
        self.gen_enum(
            "Operation", all_members, f"{self.enum_dir}/{self.enum_operation_path}"
        )
