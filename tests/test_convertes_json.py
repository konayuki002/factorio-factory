import os
import shutil
import json
import pytest
from core.loader.converters.json.item_groups import ItemGroupJsonConverter


@pytest.fixture
def json_converter(tmp_path):
    """
    - tmp_path/input に tests/fixtures/lua-sample-item-groups.lua を 'item-groups.lua' という名前でコピー
    - tmp_path/output に空ディレクトリを作成
    - ItemGroupJsonConverter のインスタンスを返す
    """
    input_base = tmp_path / "input"
    output_base = tmp_path / "output"
    input_base.mkdir()
    output_base.mkdir()
    fixtures_dir = os.path.join(os.path.dirname(__file__), "fixtures")

    # テスト用 Lua スニペットをコピーし、Converter が期待するファイル名にリネーム
    shutil.copyfile(
        os.path.join(fixtures_dir, "lua-sample-item-groups.lua"),
        input_base
        / "item-groups.lua",  # Converter が 'item_groups.lua' を読みに行く想定
    )

    converter = ItemGroupJsonConverter()
    converter.raw_dir = str(input_base)
    converter.intermediate_dir = str(output_base)
    return converter


def test_item_groups_json_generation(json_converter):
    """
    - json_converter.load() で JSON が出力される（item-groups.json）
    - 生成された JSON をロードして内容を比較
    """
    converter = json_converter

    # 変換を実行
    converter.load()

    # item_groups
    out_json_item_groups_path = os.path.join(
        converter.intermediate_dir, "item_groups.json"
    )
    assert os.path.isfile(
        out_json_item_groups_path
    ), f"JSON ファイルが生成されていません: {out_json_item_groups_path}"

    # 中身をロードして期待値と比較
    with open(out_json_item_groups_path, "r", encoding="utf-8") as f:
        item_groups_data = json.load(f)

    # 期待されるデータを fixtures からロード
    target_json_item_groups_path = os.path.join(
        os.path.dirname(__file__), "fixtures", "json_sample_item_groups.json"
    )
    with open(target_json_item_groups_path, encoding="utf-8") as f:
        expected_item_groups_data = json.load(f)

    assert len(item_groups_data) == len(expected_item_groups_data)
    # 順序は保証されないので、名前でソートして比較
    assert sorted(item_groups_data, key=lambda x: x["name"]) == sorted(
        expected_item_groups_data, key=lambda x: x["name"]
    )

    # item_subgroups
    out_json_item_subgroups_path = os.path.join(
        converter.intermediate_dir, "item_subgroups.json"
    )
    assert os.path.isfile(
        out_json_item_subgroups_path
    ), f"JSON ファイルが生成されていません: {out_json_item_subgroups_path}"
    # 中身をロードして期待値と比較
    with open(out_json_item_subgroups_path, "r", encoding="utf-8") as f:
        item_subgroups_data = json.load(f)
    # 期待されるデータを fixtures からロード
    target_json_item_subgroups_path = os.path.join(
        os.path.dirname(__file__), "fixtures", "json_sample_item_subgroups.json"
    )
    with open(target_json_item_subgroups_path, encoding="utf-8") as f:
        expected_item_subgroups_data = json.load(f)
    assert len(item_subgroups_data) == len(expected_item_subgroups_data)
    # 順序は保証されないので、名前でソートして比較
    assert sorted(item_subgroups_data, key=lambda x: x["name"]) == sorted(
        expected_item_subgroups_data, key=lambda x: x["name"]
    )
