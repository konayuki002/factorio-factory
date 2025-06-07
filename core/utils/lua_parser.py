# core/utils/lua_parser.py（Lark を削除して luaparser ベースに差し替え）
from pathlib import Path
from luaparser import ast as lua_ast
from luaparser import astnodes
from typing import Any

import logging


def parse_lua(lua_filepath: str) -> list[dict]:
    """
    luaparser を使って .lua ファイルを AST 化し、
    data:extend({...}) の中身を Python の dict に変換して返す最小実装。
    """
    lua_path = Path(lua_filepath)
    code = lua_path.read_text(encoding="utf-8")
    tree = lua_ast.parse(code)
    result: list[dict] = []

    class ExtendVisitor(lua_ast.ASTVisitor):
        def visit_Invoke(self, node):
            # data:extend({...}) のパターンをざっくり検出
            # （完全網羅はあとで直すとして、とりあえず「data:extend」が来たら Table を dict にする）
            if (
                getattr(node.source, "id", None) == "data"
                and getattr(node.func, "id", None) == "extend"
            ):
                # 引数が複数あってもすべて処理
                for arg in node.args:
                    if isinstance(arg, astnodes.Table):
                        # テーブル部分を dict に変換して result に足す
                        result.append(_table_to_dict(arg))
            # 子ノードも巡回
            # self.visit_children(node)

    ExtendVisitor().visit(tree)
    return result


def _table_to_dict(table_node: astnodes.Table) -> dict | list:
    """
    luaparser の Table ノードを Python dict/list に落とし込む。
    """
    obj: dict[str, any] = {}
    arr: list[any] = []

    for field in table_node.fields:
        # field は astnodes.Field など
        key_node = field.key
        if key_node is None:
            raise ValueError("Lua テーブルのキーが None です。")

        val_node = field.value

        k = _lit_or_name(key_node)
        v = (
            _lit_or_name(val_node)
            if not isinstance(val_node, astnodes.Table)
            else _table_to_dict(val_node)
        )
        obj[k] = v

    if all(
        isinstance(key, int) and key == i + 1 for i, (key, _) in enumerate(obj.items())
    ):
        # key が 1始まりで連番 の場合は配列要素として扱う
        arr = list(obj.values())
        return arr
    else:
        # それ以外は key 付きの dict として返す
        return obj


def _lit_or_name(node):
    """
    リテラル or 識別子ならそのまま Python の基本型に変換するヘルパー。
    たとえば astnodes.String → str, astnodes.Number → int/float, astnodes.Name → 変数名文字列など。
    簡易実装例：
    """
    if isinstance(node, astnodes.String):
        return node.s
    if isinstance(node, astnodes.Number):
        return node.n
    if isinstance(node, astnodes.Nil):
        return None
    if isinstance(node, astnodes.Name):
        return node.id
    if isinstance(node, astnodes.FalseExpr):
        return False
    if isinstance(node, astnodes.TrueExpr):
        return True
    if isinstance(node, astnodes.MultOp):
        return {
            "node_type": "expr",
            "op": "mult",
            "left": _lit_or_name(node.left),
            "right": _lit_or_name(node.right),
        }
    if isinstance(node, astnodes.FloatDivOp):
        # astnodes.FloatDiv は除算演算子
        # 後段で厳密な有理数のSympy式に変換するために, まだ計算しない
        return {
            "node_type": "expr",
            "op": "float_div",
            "left": _lit_or_name(node.left),
            "right": _lit_or_name(node.right),
        }
    if isinstance(node, astnodes.UMinusOp):
        return -_lit_or_name(node.operand)
    if isinstance(node, astnodes.Concat):
        # astnodes.Concat は文字列連結
        return {
            "node_type": "concat",
            "left": _lit_or_name(node.left),
            "right": _lit_or_name(node.right),
        }
    if isinstance(node, astnodes.Index):
        return {
            "node_type": "field_chain",
            "index": _lit_or_name(node.idx),
            "value": _lit_or_name(node.value),
        }
    if isinstance(node, astnodes.Call):
        return {
            "node_type": "call",
            "func": _lit_or_name(node.func),
            "args": [_lit_or_name(arg) for arg in node.args],
        }

    # そのほかのノードはあれば文字列化して返すだけ
    logging.warning("Unsupported node type: %s", type(node).__name__)
    return str(node)


class LuaTableExtractor(lua_ast.ASTVisitor):
    def __init__(self):
        super().__init__()
        self.data_extend_tables = []
        self.resources_tables = []

    def visit_Invoke(self, node):
        # data:extend({...}) のパターンを検出してテーブルに変換
        if (
            getattr(node.source, "id", None) == "data"
            and getattr(node.func, "id", None) == "extend"
        ):
            # 引数が複数あってもすべて処理
            for arg in node.args:
                if isinstance(arg, astnodes.Table):
                    # テーブル部分を dict に変換して result に足す
                    self.data_extend_tables.append(_table_to_dict(arg))

    def visit_Call(self, node):
        # resources(...) のパターンを検出
        if getattr(node.func, "id", None) == "resources":
            for arg in node.args:
                if isinstance(arg, astnodes.Table):
                    # テーブル部分を dict に変換して result に足す
                    self.resources_tables.append(_table_to_dict(arg))


def parse_lua_file(path: str) -> dict[str, list[Any]]:
    """
    Lua ファイルを読み込んで AST を構築し、
    『data:extend』 と 『resources』 のテーブルコンストラクタを抽出して辞書で返す。
    戻り値のイメージ:
      {
        'data_extend': [ <テーブル辞書1>, <テーブル辞書2>, … ],
        'resources':   [ <テーブル辞書A>, <テーブル辞書B>, … ]
      }
    """
    # 1) ファイル読み込み
    with open(path, "r", encoding="utf-8") as f:
        lua_code = f.read()

    # 2) AST を構築
    try:
        tree = lua_ast.parse(lua_code)
    except Exception as e:
        # 失敗時はログを吐いて空の結果を返す、または例外を再送出
        raise RuntimeError(f"Lua のパースに失敗: {e}")

    # 3) ビジターで巡回
    extractor = LuaTableExtractor()
    extractor.visit(tree)

    # 4) 抽出されたリストをまとめて返す
    return {
        "data_extend": extractor.data_extend_tables,
        "resources": extractor.resources_tables,
    }
