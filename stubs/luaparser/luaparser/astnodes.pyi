from _typeshed import Incomplete
from antlr4.Token import CommonToken
from enum import Enum

Comments: Incomplete

class Node:
    comments: Comments
    def __init__(self, name: str, comments: Comments = None, first_token: CommonToken | None = None, last_token: CommonToken | None = None) -> None: ...
    @property
    def display_name(self) -> str: ...
    def __eq__(self, other) -> bool: ...
    @property
    def first_token(self) -> CommonToken | None: ...
    @first_token.setter
    def first_token(self, val: CommonToken | None): ...
    @property
    def last_token(self) -> CommonToken | None: ...
    @last_token.setter
    def last_token(self, val: CommonToken | None): ...
    @property
    def start_char(self) -> int | None: ...
    @property
    def stop_char(self) -> int | None: ...
    @property
    def line(self) -> int | None: ...
    def to_json(self) -> any: ...

class Comment(Node):
    s: str
    is_multi_line: bool
    def __init__(self, s: str, is_multi_line: bool = False, **kwargs) -> None: ...

class Expression(Node):
    wrapped: Incomplete
    def __init__(self, name: str, wrapped: bool = False, **kwargs) -> None: ...

class Statement(Expression): ...

class Block(Node):
    body: list[Statement]
    def __init__(self, body: list[Statement], **kwargs) -> None: ...

class Chunk(Node):
    body: Incomplete
    def __init__(self, body: Block, **kwargs) -> None: ...

class Lhs(Expression): ...

class Attribute(Node):
    name: Name
    def __init__(self, name: Name, **kwargs) -> None: ...

class Name(Lhs):
    id: str
    attribute: Attribute | None
    def __init__(self, identifier: str, attribute: Attribute | None = None, **kwargs) -> None: ...

class IndexNotation(Enum):
    DOT = 0
    SQUARE = 1

class Index(Lhs):
    idx: Expression
    value: Expression
    notation: IndexNotation
    def __init__(self, idx: Expression, value: Expression, notation: IndexNotation = ..., **kwargs) -> None: ...

class Assign(Statement):
    targets: list[Node]
    values: list[Node]
    def __init__(self, targets: list[Node], values: list[Node], **kwargs) -> None: ...

class LocalAssign(Assign):
    def __init__(self, targets: list[Name], values: list[Node], **kwargs) -> None: ...

class While(Statement):
    test: Expression
    body: Block
    def __init__(self, test: Expression, body: Block, **kwargs) -> None: ...

class Do(Statement):
    body: Block
    def __init__(self, body: Block, **kwargs) -> None: ...

class Repeat(Statement):
    body: Block
    test: Expression
    def __init__(self, body: Block, test: Expression, **kwargs) -> None: ...

class ElseIf(Statement):
    test: Node
    body: Block
    orelse: Incomplete
    def __init__(self, test: Node, body: Block, orelse, **kwargs) -> None: ...

class If(Statement):
    test: Expression
    body: Block
    orelse: Incomplete
    def __init__(self, test: Expression, body: Block, orelse: None, **kwargs) -> None: ...

class Label(Statement):
    id: Name
    def __init__(self, label_id: Name, **kwargs) -> None: ...

class Goto(Statement):
    label: Name
    def __init__(self, label: Name, **kwargs) -> None: ...

class SemiColon(Statement):
    def __init__(self, **kwargs) -> None: ...

class Break(Statement):
    def __init__(self, **kwargs) -> None: ...

class Continue(Statement):
    def __init__(self, **kwargs) -> None: ...

class Return(Statement):
    values: Incomplete
    def __init__(self, values, **kwargs) -> None: ...

class Fornum(Statement):
    target: Name
    start: Expression
    stop: Expression
    step: Expression
    body: Block
    def __init__(self, target: Name, start: Expression, stop: Expression, step: Expression, body: Block, **kwargs) -> None: ...

class Forin(Statement):
    body: Block
    iter: list[Expression]
    targets: list[Name]
    def __init__(self, body: Block, iter: list[Expression], targets: list[Name], **kwargs) -> None: ...

class CallStyle(Enum):
    DEFAULT = 0
    NO_PARENTHESIS = 1

class Call(Statement):
    func: Expression
    args: list[Expression]
    style: CallStyle
    def __init__(self, func: Expression, args: list[Expression], style: CallStyle = ..., **kwargs) -> None: ...

class Invoke(Statement):
    source: Expression
    func: Expression
    args: list[Expression]
    style: CallStyle
    def __init__(self, source: Expression, func: Expression, args: list[Expression], style: CallStyle = ..., **kwargs) -> None: ...

class Function(Statement):
    name: Expression
    args: list[Expression]
    body: Block
    def __init__(self, name: Expression, args: list[Expression], body: Block, **kwargs) -> None: ...

class LocalFunction(Statement):
    name: Expression
    args: list[Expression]
    body: Block
    def __init__(self, name: Expression, args: list[Expression], body: Block, **kwargs) -> None: ...

