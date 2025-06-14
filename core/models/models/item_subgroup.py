from pydantic import BaseModel

from core.enums.item_subgroup import ItemSubgroup as ItemSubgroupEnum


class ItemSubgroup(BaseModel):
    id: ItemSubgroupEnum
