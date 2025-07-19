#!/usr/bin/env python3
"""
Lua実行ベースのコンバータシステムのテストスクリプト
"""

import sys
from pathlib import Path

# プロジェクトルートをPythonパスに追加
sys.path.insert(0, str(Path(__file__).parent))

from core.loader.registry import load_all


def test_lua_converter_integration() -> None:
    """Lua実行コンバータの統合テスト"""
    print("=== Testing Lua-based Converter Integration ===")

    try:
        # 全コンバータを実行
        load_all()
        print("✅ All converters executed successfully!")

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

        print("\n=== Generated Files Check ===")
        for filename in important_files:
            filepath = intermediate_dir / filename
            if filepath.exists():
                print(f"✅ {filename}: {filepath.stat().st_size} bytes")
            else:
                print(f"❌ {filename}: NOT FOUND")

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    test_lua_converter_integration()
