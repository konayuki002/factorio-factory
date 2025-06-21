from core.enums.material import Material

resource_allowed: set[Material] = {
    Material.ResourceIronOre,
    Material.ResourceCopperOre,
    Material.ResourceCoal,
    Material.ResourceStone,
    Material.ResourceUraniumOre,
    Material.ResourceCrudeOil,
}
