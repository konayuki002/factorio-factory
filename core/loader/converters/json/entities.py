import json
import logging
from pathlib import Path

from core.loader.converters.base import BaseConverter
from core.loader.registry import register

logger = logging.getLogger(__name__)


@register("json:entities")
class EntitiesJsonConverter(BaseConverter):
    """
    lua:prototypesの結果からentities.jsonを生成
    assembling-machine, mining-drillなどのエンティティタイプを抽出
    """

    dependencies = ["lua:prototypes"]  # Lua実行コンバータに依存
    json_entities_path = "entities.json"

    def load(self) -> None:
        try:
            # 1) lua:prototypesの結果を読み込み
            prototypes_file = Path(self.intermediate_dir) / "prototypes.json"
            if not prototypes_file.exists():
                logger.error(f"Prototypes file not found: {prototypes_file}")
                return

            with open(prototypes_file, "r", encoding="utf-8") as f:
                all_prototypes = json.load(f)

            # 2) エンティティ系のプロトタイプを抽出
            entities = []

            # エンティティ系のタイプを定義（assembling-machine, mining-drill等）
            entity_types = [
                "assembling-machine",
                "mining-drill",
                "furnace",
                "lab",
                "transport-belt",
                "inserter",
                "pipe",
                "electric-pole",
                "container",
                "logistic-container",
                "storage-tank",
                "boiler",
                "generator",
                "solar-panel",
                "accumulator",
            ]

            for entity_type in entity_types:
                if entity_type in all_prototypes:
                    for entity_name, entity_data in all_prototypes[entity_type].items():
                        entities.append(entity_data)

            # 3) JSON出力
            json_path = Path(self.intermediate_dir) / self.json_entities_path
            self.dump_json(entities, str(json_path))

            logger.info(f"Extracted {len(entities)} entities from prototypes")

        except Exception as e:
            logger.error(f"Failed to process entities: {e}")
            raise
