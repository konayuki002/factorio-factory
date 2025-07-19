import json
import logging
from pathlib import Path

from core.loader.converters.base import BaseConverter
from core.loader.registry import register

logger = logging.getLogger(__name__)


@register("json:mining_drill")
class MiningDrillJsonConverter(BaseConverter):
    """
    lua:prototypesの結果からmining_drill.jsonを生成
    mining-drillタイプのプロトタイプを抽出
    """

    dependencies = ["lua:prototypes"]  # Lua実行コンバータに依存
    json_items_path = "mining_drill.json"

    def load(self) -> None:
        try:
            # 1) lua:prototypesの結果を読み込み
            prototypes_file = Path(self.intermediate_dir) / "prototypes.json"
            if not prototypes_file.exists():
                logger.error(f"Prototypes file not found: {prototypes_file}")
                return

            with open(prototypes_file, "r", encoding="utf-8") as f:
                all_prototypes = json.load(f)

            # 2) mining-drillタイプのプロトタイプを抽出
            drills = []
            mining_drill_prototypes = all_prototypes.get("mining-drill", {})

            for _drill_name, drill_data in mining_drill_prototypes.items():
                # typeがmining-drillであることを確認（念のため）
                if drill_data.get("type") == "mining-drill":
                    drills.append(drill_data)

            # 3) JSON出力
            json_path = Path(self.intermediate_dir) / self.json_items_path
            self.dump_json(drills, str(json_path))

            logger.info(f"Extracted {len(drills)} mining drills from prototypes")

        except Exception as e:
            logger.error(f"Failed to process mining drills: {e}")
            raise
