#!/usr/bin/env python3
"""
Lua実行ベースのコンバータシステムのテストスクリプト
"""

import logging
import sys
from pathlib import Path

# プロジェクトルートをPythonパスに追加
sys.path.insert(0, str(Path(__file__).parent))

from core.loader.registry import load_all

# テスト用ロガー設定
logger = logging.getLogger(__name__)


def test_lua_converter_integration() -> None:
    """Lua実行コンバータの統合テスト"""
    logger.info("Testing Lua-based Converter Integration")

    try:
        # 全コンバータを実行
        load_all()
        logger.info("All converters executed successfully")

        # 生成されたファイルを確認
        intermediate_dir = Path("data/intermediate")
        important_files = [
            "item.json",
            "recipe.json",
            "entities.json",
            "mining_drill.json",
            "technology.json",
            "fluid.json",
        ]

        logger.info("Checking generated files")
        for filename in important_files:
            filepath = intermediate_dir / filename
            if filepath.exists():
                logger.info(
                    "Generated file %s: %d bytes", filename, filepath.stat().st_size
                )
            else:
                logger.error("Generated file %s: NOT FOUND", filename)
                raise FileNotFoundError(f"Expected file {filename} was not generated")

    except Exception as e:
        logger.error("Error during Lua converter integration test: %s", e)
        raise


if __name__ == "__main__":
    # スタンドアロン実行時のログ設定
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    test_lua_converter_integration()
