from pydantic import BaseModel

from core.enums.item_group import ItemGroup


class ItemGroup(BaseModel):
    id: ItemGroup
