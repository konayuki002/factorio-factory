import re
from lark import Lark, Transformer


def extract_data_extend_tables(lua_code: str) -> list[str]:
    # コメント行を除去
    code = re.sub(r"--.*", "", lua_code)
    tables = []
    pos = 0
    while True:
        start = code.find("data:extend", pos)
        if start == -1:
            break
        paren = code.find("(", start)
        if paren == -1:
            break
        brace = code.find("{", paren)
        if brace == -1:
            break
        count = 0
        for i in range(brace, len(code)):
            if code[i] == "{":
                count += 1
            elif code[i] == "}":
                count -= 1
                if count == 0:
                    tables.append(code[brace : i + 1])
                    pos = i + 1
                    break
        else:
            break
    return tables


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

    def NAME(self, s):
        # Luaの識別子はそのまま文字列として扱う
        return str(s)

    def true(self, _):
        return True

    def false(self, _):
        return False

    def binop(self, items):
        left, op_token, right = items  # items[1] が演算子トークン
        op = str(op_token)
        # ここでは「とりあえず文字列に連結して返す」例
        return f"{left} {op} {right}"

    def dotted_name(self, items):
        # 例: ['item_sounds', 'brick_inventory_move'] → 'item_sounds.brick_inventory_move'
        return ".".join(str(i) for i in items)

    def FUNC_CALL(self, items):
        # 例: ['foo', 'bar'] → 'foo(bar)'
        # items[0] = 関数名, items[1:] = 引数
        return f"{items[0]}({', '.join(map(str, items[1:]))})"


def parse_lua(lua_filepath: str) -> list:
    with open(lua_filepath, encoding="utf-8") as f:
        lua_code = f.read()

    table_texts = extract_data_extend_tables(lua_code)

    # LarkでLuaテーブルをパース（末尾カンマ許容）
    lua_table_grammar = r"""
        ?start: table
        ?table: "{" [item ("," item)* [","]] "}"
        ?item: pair | value
        pair: (NAME | ESCAPED_STRING) "=" value
        ?value: expr
        ?expr: term
             | expr OP term    -> binop
        ?term: factor
             | term OP factor  -> binop
        ?factor: concat
        ?concat: atom (".." atom)*
        ?atom: ESCAPED_STRING
                | SIGNED_NUMBER
                | table
                | FUNC_CALL
                | dotted_name
                | NAME
                | "(" expr ")"
                | "true"    -> true
                | "false"   -> false

        OP: "+" | "-" | "*" | "/"
        dotted_name: NAME ("." NAME)+
        FUNC_CALL: /[a-zA-Z_][a-zA-Z0-9_]*\([^)]*\)/
        %import common.ESCAPED_STRING
        %import common.SIGNED_NUMBER
        %import common.CNAME -> NAME
        %import common.WS
        %ignore WS
    """

    parser = Lark(lua_table_grammar, start="start")
    all_data = []
    for table_text in table_texts:
        data = LuaTableTransformer().transform(parser.parse(table_text))
        if isinstance(data, list):
            all_data.extend(data)
        else:
            all_data.append(data)
    return all_data
