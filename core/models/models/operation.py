from typing import Union

from pydantic import BaseModel, field_validator

from core.enums.operation import Operation as OperationEnum
from core.models.allowed.mining import mining_allowed
from core.models.allowed.recipe import recipe_allowed
from core.models.allowed.research import research_allowed


class OperationBase(BaseModel):
    id: OperationEnum


class Mining(OperationBase):
    @field_validator("id")
    def validate_item(cls, v: OperationEnum) -> OperationEnum:
        if v not in mining_allowed:
            raise ValueError(f"Invalid item: {v}")
        return v


class Recipe(OperationBase):
    @field_validator("id")
    def validate_fluid(cls, v: OperationEnum) -> OperationEnum:
        if v not in recipe_allowed:
            raise ValueError(f"Invalid fluid: {v}")
        return v


class Research(OperationBase):
    @field_validator("id")
    def validate_resource(cls, v: OperationEnum) -> OperationEnum:
        if v not in research_allowed:
            raise ValueError(f"Invalid resource: {v}")
        return v


Operation = Union[Mining, Recipe, Research]
