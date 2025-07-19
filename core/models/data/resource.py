from core.enums.operation import Operation
from sympy import Integer

TIME: dict[Operation, Integer] = {
    Operation.MiningCoal: Integer(1),
    Operation.MiningCopperOre: Integer(1),
    Operation.MiningIronOre: Integer(1),
    Operation.MiningUraniumOre: Integer(2),
    Operation.MiningCrudeOil: Integer(1),
    Operation.MiningStone: Integer(1),
}