import json
import logging
from pathlib import Path

from core.loader.converters.base import BaseConverter
from core.loader.registry import register

logger = logging.getLogger(__name__)


@register("json:fluid")
class FluidJsonConverter(BaseConverter):
    """
    lua:prototypesの結果からfluid.jsonを生成
    fluidタイプのプロトタイプを抽出
    """

    dependencies = ["lua:prototypes"]  # Lua実行コンバータに依存
    json_fluids_path = "fluid.json"

    def load(self) -> None:
        try:
            # 1) lua:prototypesの結果を読み込み
            prototypes_file = Path(self.intermediate_dir) / "prototypes.json"
            if not prototypes_file.exists():
                logger.error(f"Prototypes file not found: {prototypes_file}")
                return

            with open(prototypes_file, "r", encoding="utf-8") as f:
                all_prototypes = json.load(f)

            # 2) fluidタイプのプロトタイプを抽出・フィルタリング
            fluids = []
            fluid_prototypes = all_prototypes.get("fluid", {})

            for fluid_name, fluid_data in fluid_prototypes.items():
                # parametersサブグループは除外（元の処理と同様）
                if fluid_data.get("subgroup") == "parameters":
                    continue

                # hiddenフラグがtrueのアイテムも除外
                if fluid_data.get("hidden", False):
                    continue

                # typeがfluidであることを確認（念のため）
                if fluid_data.get("type") == "fluid":
                    fluids.append(fluid_data)

            # 3) JSON出力
            json_path = Path(self.intermediate_dir) / self.json_fluids_path
            self.dump_json(fluids, str(json_path))

            logger.info(f"Extracted {len(fluids)} fluids from prototypes")

        except Exception as e:
            logger.error(f"Failed to process fluids: {e}")
            raise
