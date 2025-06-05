import os
import shutil
import importlib.util
import pytest
from enum import Enum
from core.loader.converters.enum.item_groups import ItemGroupEnumConverter


@pytest.fixture
def enum_converter(tmp_path):
    """
    - tmp_path/input に tests/fixtures/{json_sample_item_groups.json, json_sample_item_subgroups.json}
      を 'item_groups.json', 'item_subgroups.json' という名前でコピー
    - tmp_path/output に空ディレクトリを作成
    - ItemGroupEnumConverter のインスタンスを返す
    """
    input_base = tmp_path / "input"
    output_base = tmp_path / "output"
    input_base.mkdir()
    output_base.mkdir()
    fixtures_dir = os.path.join(os.path.dirname(__file__), "fixtures")

    # テスト用 JSON スニペットをコピーし、Converter が期待するファイル名にリネーム
    shutil.copyfile(
        os.path.join(fixtures_dir, "json_sample_item_groups.json"),
        input_base
        / "item_groups.json",  # Converter が 'item_groups.json' を読みに行く想定
    )
    shutil.copyfile(
        os.path.join(fixtures_dir, "json_sample_item_subgroups.json"),
        input_base
        / "item_subgroups.json",  # Converter が 'item_subgroups.json' を読みに行く想定
    )

    converter = ItemGroupEnumConverter()
    converter.intermediate_dir = str(input_base)
    converter.enum_dir = str(output_base)
    return converter


def _import_enum(path: str, class_name: str) -> type[Enum]:
    spec = importlib.util.spec_from_file_location(class_name, path)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return getattr(module, class_name)


def _assert_enum_equal(enum1: type[Enum], enum2: type[Enum]) -> None:
    """Enumクラス同士のメンバー名・値を比較"""
    assert len(enum1) == len(
        enum2
    ), f"Enum length mismatch: {len(enum1)} vs {len(enum2)}"
    assert sorted(enum1.__members__.keys()) == sorted(
        enum2.__members__.keys()
    ), f"Enum keys differ: {enum1.__members__.keys()} vs {enum2.__members__.keys()}"
    assert sorted({m.value for m in enum1}) == sorted(
        {m.value for m in enum2}
    ), f"Enum values differ: {[m.value for m in enum1]} vs {[m.value for m in enum2]}"


def test_item_groups_enum_generation(enum_converter):
    """
    - enum_converter.load() で Enum が出力される（item_group.py, item_subgroup.py）
    - 生成された Enum を fixtures の期待値と比較
    """
    converter = enum_converter
    converter.load()

    # ItemGroup Enum の比較
    out_enum_item_groups_path = os.path.join(converter.enum_dir, "item_group.py")
    assert os.path.isfile(
        out_enum_item_groups_path
    ), f"Enum モジュールのファイルが生成されていません: {out_enum_item_groups_path}"

    # 中身をロードして期待値と比較
    ItemGroup = _import_enum(out_enum_item_groups_path, "ItemGroup")
    target_enum_item_groups_path = os.path.join(
        os.path.dirname(__file__), "fixtures", "enum_sample_item_group.py"
    )
    TargetItemGroup = _import_enum(target_enum_item_groups_path, "ItemGroup")
    _assert_enum_equal(ItemGroup, TargetItemGroup)

    # ItemSubGroup Enum の比較
    out_enum_item_subgroups_path = os.path.join(converter.enum_dir, "item_subgroup.py")
    assert os.path.isfile(
        out_enum_item_subgroups_path
    ), f"Enum モジュールのファイルが生成されていません: {out_enum_item_subgroups_path}"

    # 中身をロードして期待値と比較
    ItemSubgroup = _import_enum(out_enum_item_subgroups_path, "ItemSubgroup")
    target_enum_item_subgroups_path = os.path.join(
        os.path.dirname(__file__), "fixtures", "enum_sample_item_subgroup.py"
    )
    TargetItemSubgroup = _import_enum(target_enum_item_subgroups_path, "ItemSubgroup")
    _assert_enum_equal(ItemSubgroup, TargetItemSubgroup)
