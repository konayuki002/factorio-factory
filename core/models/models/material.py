from typing import Union

from pydantic import BaseModel, field_validator

from core.enums.material import Material as MaterialEnum
from core.models.literals.fluid import fluid_allowed
from core.models.literals.item import item_allowed
from core.models.literals.resource import resource_allowed
from core.models.literals.technology import technology_allowed


class MaterialBase(BaseModel):
    id: MaterialEnum


class Item(MaterialBase):
    @field_validator("id")
    def validate_item(cls, v: MaterialEnum) -> MaterialEnum:
        if v not in item_allowed:
            raise ValueError(f"Invalid item: {v}")
        return v


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
