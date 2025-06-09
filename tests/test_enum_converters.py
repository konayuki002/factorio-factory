import os
import shutil
import pytest

# テストケース定義: (ConverterClass, json_fixture, enum_name, enum_pyfile)
TEST_CASES = [
    (
        "core.loader.converters.enum.item_group.ItemGroupEnumConverter",
        "json_sample_item_groups.json",
        "ItemGroup",
        "item_group.py",
    ),
    (
        "core.loader.converters.enum.item_subgroup.ItemSubgroupEnumConverter",
        "json_sample_item_subgroups.json",
        "ItemSubgroup",
        "item_subgroup.py",
    ),
    (
        "core.loader.converters.enum.material.MaterialEnumConverter",
        [
            "json_sample_item.json",
            "json_sample_fluid.json",
            "json_sample_resources.json",
            "json_sample_technology.json",
        ],
        "Material",
        "material.py",
    ),
    (
        "core.loader.converters.enum.process_category.ProcessCategoryEnumConverter",
        "json_sample_recipe_category.json",
        "ProcessCategory",
        "process_category.py",
    ),
    # 他のenum converterもここに追加可能
    (
        "core.loader.converters.enum.process.ProcessEnumConverter",
        [
            "json_sample_recipe.json",
            "json_sample_technology.json",
            "json_sample_resources.json",
        ],
        "Process",
        "process.py",
    ),
    (
        "core.loader.converters.enum.assembling_machine.AssemblingMachineEnumConverter",
        [
            "json_sample_entities.json",
            "json_sample_mining_drill.json",
        ],
        "AssemblingMachine",
        "assembling_machine.py",
    ),
]


def _import_enum(enum_py_path, enum_name):
    import importlib.util

    spec = importlib.util.spec_from_file_location(enum_name, enum_py_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, enum_name)


@pytest.mark.parametrize(
    "converter_path,json_fixture,enum_name,enum_pyfile", TEST_CASES
)
def test_enum_converter(tmp_path, converter_path, json_fixture, enum_name, enum_pyfile):
    # Converterクラスをimport
    module_path, class_name = converter_path.rsplit(".", 1)
    ConverterClass = getattr(__import__(module_path, fromlist=[class_name]), class_name)

    # 入出力ディレクトリ準備
    input_base = tmp_path / "input"
    enum_base = tmp_path / "enum"
    input_base.mkdir()
    enum_base.mkdir()
    fixtures_dir = os.path.join(os.path.dirname(__file__), "fixtures")

    # JSONファイルをコピー
    if isinstance(json_fixture, list):
        json_filenames = sorted(ConverterClass.json_filenames)
        for fixture, json_filename in zip(sorted(json_fixture), json_filenames):
            shutil.copyfile(
                os.path.join(fixtures_dir, fixture),
                input_base / json_filename,  # Converterが期待するJSONファイル名
            )
    else:
        shutil.copyfile(
            os.path.join(fixtures_dir, json_fixture),
            input_base
            / ConverterClass.json_filename,  # Converterが期待するJSONファイル名
        )

    # Converterインスタンス生成
    converter = ConverterClass()
    converter.intermediate_dir = str(input_base)
    converter.enum_dir = str(enum_base)

    # 変換実行
    converter.load()

    # 生成されたEnumをimportして検証
    enum_py_path = os.path.join(converter.enum_dir, enum_pyfile)
    assert os.path.isfile(enum_py_path), f"{enum_py_path} が生成されていません"
    EnumClass = _import_enum(enum_py_path, enum_name)

    # 期待されるEnumをfixturesからimport
    expected_enum_py = os.path.join(fixtures_dir, f"enum_sample_{enum_pyfile}")
    assert os.path.isfile(expected_enum_py), f"{expected_enum_py} が存在しません"
    ExpectedEnumClass = _import_enum(expected_enum_py, enum_name)

    # メンバー名・値が一致するか
    # 異なるEnumは内部的なオブジェクトが異なるため、文字列を比較する
    actual_members = [(m.name, m.value) for m in EnumClass]
    expected_members = [(m.name, m.value) for m in ExpectedEnumClass]
    assert (
        actual_members == expected_members
    ), f"Enum members mismatch: {actual_members} vs {expected_members}"
