from pydantic import BaseModel

from core.enums.item_group import ItemGroup as ItemGroupEnum


class ItemGroup(BaseModel):
    id: ItemGroupEnum
