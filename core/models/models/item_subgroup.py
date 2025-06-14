from pydantic import BaseModel

from core.enums.item_subgroup import ItemSubgroup


class ItemSubgroup(BaseModel):
    id: ItemSubgroup
