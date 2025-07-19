from enum import Enum
from pathlib import Path
from typing import cast

from sympy import Rational, srepr

from core.loader.converters.base import BaseConverter
from core.loader.registry import register
from core.utils.utils import parse_power_kw, repr_set_of_enum, repr_set_of_str


@register("data:assembling_machine")
class AssemblingMachineDataConverter(BaseConverter):
    """Convert assembling machine related JSON to data dictionaries."""

    dependencies = ["json:entities", "json:mining_drill", "enum:assembling_machine"]
    json_entities_filename = "entities.json"
    json_mining_drill_filename = "mining_drill.json"
    data_path = "assembling_machine.py"
    json_filenames = ["entities.json", "mining_drill.json"]

    def load(self) -> None:
        from core.enums.assembling_machine import AssemblingMachine
        from core.enums.operation_category import OperationCategory

        entities = self.load_json(
            f"{self.intermediate_dir}/{self.json_entities_filename}"
        )
        drills = self.load_json(
            f"{self.intermediate_dir}/{self.json_mining_drill_filename}"
        )

        types: dict[AssemblingMachine, str] = {}
        speeds: dict[AssemblingMachine, Rational] = {}
        categories: dict[AssemblingMachine, set[OperationCategory]] = {}
        energy_usages_kw: dict[AssemblingMachine, Rational] = {}
        allowed_effects: dict[AssemblingMachine, set[str]] = {}
        module_slots: dict[AssemblingMachine, int] = {}
        for e in entities:
            if e.get("type") in {
                "assembling-machine",
                "lab",
                "furnace",
                "chemical-plant",
                "oil-refinery",
                "offshore-pump",
                "rocket-silo",
                "centrifuge",
            }:
                enum = AssemblingMachine(e["name"])
                types[enum] = e.get("type", "")
                speeds[enum] = Rational(
                    float(e.get("crafting_speed", 0))
                ).limit_denominator(4)
                categories[enum] = {
                    OperationCategory(category)
                    for category in e.get("crafting_categories", [])
                }
                energy_usages_kw[enum] = parse_power_kw(e.get("energy_usage", "0kW"))
                allowed_effects[enum] = set(e.get("allowed_effects", []))
                module_slots[enum] = e.get("module_slots", 0) or 0

        for d in drills:
            enum = AssemblingMachine(d["name"])
            types[enum] = "mining-drill"
            speeds[enum] = Rational(float(d.get("mining_speed", 0))).limit_denominator(
                4
            )
            categories[enum] = {OperationCategory.Mining}
            energy_usages_kw[enum] = parse_power_kw(d.get("energy_usage", "0kW"))
            if enum == AssemblingMachine.Pumpjack:
                # Pumpjack has no allowed effects
                allowed_effects[enum] = {
                    "consumption",
                    "speed",
                    "productivity",
                    "pollution",
                }
            else:
                allowed_effects[enum] = set(
                    d.get(
                        "allowed_effects",
                        [
                            "consumption",
                            "speed",
                            "productivity",
                            "pollution",
                            "quality",
                        ],
                    )
                )
            module_slots[enum] = d.get("module_slots", 0) or 0

        out = [
            "from sympy import Integer, Rational",
            "from core.enums.assembling_machine import AssemblingMachine",
            "from core.enums.operation_category import OperationCategory",
            "",
            "TYPES: dict[AssemblingMachine, str] = {",
            *[
                f'    {m}: "{t}",'
                for m, t in sorted(types.items(), key=lambda x: str(x[0]))
            ],
            "}",
            "",
            "SPEED: dict[AssemblingMachine, Rational] = {",
            *[
                f"    {m}: {srepr(speed)},"
                for m, speed in sorted(speeds.items(), key=lambda x: str(x[0]))
            ],
            "}",
            "",
            "CATEGORIES: dict[AssemblingMachine, set[OperationCategory]] = {",
            *[
                f"    {m}: {repr_set_of_enum(cast(set[Enum], c))},"
                for m, c in sorted(categories.items(), key=lambda x: str(x[0]))
            ],
            "}",
            "",
            "ENERGY_USAGE_KW: dict[AssemblingMachine, Rational] = {",
            *[
                f"    {m}: {srepr(e)},"
                for m, e in sorted(energy_usages_kw.items(), key=lambda x: str(x[0]))
            ],
            "}",
            "",
            "ALLOWED_EFFECTS: dict[AssemblingMachine, set[str]] = {",
            *[
                f"    {m}: {repr_set_of_str(effects)},"
                for m, effects in sorted(
                    allowed_effects.items(), key=lambda x: str(x[0])
                )
            ],
            "}",
            "",
            "MODULE_SLOTS: dict[AssemblingMachine, int] = {",
            *[
                f"    {m}: {srepr(slots)},"
                for m, slots in sorted(module_slots.items(), key=lambda x: str(x[0]))
            ],
            "}",
        ]
        (Path(self.data_dir) / self.data_path).write_text("\n".join(out))
