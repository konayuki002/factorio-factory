from typing import Literal

from enums.material import Material

Fluid = Literal[
    Material.Water,
    Material.Steam,
    Material.SulfuricAcid,
    Material.CrudeOil,
    Material.HeavyOil,
    Material.LightOil,
    Material.PetroleumGas,
    Material.Lubricant,
]