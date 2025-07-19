from core.enums.operation import Operation

mining_allowed: set[Operation] = {
    Operation.MiningIronOre,
    Operation.MiningStone,
    Operation.MiningUraniumOre,
    Operation.MiningCopperOre,
    Operation.MiningCoal,
    Operation.MiningCrudeOil,
}