#!/usr/bin/env python3
import json
from typing import Any, Dict, List

# entities.jsonの内容を分析
with open("data/intermediate/entities.json", "r") as f:
    entities = json.load(f)

print("=== assembling-machine entities analysis ===")
assembling_machines = [e for e in entities if e.get("type") == "assembling-machine"]
print(f"Found {len(assembling_machines)} assembling machines")

if assembling_machines:
    machine = assembling_machines[0]
    print(f"\nFirst machine: {machine.get('name')}")
    print(f"crafting_categories: {machine.get('crafting_categories')}")
    print(f"crafting_categories type: {type(machine.get('crafting_categories'))}")

    if machine.get("crafting_categories"):
        categories = machine.get("crafting_categories")
        if isinstance(categories, dict):
            print("crafting_categories is a dict:")
            for key, value in categories.items():
                print(f"  {key}: {value} (type: {type(value)})")
        elif isinstance(categories, list):
            print("crafting_categories is a list:")
            for i, cat in enumerate(categories):
                print(f"  {i}: {cat} (type: {type(cat)})")

# recipe_category.jsonも確認
print("\n=== recipe_category.json analysis ===")
with open("data/intermediate/recipe_category.json", "r") as f:
    categories = json.load(f)

print(f"Found {len(categories)} recipe categories")
if categories:
    print("First few categories:")
    for i, cat in enumerate(categories[:3]):
        print(f"  {cat.get('name')}: {cat}")
