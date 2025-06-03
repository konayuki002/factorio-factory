import os
import shutil
import importlib.util

import pytest

from core.loader.converters.enum.item_groups import ItemGroupEnumConverter
from core.enums.manual_item_group import MANUAL_MEMBERS
from core.utils.utils import to_enum_member


@pytest.fixture
def enum_converter(tmp_path):
    """Prepare ItemGroupEnumConverter with fixture JSON files."""
    interm = tmp_path / "intermediate"
    enum_dir = tmp_path / "enums"
    interm.mkdir()
    enum_dir.mkdir()
    fixtures_dir = os.path.join(os.path.dirname(__file__), "fixtures")

    shutil.copyfile(
        os.path.join(fixtures_dir, "json_sample_item_groups.json"),
        interm / "item_groups.json",
    )
    shutil.copyfile(
        os.path.join(fixtures_dir, "json_sample_item_subgroups.json"),
        interm / "item_subgroups.json",
    )

    converter = ItemGroupEnumConverter()
    converter.intermediate_dir = str(interm)
    converter.enum_dir = str(enum_dir)
    return converter


def _load_enum_module(path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def test_item_group_enum_generation(enum_converter):
    converter = enum_converter
    converter.load()

    group_py = os.path.join(converter.enum_dir, "item_group.py")
    subgroup_py = os.path.join(converter.enum_dir, "item_subgroup.py")
    assert os.path.isfile(group_py)
    assert os.path.isfile(subgroup_py)

    group_mod = _load_enum_module(group_py, "generated_item_group")
    subgroup_mod = _load_enum_module(subgroup_py, "generated_item_subgroup")

    ItemGroup = group_mod.ItemGroup
    ItemSubgroup = subgroup_mod.ItemSubgroup

    expected_groups = ["group1", "group2"] + MANUAL_MEMBERS["item_group"]
    expected_subgroups = [
        "subgroup1-1",
        "subgroup1-2",
        "subgroup2-1",
        "subgroup2-2",
    ] + MANUAL_MEMBERS["item_subgroup"]

    assert [e.name for e in ItemGroup] == [to_enum_member(x) for x in expected_groups]
    assert [e.value for e in ItemGroup] == expected_groups

    assert [e.name for e in ItemSubgroup] == [to_enum_member(x) for x in expected_subgroups]
    assert [e.value for e in ItemSubgroup] == expected_subgroups
