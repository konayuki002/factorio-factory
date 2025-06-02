from core.utils.utils import to_enum_member
import logging


class BaseConverter:
    """
    全コンバーターのためのベースクラス.
    Luaファイルを読み込み、JSON形式に変換、
    またはJSONファイルからデータを読み込み、
    Enumクラスを生成するための基本的なインターフェースを提供します。
    """

    dependencies: list[str] = []  # "json:item_group" のような形式で依存関係を指定
    lua_path: str = ""
    json_path: str = ""
    raw_dir: str = "data/raw"
    intermediate_dir: str = "data/intermediate"
    enum_dir: str = "core/enums"

    def __init__(self):
        # サブクラスで個別に依存を持たせたい場合の取り込み
        self.dependencies: list[str] = self.__class__.dependencies

    def load(self):
        """
        Luaファイルを読み込み、JSON形式に変換するための基本的なインターフェースを提供します。
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def parse_lua(self, lua_code: str) -> dict:
        """
        Luaコードをパースして辞書形式に変換します。
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def dump_json(self, data: list, json_path: str):
        """
        JSON形式でデータをファイルに保存します。
        :param data: 保存するデータ（リスト形式）
        :param json_path: JSONファイルが保存されるパス
        :return: 保存されたデータ
        """
        import json
        import os

        # ディレクトリが存在しない場合は作成
        os.makedirs(os.path.dirname(json_path), exist_ok=True)
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data dumped to {json_path}")
        return data

    def load_json(self, json_path: str) -> list:
        """
        JSONファイルからデータを読み込みます。
        :param json_path: JSONファイルのパス（例: "data/intermediate/item_groups.json"）
        :return: JSONファイルから読み込まれたデータ
        """
        import json

        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"Data loaded from {json_path}")
        return data

    def merge_unique(self, base: list[str], extra: list[str]) -> list[str]:
        """
        2つのリストを結合し、重複を排除して順序を維持します。
        重複する場合, 警告を出して基本のリストの順序を優先します。
        :param base: 基本のリスト
        :param extra: 追加するリスト
        :return: 重複を排除した新しいリスト
        """
        logger = logging.getLogger(__name__)
        seen = set(base)
        result = base[:]
        for x in extra:
            if x in seen:
                logger.warning("'%s' is a duplicate and will be ignored.", x)
            else:
                result.append(x)
                seen.add(x)
        return result

    def gen_enum(self, enum_name: str, members: list, enum_path: str):
        """
        Enumクラスを動的に生成し、指定されたパスに保存します。
        :param enum_name: Enumクラスの名前（例: "ItemGroup"）
        :param members: Enumのメンバー名のリスト（例: ["iron-plate", "copper-plate"]）
        :param enum_path: Enumクラスを保存するファイルのパス（例: "core/enums/item_group.py"）
        """
        from enum import Enum

        # Enumクラスを動的に生成

        # 変換: kebab-case -> UpperCamelCase
        member_map = {to_enum_member(member): member for member in members}
        enum_class = Enum(enum_name, member_map)
        # Enumクラスをモジュールの属性として追加
        module = __import__(__name__)
        setattr(module, enum_name, enum_class)
        # Enumをファイルに保存
        with open(enum_path, "w", encoding="utf-8") as f:
            f.write(f"from enum import Enum\n\n\nclass {enum_name}(Enum):\n")
            for key, value in member_map.items():
                f.write(f"    {key} = '{value}'\n")
        print(f"Enum {enum_name} saved to {enum_path}")
        return enum_class