class Method(Statement):
    source: Expression
    name: Expression
    args: list[Expression]
    body: Block
    def __init__(self, source: Expression, name: Expression, args: list[Expression], body: Block, **kwargs) -> None: ...

class Nil(Expression):
    def __init__(self, **kwargs) -> None: ...

class TrueExpr(Expression):
    def __init__(self, **kwargs) -> None: ...

class FalseExpr(Expression):
    def __init__(self, **kwargs) -> None: ...

NumberType: Incomplete

class Number(Expression):
    n: NumberType
    def __init__(self, n: NumberType, **kwargs) -> None: ...

class Varargs(Expression):
    def __init__(self, **kwargs) -> None: ...

class StringDelimiter(Enum):
    SINGLE_QUOTE = 0
    DOUBLE_QUOTE = 1
    DOUBLE_SQUARE = 2

class String(Expression):
    s: str
    delimiter: StringDelimiter
    def __init__(self, s: str, delimiter: StringDelimiter = ..., **kwargs) -> None: ...

class Field(Expression):
    key: Expression
    value: Expression
    between_brackets: bool
    def __init__(self, key: Expression, value: Expression, between_brackets: bool = False, **kwargs) -> None: ...

class Table(Expression):
    fields: list[Field]
    def __init__(self, fields: list[Field], **kwargs) -> None: ...

class Dots(Expression):
    def __init__(self, **kwargs) -> None: ...

class AnonymousFunction(Expression):
    args: list[Expression]
    body: Block
    def __init__(self, args: list[Expression], body: Block, **kwargs) -> None: ...

class Op(Expression): ...

class BinaryOp(Op):
    left: Expression
    right: Expression
    def __init__(self, name, left: Expression, right: Expression, **kwargs) -> None: ...

class AriOp(BinaryOp): ...

class AddOp(AriOp):
    def __init__(self, left: Expression, right: Expression, **kwargs) -> None: ...

class SubOp(AriOp):
    def __init__(self, left: Expression, right: Expression, **kwargs) -> None: ...

class MultOp(AriOp):
    def __init__(self, left: Expression, right: Expression, **kwargs) -> None: ...

class FloatDivOp(AriOp):
    def __init__(self, left: Expression, right: Expression, **kwargs) -> None: ...

class FloorDivOp(AriOp):
    def __init__(self, left: Expression, right: Expression, **kwargs) -> None: ...

class ModOp(AriOp):
    def __init__(self, left: Expression, right: Expression, **kwargs) -> None: ...

class ExpoOp(AriOp):
    def __init__(self, left: Expression, right: Expression, **kwargs) -> None: ...

class BitOp(BinaryOp): ...

class BAndOp(BitOp):
    def __init__(self, left: Expression, right: Expression, **kwargs) -> None: ...

class BOrOp(BitOp):
    def __init__(self, left: Expression, right: Expression, **kwargs) -> None: ...

class BXorOp(BitOp):
    def __init__(self, left: Expression, right: Expression, **kwargs) -> None: ...

class BShiftROp(BitOp):
    def __init__(self, left: Expression, right: Expression, **kwargs) -> None: ...

class BShiftLOp(BitOp):
    def __init__(self, left: Expression, right: Expression, **kwargs) -> None: ...

class RelOp(BinaryOp): ...

class LessThanOp(RelOp):
    def __init__(self, left: Expression, right: Expression, **kwargs) -> None: ...

class GreaterThanOp(RelOp):
    def __init__(self, left: Expression, right: Expression, **kwargs) -> None: ...

class LessOrEqThanOp(RelOp):
    def __init__(self, left: Expression, right: Expression, **kwargs) -> None: ...

class GreaterOrEqThanOp(RelOp):
    def __init__(self, left: Expression, right: Expression, **kwargs) -> None: ...

class EqToOp(RelOp):
    def __init__(self, left: Expression, right: Expression, **kwargs) -> None: ...

class NotEqToOp(RelOp):
    def __init__(self, left: Expression, right: Expression, **kwargs) -> None: ...

class LoOp(BinaryOp): ...

class AndLoOp(LoOp):
    def __init__(self, left: Expression, right: Expression, **kwargs) -> None: ...

class OrLoOp(LoOp):
    def __init__(self, left: Expression, right: Expression, **kwargs) -> None: ...

class Concat(BinaryOp):
    def __init__(self, left: Expression, right: Expression, **kwargs) -> None: ...

class UnaryOp(Expression):
    operand: Incomplete
    def __init__(self, name: str, operand: Expression, **kwargs) -> None: ...

class UMinusOp(UnaryOp):
    def __init__(self, operand: Expression, **kwargs) -> None: ...

class UBNotOp(UnaryOp):
    def __init__(self, operand: Expression, **kwargs) -> None: ...

class ULNotOp(UnaryOp):
    def __init__(self, operand: Expression, **kwargs) -> None: ...

class ULengthOP(UnaryOp):
    def __init__(self, operand: Expression, **kwargs) -> None: ...
