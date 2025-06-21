from pathlib import Path

from sympy import Integer, Rational, srepr

from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("data:mining_drill")
class MiningDrillDataConverter(BaseConverter):
    """Convert mining drill JSON to data dictionaries."""

    dependencies = ["json:mining_drill", "enum:assembling_machine"]
    json_filename = "mining_drill.json"
    data_path = "mining_drill.py"

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

        drills = self.load_json(f"{self.intermediate_dir}/{self.json_filename}")

        speed: dict[AssemblingMachine, Rational] = {}
        energy: dict[AssemblingMachine, Integer] = {}
        slots: dict[AssemblingMachine, Integer] = {}

        for d in drills:
            enum = AssemblingMachine(d["name"])
            spd = Rational(float(d.get("mining_speed", 0))).limit_denominator(100)
            power = Integer(self._parse_power_kw(d.get("energy_usage", "0kW")))
            slot = Integer(d.get("module_slots", 0) or 0)
            speed[enum] = spd
            energy[enum] = power
            slots[enum] = slot

        out = [
            "from sympy import Integer, Rational",
            "from core.enums.assembling_machine import AssemblingMachine",
            "",
            "MINING_SPEED: dict[AssemblingMachine, Rational] = {",
            *[f"    {m}: {srepr(v)}," for m, v in speed.items()],
            "}",
            "",
            "ENERGY_USAGE_KW: dict[AssemblingMachine, Integer] = {",
            *[f"    {m}: {srepr(v)}," for m, v in energy.items()],
            "}",
            "",
            "MODULE_SLOTS: dict[AssemblingMachine, Integer] = {",
            *[f"    {m}: {srepr(v)}," for m, v in slots.items()],
            "}",
        ]
        (Path(self.data_dir) / self.data_path).write_text("\n".join(out))
