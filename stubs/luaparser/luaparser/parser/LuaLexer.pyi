from antlr4 import *
from LuaLexerBase import LuaLexerBase as LuaLexerBase
from _typeshed import Incomplete
from io import StringIO as StringIO
from typing import TextIO

def serializedATN(): ...

class LuaLexer(LuaLexerBase):
    atn: Incomplete
    decisionsToDFA: Incomplete
    SEMI: int
    EQ: int
    BREAK: int
    GOTO: int
    DO: int
    END: int
    WHILE: int
    REPEAT: int
    UNTIL: int
    IF: int
    THEN: int
    ELSEIF: int
    ELSE: int
    FOR: int
    COMMA: int
    IN: int
    FUNCTION: int
    LOCAL: int
    LT: int
    GT: int
    RETURN: int
    CONTINUE: int
    CC: int
    NIL: int
    FALSE: int
    TRUE: int
    DOT: int
    SQUIG: int
    MINUS: int
    POUND: int
    OP: int
    CP: int
    NOT: int
    LL: int
    GG: int
    AMP: int
    SS: int
    PER: int
    COL: int
    LE: int
    GE: int
    AND: int
    OR: int
    PLUS: int
    STAR: int
    OCU: int
    CCU: int
    OB: int
    CB: int
    EE: int
    DD: int
    PIPE: int
    CARET: int
    SLASH: int
    DDD: int
    SQEQ: int
    NAME: int
    NORMALSTRING: int
    CHARSTRING: int
    LONGSTRING: int
    INT: int
    HEX: int
    FLOAT: int
    HEX_FLOAT: int
    COMMENT: int
    LINE_COMMENT: int
    WS: int
    NL: int
    SHEBANG: int
    channelNames: Incomplete
    modeNames: Incomplete
    literalNames: Incomplete
    symbolicNames: Incomplete
    ruleNames: Incomplete
    grammarFileName: str
    def __init__(self, input: Incomplete | None = None, output: TextIO = ...) -> None: ...
    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int): ...
    def SHEBANG_sempred(self, localctx: RuleContext, predIndex: int): ...
