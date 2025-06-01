# core/loader/registry.py
import importlib
import pathlib
from collections import defaultdict, deque
from core.loader.converters.base import BaseConverter

# -- まず, register & CONVERTERS を定義 --
CONVERTERS: dict[str, BaseConverter] = {}
DEPS: dict[str, list[str]] = {}  # name -> 依存フェーズキー名リスト


def register(name: str):
    """
    コンバータークラスを登録するデコレータ。dependencies 属性を読み取り、DEPSにも追加する。
    使用例:
        @register("json:item_group")
        class ItemGroupsJsonConverter(BaseConverter):
            dependencies = []  # JSON は依存なし
            ...

        @register("enum:item_group")
        class ItemGroupsEnumConverter(BaseConverter):
            dependencies = ["json:item_group"]
            ...
    """

    def _decorator(cls):
        instance = cls()
        CONVERTERS[name] = instance
        # そのクラスが持つ dependencies 属性を DEPS に保存
        # （もし dependencies が定義されていなければ空リストとみなす）
        DEPS[name] = getattr(instance, "dependencies", []) or []
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

    for file in package_path.iterdir():
        if file.suffix == ".py" and file.name != "__init__.py":
            submod = f"{module_name}.{file.stem}"
            importlib.import_module(submod)


# Lua -> JSON変換パッケージのディレクトリを動的に読み取る
json_converters_module_name = "core.loader.converters.json"
dynamic_import_one_by_one(json_converters_module_name)

# Enum -> Python Enum クラス変換パッケージのディレクトリを動的に読み取る
enum_converters_module_name = "core.loader.converters.enum"
dynamic_import_one_by_one(enum_converters_module_name)

# ここまでで、converters/ 内の各モジュールがインポートされ、
# それぞれのクラス定義に付いた @register(...) が実行され、CONVERTERS と DEPS が埋まる。


# -- トポロジカルソート関数を定義 --
def sorted_order() -> list[BaseConverter]:
    """
    DEPS をもとにトポロジカルソートを行い、
    依存フェーズが解決された順に BaseConverter のインスタンスを返す。
    """
    # 1) 入次数を初期化
    in_degree: dict[str, int] = defaultdict(int)
    graph: dict[str, list[str]] = defaultdict(list)

    # まずすべてのノードの in_degree を 0 にしておく
    for name in CONVERTERS.keys():
        in_degree[name] = 0

    # DEPS をもとにグラフと in_degree を構築
    for name, deps in DEPS.items():
        for d in deps:
            # 依存先 d が存在しない場合はエラーにしてもよいが、ここでは空ノード扱い
            if d not in CONVERTERS:
                raise RuntimeError(
                    f"Converter '{name}' が依存している '{d}' が未登録です。"
                )
            # d → name の有向辺を作成し、name の in_degree を増やす
            graph[d].append(name)
            in_degree[name] += 1

    # 2) 入次数 0 のノードをキューに入れる
    queue = deque([n for n, deg in in_degree.items() if deg == 0])
    order: list[BaseConverter] = []

    # 3) キューを使って拓扑ソート
    while queue:
        n = queue.popleft()
        order.append(CONVERTERS[n])
        for nxt in graph[n]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    # 4) すべてのノードが処理されたかチェック（サイクル検出）
    if len(order) != len(CONVERTERS):
        # 拡張としてサイクル検出の詳細メッセージを作ってもよい
        remaining = set(CONVERTERS.keys()) - {
            c_key
            for c_inst in order
            for c_key, c_val in CONVERTERS.items()
            if c_val is c_inst
        }
        raise RuntimeError(
            f"依存関係にサイクルがある可能性があります。未処理ノード: {remaining}"
        )

    return order


# -- 順序付き load_all --
def load_all():
    """
    トポロジカルソート済みの順番で、登録された各 Converter の load() を実行する。
    """
    print("[registry] 依存関係をもとにした実行順を計算中...")
    ordered_converters = sorted_order()
    for conv in ordered_converters:
        # conv から名前を取得したいので逆引きするか、
        # conv インスタンスに name 属性を持たせているならそれを参照してもよい
        # ここでは単純にインスタンスのクラス名を表示例として使う
        print(
            f"[registry] Running converter: {conv.__class__.__name__} (dependencies: {conv.dependencies})"
        )
        conv.load()
