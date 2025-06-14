from typing import Union

from pydantic import BaseModel, computed_field, field_validator
from sympy import Integer

from core.enums.material import Material as MaterialEnum
from core.models.allowed.fluid import fluid_allowed
from core.models.allowed.item import item_allowed
from core.models.allowed.resource import resource_allowed
from core.models.allowed.technology import technology_allowed
from core.models.data.item import STACK_SIZE


class MaterialBase(BaseModel):
    id: MaterialEnum


class Item(MaterialBase):
    @field_validator("id")
    def validate_item(cls, v: MaterialEnum) -> MaterialEnum:
        if v not in item_allowed:
            raise ValueError(f"Invalid item: {v}")
        return v

    @property
    @computed_field(return_type=Integer, repr=False)
    def stack_size(self) -> Integer:
        """
        アイテムのスタックサイズを返す.
        """
        try:
            return STACK_SIZE[self.id]
        except KeyError as e:
            raise ValueError(f"Invalid item stack size for: {self.id}") from e


class Fluid(MaterialBase):
    @field_validator("id")
    def validate_fluid(cls, v: MaterialEnum) -> MaterialEnum:
        if v not in fluid_allowed:
            raise ValueError(f"Invalid fluid: {v}")
        return v


class Resource(MaterialBase):
    @field_validator("id")
    def validate_resource(cls, v: MaterialEnum) -> MaterialEnum:
        if v not in resource_allowed:
            raise ValueError(f"Invalid resource: {v}")
        return v


class Technology(MaterialBase):
    @field_validator("id")
    def validate_technology(cls, v: MaterialEnum) -> MaterialEnum:
        if v not in technology_allowed:
            raise ValueError(f"Invalid technology: {v}")
        return v


Material = Union[Item, Fluid, Resource, Technology]
