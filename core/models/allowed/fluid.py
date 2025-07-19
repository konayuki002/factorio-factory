from core.enums.material import Material

fluid_allowed: set[Material] = {
    Material.CrudeOil,
    Material.Lubricant,
    Material.Water,
    Material.SulfuricAcid,
    Material.PetroleumGas,
    Material.LightOil,
    Material.Steam,
    Material.HeavyOil,
}