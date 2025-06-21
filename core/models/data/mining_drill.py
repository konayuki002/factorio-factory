from sympy import Integer, Rational

from core.enums.assembling_machine import AssemblingMachine

MINING_SPEED: dict[AssemblingMachine, Rational] = {
    AssemblingMachine.ElectricMiningDrill: Rational(1, 2),
    AssemblingMachine.BurnerMiningDrill: Rational(1, 4),
    AssemblingMachine.Pumpjack: Integer(1),
}

ENERGY_USAGE_KW: dict[AssemblingMachine, Integer] = {
    AssemblingMachine.ElectricMiningDrill: Integer(90),
    AssemblingMachine.BurnerMiningDrill: Integer(150),
    AssemblingMachine.Pumpjack: Integer(90),
}

MODULE_SLOTS: dict[AssemblingMachine, Integer] = {
    AssemblingMachine.ElectricMiningDrill: Integer(3),
    AssemblingMachine.BurnerMiningDrill: Integer(0),
    AssemblingMachine.Pumpjack: Integer(2),
}
