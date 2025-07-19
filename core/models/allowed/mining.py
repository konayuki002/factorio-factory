from core.enums.operation import Operation

mining_allowed: set[Operation] = {
    Operation.MiningCoal,
    Operation.MiningCopperOre,
    Operation.MiningCrudeOil,
    Operation.MiningIronOre,
    Operation.MiningStone,
    Operation.MiningUraniumOre,
}