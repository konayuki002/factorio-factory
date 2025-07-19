from enum import Enum


class ItemGroup(Enum):
    Signals = 'signals'
    Enemies = 'enemies'
    Environment = 'environment'
    Tiles = 'tiles'
    IntermediateProducts = 'intermediate-products'
    Production = 'production'
    Other = 'other'
    Effects = 'effects'
    Logistics = 'logistics'
    Fluids = 'fluids'
    Combat = 'combat'
    UnminedResource = 'unmined-resource'
    Technology = 'technology'
