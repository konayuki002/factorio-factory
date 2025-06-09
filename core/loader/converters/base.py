from enum import Enum
from core.utils.utils import to_enum_member
from typing import Any, cast
import logging


logger = logging.getLogger(__name__)


class BaseConverter:
    """
    全コンバーターのためのベースクラス.
    Luaファイルを読み込み、JSON形式に変換、
    またはJSONファイルからデータを読み込み、
    Enumクラスを生成するための基本的なインターフェースを提供します。
    """

    dependencies: list[str] = []  # "json:item_group" のような形式で依存関係を指定
    lua_filename: str = ""
    json_path: str = ""
    raw_dir: str = "data/raw"
    intermediate_dir: str = "data/intermediate"
    enum_dir: str = "core/enums"

    def __init__(self, name: str = ""):
        # サブクラスで個別に依存を持たせたい場合の取り込み
        self.dependencies: list[str] = self.__class__.dependencies
        self.name = name

    def load(self) -> None:
        """
        Luaファイルを読み込み、JSON形式に変換するための基本的なインターフェースを提供します。
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def dump_json(
        self, data: list[dict[str, Any]], json_path: str
    ) -> list[dict[str, Any]]:
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
        logger.info(f"Data dumped to {json_path}")
        return data

    def load_json(self, json_path: str) -> list[dict[str, Any]]:
        """
        JSONファイルからデータを読み込みます。
        :param json_path: JSONファイルのパス（例: "data/intermediate/item_groups.json"）
        :return: JSONファイルから読み込まれたデータ
        """
        import json

        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        logger.info(f"Data loaded from {json_path}")
        return cast(list[dict[str, Any]], data)

    def merge_unique(
        self, base: list[str], extra: list[str], enum_name: str = "UnknownEnum"
    ) -> list[str]:
        """
        2つのリストを結合し、重複を排除して順序を維持します。
        重複する場合, 警告を出して基本のリストの順序を優先します。
        大文字と小文字は区別されるため, 渡す前に適切に処理してください。
        :param base: 基本のリスト
        :param extra: 追加するリスト
        :param enum_name: Enumの名前（デバッグ用, 例: "ItemGroup"）
        :return: 重複を排除した新しいリスト
        """
        seen = set(base)
        result = base[:]
        for x in extra:
            if x in seen:
                logger.warning(
                    "[%s] '%s' is a duplicate and will be ignored when merging Enum members (base: %s, extra: %s)",
                    enum_name,
                    x,
                    base,
                    extra,
                )
            else:
                result.append(x)
                seen.add(x)
        return result

    def gen_enum(
        self, enum_name: str, members: list[str], enum_path: str
    ) -> type[Enum]:
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
        enum_class = Enum(enum_name, member_map)  # type: ignore[misc]

        # Enumをファイルに保存
        import os

        enum_dir = os.path.dirname(enum_path)
        if not os.path.isdir(enum_dir):
            # 本プロジェクトではenums/.gitkeepでディレクトリを確保しており、
            # 誤った場所へのファイル生成を防ぐため明示的なエラー通知を優先しています
            raise FileNotFoundError(f"Enum出力先ディレクトリが存在しません: {enum_dir}")
        with open(enum_path, "w", encoding="utf-8") as f:
            f.write(f"from enum import Enum\n\n\nclass {enum_name}(Enum):\n")
            for key, value in member_map.items():
                f.write(f"    {key} = '{value}'\n")
        logger.info(f"Enum {enum_name} saved to {enum_path}")
        return enum_class
