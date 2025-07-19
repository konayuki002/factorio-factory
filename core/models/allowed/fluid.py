from core.enums.material import Material

fluid_allowed: set[Material] = {
    Material.CrudeOil,
    Material.HeavyOil,
    Material.LightOil,
    Material.Lubricant,
    Material.PetroleumGas,
    Material.Steam,
    Material.SulfuricAcid,
    Material.Water,
}