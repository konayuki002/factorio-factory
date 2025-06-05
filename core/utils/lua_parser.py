# core/utils/lua_parser.py（Lark を削除して luaparser ベースに差し替え）
from pathlib import Path
from luaparser import ast as lua_ast
from luaparser import astnodes


def parse_lua(lua_filepath: str) -> list[dict]:
    """
    luaparser を使って .lua ファイルを AST 化し、
    data:extend({...}) の中身を Python の dict に変換して返す最小実装。
    """
    lua_path = Path(lua_filepath)
    code = lua_path.read_text(encoding="utf-8")
    print("x")
    tree = lua_ast.parse(code)
    print("z")
    result: list[dict] = []

    class ExtendVisitor(lua_ast.ASTVisitor):
        def visit_Call(self, node):
            # data:extend({...}) のパターンをざっくり検出
            # （完全網羅はあとで直すとして、とりあえず「data:extend」が来たら Table を dict にする）
            if (
                isinstance(node.func, astnodes.Index)
                and getattr(node.func.idx, "id", None) == "extend"
                and getattr(node.func.value, "id", None) == "data"
            ):
                # 引数が複数あってもすべて処理
                for arg in node.args:
                    if isinstance(arg, astnodes.Table):
                        # テーブル部分を dict に変換して result に足す
                        result.append(_table_to_dict(arg))
            # 子ノードも巡回
            # self.visit_children(node)

    print("a")
    ExtendVisitor().visit(tree)
    print("b")
    return result


def _table_to_dict(table_node: astnodes.Table) -> dict:
    """
    luaparser の Table ノードを Python dict/list に落とし込む最小例。
    面倒であれば「{ key = value, ... }」だけ拾って返す実装でもOKです。
    """
    obj: dict[str, any] = {}
    arr: list[any] = []

    for field in table_node.fields:
        # field は astnodes.Field など
        key_node = field.key  # 省略：key が None の場合は配列要素として扱う
        val_node = field.value

        # 「key = value」の場合
        if key_node is not None:
            k = _lit_or_name(key_node)
            v = (
                _lit_or_name(val_node)
                if not isinstance(val_node, astnodes.Table)
                else _table_to_dict(val_node)
            )
            obj[k] = v
        else:
            # 配列要素（{123, "hoge", {...} }みたいな場合）
            if isinstance(val_node, astnodes.Table):
                arr.append(_table_to_dict(val_node))
            else:
                arr.append(_lit_or_name(val_node))

    # Lua の混在テーブル対応（key付きと配列要素の併存）
    if obj and not arr:
        return obj
    elif arr and not obj:
        return arr  # 純配列として返す
    else:
        # key 付きと配列要素が混ざっていたら、両方いっしょの dict に突っ込む
        obj["_arr"] = arr
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
    # そのほかのノードは文字列化して返すだけ（とりあえず）
    return str(node)
