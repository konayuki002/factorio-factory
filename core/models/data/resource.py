from sympy import Integer

from core.enums.operation import Operation

TIME: dict[Operation, Integer] = {
    Operation.MiningIronOre: Integer(1),
    Operation.MiningCopperOre: Integer(1),
    Operation.MiningCoal: Integer(1),
    Operation.MiningStone: Integer(1),
    Operation.MiningUraniumOre: Integer(2),
    Operation.MiningCrudeOil: Integer(1),
}
