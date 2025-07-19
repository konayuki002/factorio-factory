from core.enums.operation import Operation

mining_allowed: set[Operation] = {
    Operation.MiningCoal,
    Operation.MiningCopperOre,
    Operation.MiningIronOre,
    Operation.MiningUraniumOre,
    Operation.MiningCrudeOil,
    Operation.MiningStone,
}