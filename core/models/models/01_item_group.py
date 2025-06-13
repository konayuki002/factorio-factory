# dummy below

from typing import Optional

from pydantic import BaseModel


class ItemGroup(BaseModel):
    type: str
    name: str
    order: Optional[str]
    icon: Optional[str]
    icon_size: Optional[int]
    order_in_recipe: Optional[str] = None


class ItemSubgroup(BaseModel):
    type: str
    name: str
    group: str
    order: str
