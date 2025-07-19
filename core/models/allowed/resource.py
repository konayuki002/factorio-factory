from core.enums.material import Material

resource_allowed: set[Material] = {
    Material.ResourceIronOre,
    Material.ResourceStone,
    Material.ResourceUraniumOre,
    Material.ResourceCopperOre,
    Material.ResourceCoal,
    Material.ResourceCrudeOil,
}