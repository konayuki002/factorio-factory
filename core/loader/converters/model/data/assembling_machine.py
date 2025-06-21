from pathlib import Path

from sympy import Integer, Rational, srepr

from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("data:assembling_machine")
class AssemblingMachineDataConverter(BaseConverter):
    """Convert assembling machine related JSON to data dictionaries."""

    dependencies = ["json:entities", "json:mining_drill", "enum:assembling_machine"]
    json_entities_filename = "entities.json"
    json_mining_drill_filename = "mining_drill.json"
    data_path = "assembling_machine.py"
    json_filenames = ["entities.json", "mining_drill.json"]

    def _parse_power_kw(self, value: str) -> int:
        if value.endswith("kW"):
            return int(float(value[:-2]))
        if value.endswith("MW"):
            return int(float(value[:-2]) * 1000)
        if value.endswith("W"):
            return int(float(value[:-1]) / 1000)
        raise ValueError(f"Unknown power unit in {value}")

    def load(self) -> None:
        from core.enums.assembling_machine import AssemblingMachine

        entities = self.load_json(
            f"{self.intermediate_dir}/{self.json_entities_filename}"
        )
        drills = self.load_json(
            f"{self.intermediate_dir}/{self.json_mining_drill_filename}"
        )

        records: dict[str, tuple[float, int, int]] = {}
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
                name = e["name"]
                speed = float(e.get("crafting_speed", 0))
                energy = e.get("energy_usage", "0kW")
                slots = e.get("module_slots", 0) or 0
                records[name] = (speed, self._parse_power_kw(energy), int(slots))

        for d in drills:
            name = d["name"]
            speed = float(d.get("mining_speed", 0))
            energy = d.get("energy_usage", "0kW")
            slots = d.get("module_slots", 0) or 0
            records[name] = (speed, self._parse_power_kw(energy), int(slots))

        crafting_speed: dict[AssemblingMachine, Rational] = {}
        energy_usage: dict[AssemblingMachine, Integer] = {}
        module_slots: dict[AssemblingMachine, Integer] = {}

        for name, (speed, energy_kw, slots) in records.items():
            enum = AssemblingMachine(name)
            crafting_speed[enum] = Rational(speed).limit_denominator(100)
            energy_usage[enum] = Integer(energy_kw)
            module_slots[enum] = Integer(slots)

        out = [
            "from sympy import Integer, Rational",
            "from core.enums.assembling_machine import AssemblingMachine",
            "",
            "CRAFTING_SPEED: dict[AssemblingMachine, Rational] = {",
            *[f"    {m}: {srepr(speed)}," for m, speed in crafting_speed.items()],
            "}",
            "",
            "ENERGY_USAGE_KW: dict[AssemblingMachine, Integer] = {",
            *[f"    {m}: {srepr(power)}," for m, power in energy_usage.items()],
            "}",
            "",
            "MODULE_SLOTS: dict[AssemblingMachine, Integer] = {",
            *[f"    {m}: {srepr(slots)}," for m, slots in module_slots.items()],
            "}",
        ]
        (Path(self.data_dir) / self.data_path).write_text("\n".join(out))
