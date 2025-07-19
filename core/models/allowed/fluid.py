from core.enums.material import Material

fluid_allowed: set[Material] = {
    Material.SulfuricAcid,
    Material.Lubricant,
    Material.CrudeOil,
    Material.HeavyOil,
    Material.Water,
    Material.PetroleumGas,
    Material.LightOil,
    Material.Steam,
}