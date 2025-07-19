from core.enums.material import Material

resource_allowed: set[Material] = {
    Material.ResourceCrudeOil,
    Material.ResourceUraniumOre,
    Material.ResourceIronOre,
    Material.ResourceCopperOre,
    Material.ResourceCoal,
    Material.ResourceStone,
}