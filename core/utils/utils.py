from enum import Enum

from sympy import Integer, Rational


def to_enum_member(name: str) -> str:
    """
    kebab-case → SNAKE_CASE → UPPER_CAMEL_CASE
    例: "iron-plate" → "IronPlate"
    """
    return "".join(word.capitalize() for word in name.split("-"))


def parse_power_kw(value: str) -> Rational:
    if value.endswith("kW"):
        return Rational(float(value[:-2])).limit_denominator(10)
    if value.endswith("MW"):
        return Rational(float(value[:-2])).limit_denominator(10) * Integer(1000)
    if value.endswith("GW"):
        return Rational(float(value[:-2])).limit_denominator(10) * Integer(1000000)
    raise ValueError(f"Unknown power unit in {value}")


def repr_set_of_enum(enum_set: set[Enum]) -> str:
    """
    set[Enum] → repr
    例: {AssemblingMachine.assembling_machine_1, AssemblingMachine.assembling_machine_2} → "{AssemblingMachine.assembling_machine_1, AssemblingMachine.assembling_machine_2}"
    """
    if not enum_set:
        return "set()"
    sorted_enums = sorted(enum_set, key=lambda e: e.name)
    return (
        "{" + ", ".join(f"{e.__class__.__name__}.{e.name}" for e in sorted_enums) + "}"
    )


def repr_set_of_str(str_set: set[str]) -> str:
    """
    set[str] → repr
    例: {"iron-plate", "copper-plate"} → "{'iron-plate', 'copper-plate'}"
    """
    if not str_set:
        return "set()"
    sorted_strings = sorted(str_set)
    return "{" + ", ".join(f"'{s}'" for s in sorted_strings) + "}"
