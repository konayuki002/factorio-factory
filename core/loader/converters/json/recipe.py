import json
import logging
from pathlib import Path

from core.loader.converters.base import BaseConverter
from core.loader.registry import register

logger = logging.getLogger(__name__)


@register("json:recipe")
class RecipeJsonConverter(BaseConverter):
    """
    レシピに関するLua実行結果 -> JSONファイルの変換.
    lua:prototypesコンバータが生成したprototypes.jsonから
    recipeタイプのプロトタイプを抽出してrecipe.jsonを生成
    """

    dependencies = ["lua:prototypes"]  # Lua実行コンバータに依存
    json_recipe_path = "recipe.json"

    def load(self) -> None:
        try:
            # 1) lua:prototypesの結果を読み込み
            prototypes_file = Path(self.intermediate_dir) / "prototypes.json"
            if not prototypes_file.exists():
                logger.error(f"Prototypes file not found: {prototypes_file}")
                return

            with open(prototypes_file, "r", encoding="utf-8") as f:
                all_prototypes = json.load(f)

            # 2) recipeタイプのプロトタイプを抽出・フィルタリング
            recipes = []
            recipe_prototypes = all_prototypes.get("recipe", {})

            for _recipe_name, recipe_data in recipe_prototypes.items():
                # parametersサブグループは除外（元の処理と同様）
                if recipe_data.get("subgroup") == "parameters":
                    continue

                # typeがrecipeであることを確認（念のため）
                if recipe_data.get("type") == "recipe":
                    recipes.append(recipe_data)

            # 3) JSON出力
            json_path = Path(self.intermediate_dir) / self.json_recipe_path
            self.dump_json(recipes, str(json_path))

            logger.info(f"Extracted {len(recipes)} recipes from prototypes")

        except Exception as e:
            logger.error(f"Failed to process recipes: {e}")
            raise
