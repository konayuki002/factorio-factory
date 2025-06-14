from typing import Union

from pydantic import BaseModel

from core.enums.material import Material as MaterialEnum
from core.models.literals.fluid import Fluid as FluidLiteral
from core.models.literals.item import Item as ItemLiteral
from core.models.literals.resource import Resource as ResourceLiteral
from core.models.literals.technology import Technology as TechnologyLiteral


class MaterialBase(BaseModel):
    id: MaterialEnum


class Item(MaterialBase):
    id: ItemLiteral


class Fluid(MaterialBase):
    id: FluidLiteral


class Resource(MaterialBase):
    id: ResourceLiteral


class Technology(MaterialBase):
    id: TechnologyLiteral


Material = Union[Item, Fluid, Resource, Technology]
