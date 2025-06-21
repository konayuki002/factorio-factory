# factorio_factory/core/loader/__main__.py
import argparse
import logging
from pathlib import Path


def run_converters(stage: str = "all", log_level: str = "INFO") -> None:
    """
    コンバーターを実行する関数。
    stage引数に応じて、Lua -> JSON変換、JSON -> Enumクラス生成を行う。
    """
    from core.loader.registry import sorted_order

    logging.basicConfig(
        level=getattr(logging, log_level, logging.INFO),
    )

    # トポロジカルソートで依存関係を解決
    sorted_converters = sorted_order()

    # 指定されたステージに応じてコンバーターを実行
    stage_prefixes = {
        "json": ["json:"],
        "enum": ["enum:"],
        "data": ["data:"],
        "allowed": ["allowed:"],
        "model": ["data:", "allowed:"],
    }

    for conv in sorted_converters:
        if stage == "all":
            # 全てのステージを実行
            conv.load()
        elif any(
            conv.name.startswith(prefix) for prefix in stage_prefixes.get(stage, [])
        ):
            # 指定されたステージに該当するコンバーターのみ実行
            conv.load()


def clean_artifacts() -> None:
    """
    data/intermediate 以下の JSON ファイルや
    core/enum/*.py, core/01_models/*.py などを一括削除する。
    """
    # 例: data/intermediate/*.json をすべて削除
    intermediate_dir = Path(__file__).parents[2] / "data" / "intermediate"
    for file in intermediate_dir.glob("*.json"):
        file.unlink(missing_ok=True)

    # core/enum/*.py を削除（__init__.py は残す、あるいは判定ロジックを入れてもよい）
    enum_dir = Path(__file__).parents[2] / "core" / "enums"
    for file in enum_dir.glob("*.py"):
        if file.name != "__init__.py" and not file.name.startswith("manual_"):
            # manual_で始まるファイルは削除しない
            file.unlink(missing_ok=True)

    # core/data/*.py を削除（__init__.py は残す）
    data_dir = Path(__file__).parents[2] / "core" / "data"
    for file in data_dir.glob("*.py"):
        if file.name != "__init__.py" and not file.name.startswith("manual_"):
            file.unlink(missing_ok=True)

    # core/allowed/*.py を削除（__init__.py は残す）
    allowed_dir = Path(__file__).parents[2] / "core" / "allowed"
    for file in allowed_dir.glob("*.py"):
        if file.name != "__init__.py" and not file.name.startswith("manual_"):
            # manual_で始まるファイルは削除しない
            file.unlink(missing_ok=True)

    # 以下はmodelの自動生成の実装前なのでコメントアウト
    # core/01_models/*.py を同様に削除する
    # models_dir = Path(__file__).parents[2] / "core" / "01_models"
    # for file in models_dir.glob("0*_*.py"):
    #     file.unlink(missing_ok=True)

    logging.info("Cleaned up intermediate files and models.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Factorio Factory Loader", prog="core.loader"
    )
    # ログレベルと出力ディレクトリのオプション
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Set log level (DEBUG, INFO, WARNING, ERROR)",
    )

    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("build-json", help="Build JSON files from Lua data")
    sub.add_parser("build-enum", help="Build Enum classes from JSON data")
    sub.add_parser("build-data", help="Build data dict from JSON data and Enum classes")
    sub.add_parser(
        "build-allowed",
        help="Build allowed enum sets for submodel from JSON data and Enum classes",
    )
    sub.add_parser("build-model", help="Build Pydantic models from JSON data")
    sub.add_parser("build-all", help="Build all stages (JSON, Enum, Model)")
    sub.add_parser("clean", help="Clean up intermediates")

    args = parser.parse_args()

    if args.cmd == "build-json":
        run_converters(stage="json", log_level=args.log_level)
    elif args.cmd == "build-enum":
        run_converters(stage="enum", log_level=args.log_level)
    elif args.cmd == "build-data":
        run_converters(stage="data", log_level=args.log_level)
    elif args.cmd == "build-allowed":
        run_converters(stage="allowed", log_level=args.log_level)
    elif args.cmd == "build-model":
        run_converters(stage="model", log_level=args.log_level)
    elif args.cmd == "build-all":
        run_converters(stage="all", log_level=args.log_level)
    elif args.cmd == "clean":
        clean_artifacts()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
