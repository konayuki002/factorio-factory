import re
from lark import Lark, Transformer


def extract_data_extend_table(lua_code: str) -> str:
    # コメント行を除去
    code = re.sub(r"--.*", "", lua_code)
    # data:extendの位置を探す
    start = code.find("data:extend")
    if start == -1:
        raise ValueError("No data:extend found")
    paren = code.find("(", start)
    if paren == -1:
        raise ValueError("No opening parenthesis after data:extend")
    brace = code.find("{", paren)
    if brace == -1:
        raise ValueError("No opening brace after data:extend(")
    count = 0
    for i in range(brace, len(code)):
        if code[i] == "{":
            count += 1
        elif code[i] == "}":
            count -= 1
            if count == 0:
                return code[brace : i + 1]
    raise ValueError("No matching closing brace found")


class LuaTableTransformer(Transformer):
    def table(self, items):
        # テーブルが { ... } のみの場合はリスト、{key=val,...} ならdict
        if all(isinstance(i, tuple) and len(i) == 2 for i in items):
            return dict(items)
        return list(items)

    def pair(self, items):
        return (items[0].strip('"'), items[1])

    def SIGNED_NUMBER(self, s):
        # 整数か小数かで型を分ける
        s = str(s)
        if "." in s or "e" in s or "E" in s:
            return float(s)
        else:
            return int(s)

    def ESCAPED_STRING(self, s):
        return s[1:-1]

    def true(self, _):
        return True

    def false(self, _):
        return False


def parse_lua(lua_filepath: str) -> dict:
    with open(lua_filepath, encoding="utf-8") as f:
        lua_code = f.read()

    table_text = extract_data_extend_table(lua_code)

    # LarkでLuaテーブルをパース（末尾カンマ許容）
    lua_table_grammar = r"""
        ?start: table
        ?table: "{" [pair_or_table ("," pair_or_table)* [","]] "}"
        ?pair_or_table: pair | table
        pair: (NAME | ESCAPED_STRING) "=" value
        ?value: ESCAPED_STRING
                | SIGNED_NUMBER
                | table
                | "true"    -> true
                | "false"   -> false
        %import common.ESCAPED_STRING
        %import common.SIGNED_NUMBER
        %import common.CNAME -> NAME
        %import common.WS
        %ignore WS
    """

    parser = Lark(lua_table_grammar, start="start")
    data = LuaTableTransformer().transform(parser.parse(table_text))

    return data
