import json
import logging
from pathlib import Path

from core.loader.converters.base import BaseConverter
from core.loader.registry import register

logger = logging.getLogger(__name__)


@register("json:technology")
class TechnologyJsonConverter(BaseConverter):
    """
    lua:prototypesの結果からtechnology.jsonを生成
    technologyタイプのプロトタイプを抽出
    """

    dependencies = ["lua:prototypes"]  # Lua実行コンバータに依存
    json_technology_path = "technology.json"

    def load(self) -> None:
        try:
            # 1) lua:prototypesの結果を読み込み
            prototypes_file = Path(self.intermediate_dir) / "prototypes.json"
            if not prototypes_file.exists():
                logger.error(f"Prototypes file not found: {prototypes_file}")
                return

            with open(prototypes_file, "r", encoding="utf-8") as f:
                all_prototypes = json.load(f)

            # 2) technologyタイプのプロトタイプを抽出
            technologies = []
            technology_prototypes = all_prototypes.get("technology", {})

            for _tech_name, tech_data in technology_prototypes.items():
                # typeがtechnologyであることを確認（念のため）
                if tech_data.get("type") == "technology":
                    technologies.append(tech_data)

            # 3) JSON出力
            json_path = Path(self.intermediate_dir) / self.json_technology_path
            self.dump_json(technologies, str(json_path))

            logger.info(f"Extracted {len(technologies)} technologies from prototypes")

        except Exception as e:
            logger.error(f"Failed to process technologies: {e}")
            raise
