from core.enums.material import Material

resource_allowed: set[Material] = {
    Material.ResourceCoal,
    Material.ResourceCopperOre,
    Material.ResourceCrudeOil,
    Material.ResourceIronOre,
    Material.ResourceStone,
    Material.ResourceUraniumOre,
}