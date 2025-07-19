import json
import logging
from pathlib import Path

from core.loader.converters.base import BaseConverter
from core.loader.registry import register

logger = logging.getLogger(__name__)


@register("json:item")
class ItemJsonConverter(BaseConverter):
    """
    アイテムに関するLua実行結果 -> JSONファイルの変換.
    lua:prototypesコンバータが生成したprototypes.jsonから
    itemタイプのプロトタイプを抽出してitem.jsonを生成
    """

    dependencies = ["lua:prototypes"]  # Lua実行コンバータに依存
    json_items_path = "item.json"

    capable_subgroups = [
        "capsule",
        "item",
        "repair-tool",
        "tool",
        "item-with-entity-data",
        "rail-planner",
        "module",
        "ammo",
        "gun",
        "armor",
    ]

    def load(self) -> None:
        # prototypes.jsonからデータを読み込み
        prototypes_path = Path(self.intermediate_dir) / "prototypes.json"
        with open(prototypes_path, encoding="utf-8") as f:
            all_prototypes = json.load(f)

        # capable_subgroupsに該当するアイテムタイプのプロトタイプを抽出
        items = []
        for prototype_type in self.capable_subgroups:
            type_prototypes = all_prototypes.get(prototype_type, {})
            for item_name, item_data in type_prototypes.items():
                # 隠しアイテムをスキップ（hidden: trueのアイテム）
                if item_data.get("hidden", False):
                    continue
                # subgroupキーが存在しない場合や"parameters"の場合はスキップ
                if item_data.get("subgroup") == "parameters":
                    continue
                items.append(item_data)

        # JSON出力
        json_items_path = Path(self.intermediate_dir) / self.json_items_path
        self.dump_json(items, str(json_items_path))
