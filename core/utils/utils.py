def to_enum_member(name: str) -> str:
    """
    kebab-case → SNAKE_CASE → UPPER_CAMEL_CASE
    例: "iron-plate" → "IronPlate"
    """
    return "".join(word.capitalize() for word in name.split("-"))
