from core.enums.operation import Operation

mining_allowed: set[Operation] = {
    Operation.MiningIronOre,
    Operation.MiningStone,
    Operation.MiningCopperOre,
    Operation.MiningCrudeOil,
    Operation.MiningCoal,
    Operation.MiningUraniumOre,
}