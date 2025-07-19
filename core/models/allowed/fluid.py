from core.enums.material import Material

fluid_allowed: set[Material] = {
    Material.Water,
    Material.HeavyOil,
    Material.Steam,
    Material.LightOil,
    Material.Lubricant,
    Material.PetroleumGas,
    Material.SulfuricAcid,
    Material.CrudeOil,
}