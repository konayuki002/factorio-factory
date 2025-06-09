from core.loader.converters.base import BaseConverter
from core.loader.registry import register
from core.enums.manual_process_category import PROCESS_CATEGORY_MANUAL


@register("enum:process_category")
class ProcessCategoryEnumConverter(BaseConverter):
    """
    recipe_category.json + manual要素からProcessCategory Enumを生成
    """

    dependencies = ["json:recipe_category"]
    json_filename = "recipe_category.json"
    enum_process_category_path = "process_category.py"

    def load(self) -> None:
        json_path = f"{self.intermediate_dir}/{self.json_filename}"
        data = self.load_json(json_path)
        names = [entry["name"] for entry in data if "name" in entry]
        # manual要素を追加（重複排除・順序維持）
        all_names = self.merge_unique(names, PROCESS_CATEGORY_MANUAL, "ProcessCategory")
        self.gen_enum(
            "ProcessCategory",
            all_names,
            f"{self.enum_dir}/{self.enum_process_category_path}",
        )
