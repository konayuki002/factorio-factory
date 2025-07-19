#!/usr/bin/env python3
import json
from typing import Any, Dict, List

# fluid.jsonの構造を確認
with open("data/intermediate/fluid.json", "r") as f:
    fluids = json.load(f)

print(f"Found {len(fluids)} fluids")
if fluids:
    print("First fluid:")
    fluid = fluids[0]
    print(f"  Name: {fluid.get('name')}")
    print(f"  Keys: {list(fluid.keys())}")
    print(f"  Full content: {fluid}")

    # subgroupフィールドの有無を確認
    has_subgroup = "subgroup" in fluid
    print(f"  Has subgroup: {has_subgroup}")
    if not has_subgroup:
        print("  ❌ subgroup field is missing!")

    # 他のfluidsも確認
    print(f"\nAll fluids subgroup status:")
    for i, fluid in enumerate(fluids):
        has_subgroup = "subgroup" in fluid
        print(f"  {fluid.get('name', f'fluid_{i}')}: has_subgroup={has_subgroup}")
