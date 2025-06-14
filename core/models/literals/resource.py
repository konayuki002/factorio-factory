from typing import Literal

from enums.material import Material

Resource = Literal[
    Material.ResourceIronOre,
    Material.ResourceCopperOre,
    Material.ResourceCoal,
    Material.ResourceStone,
    Material.ResourceUraniumOre,
    Material.ResourceCrudeOil,
]