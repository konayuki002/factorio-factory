from pathlib import Path

from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("allowed:mining_drill")
class MiningDrillAllowedConverter(BaseConverter):
    """Generate allowed set for MiningDrill enum."""

    dependencies = ["json:mining_drill", "enum:assembling_machine"]
    json_filename = "mining_drill.json"
    allowed_filename = "mining_drill.py"

    def load(self) -> None:
        from core.enums.assembling_machine import AssemblingMachine

        drills = self.load_json(f"{self.intermediate_dir}/{self.json_filename}")
        ret = [AssemblingMachine(d["name"]) for d in drills]

        out = [
            "from core.enums.assembling_machine import AssemblingMachine",
            "",
            "mining_drill_allowed: set[AssemblingMachine] = {",
            *[f"    {m}," for m in ret],
            "}",
        ]
        (Path(self.allowed_dir) / self.allowed_filename).write_text("\n".join(out))
