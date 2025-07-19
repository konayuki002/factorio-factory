from enum import Enum


class ItemGroup(Enum):
    Effects = 'effects'
    IntermediateProducts = 'intermediate-products'
    Environment = 'environment'
    Signals = 'signals'
    Logistics = 'logistics'
    Combat = 'combat'
    Production = 'production'
    Fluids = 'fluids'
    Other = 'other'
    Tiles = 'tiles'
    Enemies = 'enemies'
    UnminedResource = 'unmined-resource'
    Technology = 'technology'
