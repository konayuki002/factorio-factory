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

# converters パッケージのディレクトリを動的に読み取る
json_module_name = "core.loader.converters.json"
package = importlib.import_module(json_module_name)
package_path = pathlib.Path(package.__path__[0])

# *.py モジュールをひとつずつインポート
for file in package_path.iterdir():
    if file.suffix == ".py" and file.name != "__init__.py":
        module_name = f"core.loader.converters.json.{file.stem}"
        importlib.import_module(module_name)

# enum モジュールも同様にインポート
enum_module_name = "core.loader.converters.enum"
package = importlib.import_module(enum_module_name)
package_path = pathlib.Path(package.__path__[0])
# *.py モジュールをひとつずつインポート
for file in package_path.iterdir():
    if file.suffix == ".py" and file.name != "__init__.py":
        module_name = f"core.loader.converters.enum.{file.stem}"
        importlib.import_module(module_name)

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
