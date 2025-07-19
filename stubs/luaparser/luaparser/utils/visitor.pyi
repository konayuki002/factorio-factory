from _typeshed import Incomplete

class VisitorException(Exception):
    message: Incomplete
    def __init__(self, message) -> None: ...

def visitor(arg_type): ...
