from core.enums.material import Material

resource_allowed: set[Material] = {
    Material.ResourceIronOre,
    Material.ResourceStone,
    Material.ResourceCopperOre,
    Material.ResourceCrudeOil,
    Material.ResourceCoal,
    Material.ResourceUraniumOre,
}