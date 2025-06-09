from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("enum:assembling_machine")
class AssemblingMachineEnumConverter(BaseConverter):
    """
    entities.json, mining_drill.json からアセンブリ機械系のEnumを生成
    - entities.json: typeが
        "assembling-machine", "lab", "furnace", "chemical-plant", "oil-refinery", "offshore-pump", "rocket-silo"
    - mining_drill.json: typeが"mining-drill"またはnameが"pumpjack"
    - ハードコード要素: "rocket-assembly-silo", "rocket-launch-silo"（仮名、後で調整可）
    """

    dependencies = ["json:entities", "json:mining_drill"]
    json_entities_filename = "entities.json"
    json_mining_drill_filename = "mining_drill.json"
    enum_path = "assembling_machine.py"
    json_filenames = ["entities.json", "mining_drill.json"]

    def load(self):
        # entities.json
        entities = self.load_json(
            f"{self.intermediate_dir}/{self.json_entities_filename}"
        )
        entity_types = [
            "assembling-machine",
            "lab",
            "furnace",
            "chemical-plant",
            "oil-refinery",
            "offshore-pump",
            "rocket-silo",
        ]
        entity_names = [e["name"] for e in entities if e.get("type") in entity_types]

        # mining_drill.json
        drills = self.load_json(
            f"{self.intermediate_dir}/{self.json_mining_drill_filename}"
        )
        drill_names = [
            d["name"]
            for d in drills
            if d.get("type") == "mining-drill" or d.get("name") == "pumpjack"
        ]

        # ハードコード要素
        manual = ["rocket-assembly-silo", "rocket-launch-silo"]

        all_names = self.merge_unique(
            entity_names, drill_names + manual, "AssemblingMachine"
        )
        self.gen_enum(
            "AssemblingMachine",
            all_names,
            f"{self.enum_dir}/{self.enum_path}",
        )
