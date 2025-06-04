import os
import shutil
import importlib.util
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest
from core.loader.converters.enum.item_groups import ItemGroupEnumConverter


@pytest.fixture
def enum_converter(tmp_path):
    intermediate = tmp_path / "intermediate"
    enum_out = tmp_path / "enum"
    intermediate.mkdir()
    enum_out.mkdir()
    fixtures_dir = os.path.join(os.path.dirname(__file__), "fixtures")

    shutil.copyfile(
        os.path.join(fixtures_dir, "json_sample_item_groups.json"),
        intermediate / "item_groups.json",
    )
    shutil.copyfile(
        os.path.join(fixtures_dir, "json_sample_item_subgroups.json"),
        intermediate / "item_subgroups.json",
    )

    converter = ItemGroupEnumConverter()
    converter.intermediate_dir = str(intermediate)
    converter.enum_dir = str(enum_out)
    return converter


def _import_enum(path: str, class_name: str):
    spec = importlib.util.spec_from_file_location(class_name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return getattr(module, class_name)


def test_item_groups_enum_generation(enum_converter):
    converter = enum_converter

    converter.load()

    fixtures_dir = os.path.join(os.path.dirname(__file__), "fixtures")

    item_group_path = os.path.join(converter.enum_dir, "item_group.py")
    expected_item_group = os.path.join(fixtures_dir, "enum_expected_item_group.py")
    assert os.path.isfile(item_group_path)
    with open(item_group_path) as gen, open(expected_item_group) as exp:
        assert gen.read() == exp.read()

    ItemGroup = _import_enum(item_group_path, "ItemGroup")
    assert {m.value for m in ItemGroup} == {
        "group1",
        "group2",
        "unmined-resource",
        "technology",
    }

    item_subgroup_path = os.path.join(converter.enum_dir, "item_subgroup.py")
    expected_item_subgroup = os.path.join(fixtures_dir, "enum_expected_item_subgroup.py")
    assert os.path.isfile(item_subgroup_path)
    with open(item_subgroup_path) as gen, open(expected_item_subgroup) as exp:
        assert gen.read() == exp.read()

    ItemSubgroup = _import_enum(item_subgroup_path, "ItemSubgroup")
    expected_subgroups = [
        "subgroup1-1",
        "subgroup1-2",
        "subgroup2-1",
        "subgroup2-2",
        "unmined-resource-basic-solid",
        "unmined-resource-basic-fluid",
        "technology",
    ]
    subgroup_members = [m.value for m in ItemSubgroup]
    assert set(subgroup_members) == set(expected_subgroups)
    assert len(subgroup_members) == len(expected_subgroups)
