#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

# 更新されたentities.jsonを確認
entities_path = Path("data/intermediate/entities.json")
if not entities_path.exists():
    print("entities.json not found")
    sys.exit(1)

with open(entities_path, "r") as f:
    entities = json.load(f)

print("=== Updated assembling-machine analysis ===")
assembling_machines = [e for e in entities if e.get("type") == "assembling-machine"]
print(f"Found {len(assembling_machines)} assembling machines")

if assembling_machines:
    machine = assembling_machines[0]
    print(f"\nFirst machine: {machine.get('name')}")
    categories = machine.get("crafting_categories")
    print(f"crafting_categories: {categories}")
    print(f"crafting_categories type: {type(categories)}")

    if isinstance(categories, list):
        print("✅ crafting_categories is now a list (正規化成功)")
        for i, cat in enumerate(categories):
            print(f"  {i}: {cat}")
    elif isinstance(categories, dict):
        print("❌ crafting_categories is still a dict (正規化失敗)")
        for key, value in categories.items():
            print(f"  {key}: {value}")
    else:
        print(f"❓ unexpected type: {type(categories)}")

# その他のフィールドも確認
if assembling_machines:
    machine = assembling_machines[0]
    print(f"\nOther fields check:")
    allowed_effects = machine.get("allowed_effects")
    print(f"allowed_effects: {allowed_effects} (type: {type(allowed_effects)})")
