# core/utils/lua_parser.py
from pathlib import Path
from typing import Any, Union, List, Dict
import logging
from functools import singledispatch

from luaparser import ast as lua_ast
from luaparser import astnodes

Jsonable = Union[Dict[str, Any], List[Any]]


# ──────────────────────────────────────────────────────────────
# node → Python 型／構造への変換
# ──────────────────────────────────────────────────────────────
@singledispatch
def _convert_node(node: astnodes.Node) -> Any:
    logging.warning("Unsupported node type: %s", type(node).__name__)
    return str(node)


@_convert_node.register
def _(node: astnodes.String) -> str:
    return node.s


@_convert_node.register
def _(node: astnodes.Number) -> Union[int, float]:
    return node.n


@_convert_node.register
def _(node: astnodes.Nil) -> None:
    return None


@_convert_node.register
def _(node: astnodes.Name) -> str:
    return node.id


@_convert_node.register
def _(node: astnodes.FalseExpr) -> bool:
    return False


@_convert_node.register
def _(node: astnodes.TrueExpr) -> bool:
    return True


# 二項演算子系は共通処理へ
def _binary_expr(
    op_name: str, left: astnodes.Node, right: astnodes.Node
) -> Dict[str, Any]:
    return {
        "node_type": "expr",
        "op": op_name,
        "left": _convert_node(left),
        "right": _convert_node(right),
    }


@_convert_node.register
def _(node: astnodes.MultOp) -> Dict[str, Any]:
    return _binary_expr("mult", node.left, node.right)


@_convert_node.register
def _(node: astnodes.FloatDivOp) -> Dict[str, Any]:
    return _binary_expr("float_div", node.left, node.right)


@_convert_node.register
def _(node: astnodes.SubOp) -> Dict[str, Any]:
    return _binary_expr("sub", node.left, node.right)


@_convert_node.register
def _(node: astnodes.Concat) -> Dict[str, Any]:
    return {
        "node_type": "concat",
        "left": _convert_node(node.left),
        "right": _convert_node(node.right),
    }


@_convert_node.register
def _(node: astnodes.UMinusOp) -> Any:
    return -_convert_node(node.operand)


@_convert_node.register
def _(node: astnodes.Index) -> Dict[str, Any]:
    return {
        "node_type": "field_chain",
        "index": _convert_node(node.idx),
        "value": _convert_node(node.value),
    }


@_convert_node.register
def _(node: astnodes.Call) -> Dict[str, Any]:
    return {
        "node_type": "call",
        "func": _convert_node(node.func),
        "args": [_convert_node(arg) for arg in node.args],
    }


@_convert_node.register
def _(node: astnodes.Table) -> Jsonable:
    return _table_to_py(node)


# ──────────────────────────────────────────────────────────────
# Table ノード → dict / list 変換
# ──────────────────────────────────────────────────────────────
def _table_to_py(table: astnodes.Table) -> Jsonable:
    obj: Dict[Any, Any] = {}
    for field in table.fields:
        if field.key is None:
            raise ValueError("Lua テーブルのキーが None です。")
        key = _convert_node(field.key)
        value = _convert_node(field.value)
        obj[key] = value

    # 1-based 連番キーなら list に変換
    if _is_array_like(obj):
        return list(obj.values())
    return obj


def _is_array_like(d: Dict[Any, Any]) -> bool:
    return all(isinstance(k, int) and k == idx + 1 for idx, k in enumerate(d.keys()))


# ──────────────────────────────────────────────────────────────
# AST から data:extend / resource 呼び出し部分を抽出
# ──────────────────────────────────────────────────────────────
class LuaTableExtractor(lua_ast.ASTVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.data_extend_tables: List[Dict[str, Any]] = []

    def visit_Invoke(self, node: astnodes.Invoke) -> None:
        src_id = getattr(node.source, "id", None)
        func_id = getattr(node.func, "id", None)
        if src_id != "data" or func_id != "extend":
            return

        if len(node.args) != 1:
            logging.warning("data:extend の引数が1つではありません: %d", len(node.args))
            return

        arg = node.args[0]
        if not isinstance(arg, astnodes.Table):
            logging.warning(
                "data:extend の引数がテーブルではありません: %s", type(arg).__name__
            )
            return

        for field in arg.fields:
            self._handle_field_value(field.value)

    def _handle_field_value(self, val: astnodes.Node) -> None:
        if isinstance(val, astnodes.Table):
            self.data_extend_tables.append(_table_to_py(val))
            return

        if (
            isinstance(val, astnodes.Call)
            and getattr(val.func, "id", None) == "resource"
        ):
            merged: Dict[str, Any] = {}
            for sub in val.args:
                if isinstance(sub, astnodes.Table):
                    merged.update(_table_to_py(sub))
            self.data_extend_tables.append(merged)
            return

        logging.warning(
            "Unsupported expression in data:extend: %s",
            getattr(val, "func", getattr(val, "id", type(val).__name__)),
        )


# ──────────────────────────────────────────────────────────────
# 公開関数
# ──────────────────────────────────────────────────────────────
def parse_lua_file(path: Union[str, Path]) -> List[Dict[str, Any]]:
    """
    Lua ファイルを読み込んで AST を構築し、
    data:extend と resource(...) のテーブル部分を dict リストで返す。
    """
    code = Path(path).read_text(encoding="utf-8")
    try:
        tree = lua_ast.parse(code)
    except Exception as e:
        raise RuntimeError(f"Lua のパースに失敗: {e!s}")

    extractor = LuaTableExtractor()
    extractor.visit(tree)
    return extractor.data_extend_tables
