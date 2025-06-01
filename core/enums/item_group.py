from enum import Enum


class ItemGroup(Enum):
    Logistics = 'logistics'
    Production = 'production'
    IntermediateProducts = 'intermediate-products'
    Combat = 'combat'
    Fluids = 'fluids'
    Signals = 'signals'
    Enemies = 'enemies'
    Environment = 'environment'
    Tiles = 'tiles'
    Effects = 'effects'
    Other = 'other'
