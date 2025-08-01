import json
import os
import shutil
from pathlib import Path

import pytest

# テストケース定義: (ConverterClass, lua_fixture, [(出力json, 期待json), ...])
TEST_CASES = [
    (
        "core.loader.converters.json.item_groups.ItemGroupJsonConverter",
        "lua-sample-item-groups.lua",
        [
            ("item_groups.json", "sample_item_groups.json"),
            ("item_subgroups.json", "sample_item_subgroups.json"),
        ],
    ),
    (
        "core.loader.converters.json.item.ItemJsonConverter",
        "lua-sample-item.lua",
        [
            ("item.json", "sample_item.json"),
        ],
    ),
    (
        "core.loader.converters.json.fluid.FluidJsonConverter",
        "lua-sample-fluid.lua",
        [
            ("fluid.json", "sample_fluid.json"),
        ],
    ),
    (
        "core.loader.converters.json.resource.ResourceJsonConverter",
        "lua-sample-resources.lua",
        [
            ("resources.json", "sample_resources.json"),
        ],
    ),
    (
        "core.loader.converters.json.resource_category.ResourceCategoryJsonConverter",
        "lua-sample-resource-category.lua",
        [
            ("resource_category.json", "sample_resource_category.json"),
        ],
    ),
    (
        "core.loader.converters.json.technology.TechnologyJsonConverter",
        "lua-sample-technology.lua",
        [
            ("technology.json", "sample_technology.json"),
        ],
    ),
    (
        "core.loader.converters.json.recipe.RecipeJsonConverter",
        "lua-sample-recipe.lua",
        [
            ("recipe.json", "sample_recipe.json"),
        ],
    ),
    (
        "core.loader.converters.json.mining_drill.MiningDrillJsonConverter",
        "lua-sample-mining-drill.lua",
        [
            ("mining_drill.json", "sample_mining_drill.json"),
        ],
    ),
    (
        "core.loader.converters.json.entities.EntitiesJsonConverter",
        "lua-sample-entities.lua",
        [
            ("entities.json", "sample_entities.json"),
        ],
    ),
    (
        "core.loader.converters.json.recipe_category.RecipeCategoryJsonConverter",
        "lua-sample-recipe-category.lua",
        [
            ("recipe_category.json", "sample_recipe_category.json"),
        ],
    ),
    # 他のConverterも追加
]


@pytest.mark.parametrize("converter_path,lua_fixture,outputs", TEST_CASES)
def test_json_converter(
    tmp_path: Path,
    converter_path: str,
    lua_fixture: str,
    outputs: list[tuple[str, str]],
) -> None:
    # Converterクラスをimport
    module_path, class_name = converter_path.rsplit(".", 1)
    ConverterClass = getattr(__import__(module_path, fromlist=[class_name]), class_name)

    # 入出力ディレクトリ準備
    input_base = tmp_path / "input"
    output_base = tmp_path / "output"
    input_base.mkdir()
    output_base.mkdir()
    fixtures_dir = os.path.join(os.path.dirname(__file__), "fixtures")

    # Luaファイルをコピー
    shutil.copyfile(
        os.path.join(fixtures_dir, lua_fixture),
        input_base / ConverterClass.lua_filename,  # Converterが期待するLuaファイル名
    )

    # Converterインスタンス生成
    converter = ConverterClass()
    converter.raw_dir = str(input_base)
    converter.intermediate_dir = str(output_base)

    # 変換実行
    converter.load()

    # 各出力JSONについて比較
    for out_json, expected_json in outputs:
        out_json_path = os.path.join(converter.intermediate_dir, out_json)
        assert os.path.isfile(out_json_path), f"{out_json_path} が生成されていません"
        with open(out_json_path, encoding="utf-8") as f:
            actual = json.load(f)
        expected_json_path = os.path.join(fixtures_dir, f"json/{expected_json}")
        with open(expected_json_path, encoding="utf-8") as f:
            expected = json.load(f)
        # 順序非依存で比較
        assert sorted(actual, key=lambda x: x.get("name", "")) == sorted(
            expected, key=lambda x: x.get("name", "")
        )
