#!/usr/bin/env python3
import json
import os
from typing import Any, Dict, List

# 新方式の結果を確認
with open("data/intermediate/recipe.json", "r") as f:
    new_recipes = json.load(f)

print(f"新方式（Lua実行）のrecipe件数: {len(new_recipes)}")

# 最初のレシピ名を確認
if new_recipes:
    print(f'最初のレシピ: {new_recipes[0].get("name", "不明")}')
    print(f"最初のレシピの構造: {list(new_recipes[0].keys())}")

# prototypes.jsonから直接recipe件数を確認
with open("data/intermediate/prototypes.json", "r") as f:
    all_prototypes = json.load(f)

if "recipe" in all_prototypes:
    print(f'prototypes.jsonのrecipe件数: {len(all_prototypes["recipe"])}')

print(f"prototypes.jsonのプロトタイプタイプ数: {len(all_prototypes.keys())}")
print("主要なプロトタイプタイプ:")
for ptype in sorted(all_prototypes.keys())[:10]:
    count = len(all_prototypes[ptype])
    print(f"  {ptype}: {count} items")
