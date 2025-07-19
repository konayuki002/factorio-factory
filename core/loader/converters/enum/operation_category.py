from core.enums.manual_operation_category import OPERATION_CATEGORY_MANUAL
from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("enum:operation_category")
class OperationCategoryEnumConverter(BaseConverter):
    """
    recipe_category.json + manual要素からOperationCategory Enumを生成
    """

    dependencies = ["json:recipe_category"]
    json_filename = "recipe_category.json"
    enum_operation_category_path = "operation_category.py"

    def load(self) -> None:
        json_path = f"{self.intermediate_dir}/{self.json_filename}"
        data = self.load_json(json_path)
        names = [entry["name"] for entry in data if "name" in entry]
        # manual要素を追加（重複排除・順序維持）
        all_names = self.merge_unique(
            names, OPERATION_CATEGORY_MANUAL, "OperationCategory"
        )
        all_names.sort()
        self.gen_enum(
            "OperationCategory",
            all_names,
            f"{self.enum_dir}/{self.enum_operation_category_path}",
        )
