from core.enums.operation import Operation

mining_allowed: set[Operation] = {
    Operation.MiningIronOre,
    Operation.MiningCopperOre,
    Operation.MiningCoal,
    Operation.MiningStone,
    Operation.MiningUraniumOre,
    Operation.MiningCrudeOil,
}
