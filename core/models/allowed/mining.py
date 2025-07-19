from core.enums.operation import Operation

mining_allowed: set[Operation] = {
    Operation.MiningCrudeOil,
    Operation.MiningUraniumOre,
    Operation.MiningIronOre,
    Operation.MiningCopperOre,
    Operation.MiningCoal,
    Operation.MiningStone,
}