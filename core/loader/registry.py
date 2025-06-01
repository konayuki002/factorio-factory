# core/loader/registry.py
import importlib
import pathlib

# -- まず, register & CONVERTERS を定義 --

CONVERTERS = {}


def register(name: str):
    """
    コンバータークラスを登録するデコレータ。
    使用例:
        @register("item_group_json")
        class ItemGroupJsonConverter(BaseConverter):
            ...
    """

    def _decorator(cls):
        CONVERTERS[name] = cls()
        return cls

    return _decorator


# -- 次に, 動的インポートの処理 --


def dynamic_import_one_by_one(module_name: str):
    """
    指定されたモジュール以下のモジュールを動的にインポートする。
    モジュール名は 'core.loader.converters.json' のような形式で指定。
    """
    package = importlib.import_module(module_name)
    package_path = pathlib.Path(package.__path__[0])

    # *.py モジュールをひとつずつインポート
    for file in package_path.iterdir():
        if file.suffix == ".py" and file.name != "__init__.py":
            module_name = f"{module_name}.{file.stem}"
            importlib.import_module(module_name)


# Lua -> JSON変換パッケージのディレクトリを動的に読み取る
json_converters_module_name = "core.loader.converters.json"
dynamic_import_one_by_one(json_converters_module_name)

# Enum -> Python Enum クラス変換パッケージのディレクトリを動的に読み取る
enum_converters_module_name = "core.loader.converters.enum"
dynamic_import_one_by_one(enum_converters_module_name)

# ここまでで、converters/ 内の各モジュールが一度インポートされ、
# それぞれのクラス定義に付いた @register() が実行される。


# -- 順序付きの load_all 関数 --


def load_all():
    """
    まず, *_jsonのConverterを順番に実行
    その後, *_enumのConverterを順番に実行
    """

    for name, conv in CONVERTERS.items():
        if name.startswith("json:"):
            print(f"[registry] Running JSON converter: {name}")
            conv.load()

    for name, conv in CONVERTERS.items():
        if name.startswith("enum:"):
            print(f"[registry] Running Enum converter: {name}")
            conv.load()
