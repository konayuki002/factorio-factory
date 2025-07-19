from core.enums.material import Material

resource_allowed: set[Material] = {
    Material.ResourceCoal,
    Material.ResourceCopperOre,
    Material.ResourceIronOre,
    Material.ResourceUraniumOre,
    Material.ResourceCrudeOil,
    Material.ResourceStone,
}