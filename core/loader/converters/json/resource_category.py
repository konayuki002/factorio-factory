import json
import logging
from pathlib import Path

from core.loader.converters.base import BaseConverter
from core.loader.registry import register

logger = logging.getLogger(__name__)


@register("json:resource_category")
class ResourceCategoryJsonConverter(BaseConverter):
    """
    lua:prototypesの結果からresource_category.jsonを生成
    resource-categoryタイプのプロトタイプを抽出
    """

    dependencies = ["lua:prototypes"]  # Lua実行コンバータに依存
    json_categories_path = "resource_category.json"

    def load(self) -> None:
        try:
            # 1) lua:prototypesの結果を読み込み
            prototypes_file = Path(self.intermediate_dir) / "prototypes.json"
            if not prototypes_file.exists():
                logger.error(f"Prototypes file not found: {prototypes_file}")
                return

            with open(prototypes_file, "r", encoding="utf-8") as f:
                all_prototypes = json.load(f)

            # 2) resource-categoryタイプのプロトタイプを抽出
            categories = []
            category_prototypes = all_prototypes.get("resource-category", {})

            for category_name, category_data in category_prototypes.items():
                categories.append(category_data)

            # 3) JSON出力
            json_path = Path(self.intermediate_dir) / self.json_categories_path
            self.dump_json(categories, str(json_path))

            logger.info(
                f"Extracted {len(categories)} resource categories from prototypes"
            )

        except Exception as e:
            logger.error(f"Failed to process resource categories: {e}")
            raise
