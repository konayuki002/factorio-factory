import json
import logging
from pathlib import Path

from core.loader.converters.base import BaseConverter
from core.loader.registry import register

logger = logging.getLogger(__name__)


@register("json:item_group")
class ItemGroupJsonConverter(BaseConverter):
    """
    lua:prototypesの結果からitem_groups.jsonとitem_subgroups.jsonを生成
    item-groupタイプとitem-subgroupタイプのプロトタイプを抽出
    """

    dependencies = ["lua:prototypes"]  # Lua実行コンバータに依存
    json_groups_path = "item_groups.json"
    json_subgroups_path = "item_subgroups.json"

    def load(self) -> None:
        try:
            # 1) lua:prototypesの結果を読み込み
            prototypes_file = Path(self.intermediate_dir) / "prototypes.json"
            if not prototypes_file.exists():
                logger.error(f"Prototypes file not found: {prototypes_file}")
                return

            with open(prototypes_file, "r", encoding="utf-8") as f:
                all_prototypes = json.load(f)

            # 2) item-groupタイプのプロトタイプを抽出
            groups = []
            group_prototypes = all_prototypes.get("item-group", {})

            for group_name, group_data in group_prototypes.items():
                if group_data.get("type") == "item-group":
                    groups.append(group_data)

            # 3) item-subgroupタイプのプロトタイプを抽出
            subgroups = []
            subgroup_prototypes = all_prototypes.get("item-subgroup", {})

            for subgroup_name, subgroup_data in subgroup_prototypes.items():
                if subgroup_data.get("type") == "item-subgroup":
                    subgroups.append(subgroup_data)

            # 4) JSON出力
            groups_path = Path(self.intermediate_dir) / self.json_groups_path
            self.dump_json(groups, str(groups_path))

            subgroups_path = Path(self.intermediate_dir) / self.json_subgroups_path
            self.dump_json(subgroups, str(subgroups_path))

            logger.info(
                f"Extracted {len(groups)} item groups and {len(subgroups)} subgroups from prototypes"
            )

        except Exception as e:
            logger.error(f"Failed to process item groups: {e}")
            raise
