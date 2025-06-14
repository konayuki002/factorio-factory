from pathlib import Path

from sympy.core import Integer
from sympy.printing import srepr

from core.loader.converters.base import BaseConverter
from core.loader.registry import register


@register("data:item")
class ItemDataConverter(BaseConverter):
    """
    アイテムに関するJSON -> Data 辞書の生成.
    具体的には、以下のファイルを処理します:
    intermediate/items.json -> data/item.py
    """

    dependencies = ["json:item", "enum:material"]
    json_filename = "item.json"
    enum_filename = "material.py"
    data_path = "item.py"

    def load(self) -> None:
        # 1) JSON load
        json_items_path = f"{self.intermediate_dir}/{self.json_filename}"
        items = self.load_json(json_items_path)

        # 2) Enum load
        enum_material_path = f"{self.enum_dir}/{self.enum_filename}"
        EnumMaterialClass = self.load_enum("Material", enum_material_path)

        # 3) Data 辞書を生成して保存
        ret = {EnumMaterialClass(item["name"]): item["stack_size"] for item in items}

        out = [
            "from enums.material import Material",
            "from sympy import Integer",
            "",
            "STACK_SIZE: dict[Material, Integer] = {",
            *[
                f"    {material}: {srepr(Integer(stack_size))},"
                for material, stack_size in ret.items()
            ],
            "}",
        ]

        # 2) Data 辞書を生成して保存
        (Path(self.data_dir) / self.data_path).write_text("\n".join(out))
