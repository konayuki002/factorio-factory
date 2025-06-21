from typing import Union

from pydantic import BaseModel, computed_field, field_validator
from sympy import Expr, Integer, Rational

from core.enums.material import Material as MaterialEnum
from core.enums.operation import Operation as OperationEnum
from core.enums.operation_category import OperationCategory as CategoryEnum
from core.models.allowed.mining import mining_allowed
from core.models.allowed.recipe import recipe_allowed
from core.models.allowed.research import research_allowed
from core.models.data.operation import CATEGORY_OF_RECIPE, INGREDIENTS, RESULTS
from core.models.data.recipe import ENERGY_REQUIRED
from core.models.data.research import TIME as RESEARCH_TIME
from core.models.data.resource import TIME as MINING_TIME


class OperationBase(BaseModel):
    id: OperationEnum

    @property
    @computed_field(return_type=dict[MaterialEnum, Expr], repr=False)
    def ingredients(self) -> dict[MaterialEnum, Expr]:
        """
        この操作に必要な材料を返す.
        """
        try:
            return INGREDIENTS[self.id]
        except KeyError as e:
            raise ValueError(f"Invalid ingredients for operation: {self.id}") from e

    @property
    @computed_field(return_type=dict[MaterialEnum, Integer], repr=False)
    def results(self) -> dict[MaterialEnum, Integer]:
        """
        この操作の結果を返す.
        """
        try:
            return RESULTS[self.id]
        except KeyError as e:
            raise ValueError(f"Invalid results for operation: {self.id}") from e

    @property
    @computed_field(return_type=CategoryEnum, repr=False)
    def category(self) -> CategoryEnum:
        """
        この操作のカテゴリを返す.
        """
        try:
            return CATEGORY_OF_RECIPE[self.id]
        except KeyError as e:
            raise ValueError(f"Invalid category for operation: {self.id}") from e


class Mining(OperationBase):
    @field_validator("id")
    def validate_item(cls, v: OperationEnum) -> OperationEnum:
        if v not in mining_allowed:
            raise ValueError(f"Invalid item: {v}")
        return v

    @property
    @computed_field(return_type=Integer, repr=False)
    def time(self) -> Integer:
        """
        採掘にかかる時間を返す.
        """
        try:
            return MINING_TIME[self.id]
        except KeyError as e:
            raise ValueError(f"Invalid mining time required for: {self.id}") from e


class Recipe(OperationBase):
    @field_validator("id")
    def validate_fluid(cls, v: OperationEnum) -> OperationEnum:
        if v not in recipe_allowed:
            raise ValueError(f"Invalid fluid: {v}")
        return v

    @property
    @computed_field(return_type=Rational, repr=False)
    def energy_required(self) -> Rational:
        """
        レシピのエネルギー消費量を返す.
        """
        try:
            return ENERGY_REQUIRED[self.id]
        except KeyError as e:
            raise ValueError(f"Invalid recipe energy required for: {self.id}") from e


class Research(OperationBase):
    @field_validator("id")
    def validate_resource(cls, v: OperationEnum) -> OperationEnum:
        if v not in research_allowed:
            raise ValueError(f"Invalid resource: {v}")
        return v

    @property
    @computed_field(return_type=Integer, repr=False)
    def time(self) -> Integer:
        """
        研究にかかる時間を返す.
        """
        try:
            return RESEARCH_TIME[self.id]
        except KeyError as e:
            raise ValueError(f"Invalid research time required for: {self.id}") from e


Operation = Union[Mining, Recipe, Research]
