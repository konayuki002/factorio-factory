from enum import Enum


class ItemGroup(Enum):
    Logistics = 'logistics'
    Environment = 'environment'
    Enemies = 'enemies'
    Production = 'production'
    Signals = 'signals'
    Effects = 'effects'
    Combat = 'combat'
    Fluids = 'fluids'
    Tiles = 'tiles'
    Other = 'other'
    IntermediateProducts = 'intermediate-products'
    UnminedResource = 'unmined-resource'
    Technology = 'technology'
