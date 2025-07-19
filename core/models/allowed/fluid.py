from core.enums.material import Material

fluid_allowed: set[Material] = {
    Material.Water,
    Material.Steam,
    Material.SulfuricAcid,
    Material.CrudeOil,
    Material.HeavyOil,
    Material.LightOil,
    Material.PetroleumGas,
    Material.Lubricant,
}
