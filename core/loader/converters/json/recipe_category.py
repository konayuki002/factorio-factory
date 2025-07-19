import json
import logging
from pathlib import Path

from core.loader.converters.base import BaseConverter
from core.loader.registry import register

logger = logging.getLogger(__name__)


@register("json:recipe_category")
class RecipeCategoryJsonConverter(BaseConverter):
    """
    lua:prototypesの結果からrecipe_category.jsonを生成
    recipe-categoryタイプのプロトタイプを抽出
    """

    dependencies = ["lua:prototypes"]  # Lua実行コンバータに依存
    json_path = "recipe_category.json"

    def load(self) -> None:
        try:
            # 1) lua:prototypesの結果を読み込み
            prototypes_file = Path(self.intermediate_dir) / "prototypes.json"
            if not prototypes_file.exists():
                logger.error(f"Prototypes file not found: {prototypes_file}")
                return

            with open(prototypes_file, "r", encoding="utf-8") as f:
                all_prototypes = json.load(f)

            # 2) recipe-categoryタイプのプロトタイプを抽出
            categories = []
            category_prototypes = all_prototypes.get("recipe-category", {})

            for category_name, category_data in category_prototypes.items():
                if category_data.get("type") == "recipe-category":
                    categories.append(category_data)

            # 3) JSON出力
            json_output_path = Path(self.intermediate_dir) / self.json_path
            self.dump_json(categories, str(json_output_path))

            logger.info(
                f"Extracted {len(categories)} recipe categories from prototypes"
            )

        except Exception as e:
            logger.error(f"Failed to process recipe categories: {e}")
            raise
