from enum import Enum


class ItemGroup(Enum):
    Combat = 'combat'
    Effects = 'effects'
    Enemies = 'enemies'
    Environment = 'environment'
    Fluids = 'fluids'
    IntermediateProducts = 'intermediate-products'
    Logistics = 'logistics'
    Other = 'other'
    Production = 'production'
    Signals = 'signals'
    Technology = 'technology'
    Tiles = 'tiles'
    UnminedResource = 'unmined-resource'
