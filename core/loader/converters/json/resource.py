import json
import logging
from pathlib import Path

from core.loader.converters.base import BaseConverter
from core.loader.registry import register

logger = logging.getLogger(__name__)


@register("json:resource")
class ResourceJsonConverter(BaseConverter):
    """
    lua:prototypesの結果からresources.jsonを生成
    resourceタイプのプロトタイプを抽出
    """

    dependencies = ["lua:prototypes"]  # Lua実行コンバータに依存
    json_items_path = "resources.json"

    def load(self) -> None:
        try:
            # 1) lua:prototypesの結果を読み込み
            prototypes_file = Path(self.intermediate_dir) / "prototypes.json"
            if not prototypes_file.exists():
                logger.error(f"Prototypes file not found: {prototypes_file}")
                return

            with open(prototypes_file, "r", encoding="utf-8") as f:
                all_prototypes = json.load(f)

            # 2) resourceタイプのプロトタイプを抽出
            resources = []
            resource_prototypes = all_prototypes.get("resource", {})

            for _resource_name, resource_data in resource_prototypes.items():
                resources.append(resource_data)

            # 3) JSON出力
            json_path = Path(self.intermediate_dir) / self.json_items_path
            self.dump_json(resources, str(json_path))

            logger.info(f"Extracted {len(resources)} resources from prototypes")

        except Exception as e:
            logger.error(f"Failed to process resources: {e}")
            raise
