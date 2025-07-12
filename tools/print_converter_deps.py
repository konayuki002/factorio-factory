#!/usr/bin/env python3
"""
コンバータ依存関係をGraphviz dot形式で出力するスクリプト
"""
from core.loader.registry import DEPS


def main() -> None:
    """
    使い方:
    1. このスクリプトを実行する前に、コンバータを登録しておく必要があります。
    2. 以下のコマンドを実行して依存関係を出力します:
       PYTHONPATH=. python3 tools/print_converter_deps.py
    """
    print("digraph converters {")
    for name, deps in DEPS.items():
        for dep in deps:
            print(f'    "{dep}" -> "{name}";')
    print("}")


if __name__ == "__main__":
    main()
