#!/usr/bin/env python3
import json
from typing import Any, Dict

# prototypes.jsonからfluidデータを直接確認
with open("data/intermediate/prototypes.json", "r") as f:
    all_prototypes = json.load(f)

fluid_prototypes = all_prototypes.get("fluid", {})
print(f"Found {len(fluid_prototypes)} fluid prototypes in prototypes.json")

print("\nFluid prototypes analysis:")
for name, fluid in fluid_prototypes.items():
    has_subgroup = "subgroup" in fluid
    print(f"  {name}: has_subgroup={has_subgroup}")
    if not has_subgroup:
        print(f"    Missing subgroup: {fluid}")

# fluid-unknownの具体的な内容を確認
if "fluid-unknown" in fluid_prototypes:
    print(f"\nfluid-unknown details:")
    print(fluid_prototypes["fluid-unknown"])
else:
    print("\nfluid-unknown not found in prototypes.json")
