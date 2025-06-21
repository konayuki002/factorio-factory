from sympy import Integer, Rational

from core.enums.assembling_machine import AssemblingMachine

CRAFTING_SPEED: dict[AssemblingMachine, Rational] = {
    AssemblingMachine.StoneFurnace: Integer(1),
    AssemblingMachine.OffshorePump: Integer(0),
    AssemblingMachine.AssemblingMachine1: Rational(1, 2),
    AssemblingMachine.AssemblingMachine2: Rational(3, 4),
    AssemblingMachine.Lab: Integer(0),
    AssemblingMachine.ElectricFurnace: Integer(2),
    AssemblingMachine.SteelFurnace: Integer(2),
    AssemblingMachine.AssemblingMachine3: Rational(5, 4),
    AssemblingMachine.RocketSilo: Integer(1),
    AssemblingMachine.OilRefinery: Integer(1),
    AssemblingMachine.ChemicalPlant: Integer(1),
    AssemblingMachine.Centrifuge: Integer(1),
    AssemblingMachine.ElectricMiningDrill: Rational(1, 2),
    AssemblingMachine.BurnerMiningDrill: Rational(1, 4),
    AssemblingMachine.Pumpjack: Integer(1),
}

ENERGY_USAGE_KW: dict[AssemblingMachine, Integer] = {
    AssemblingMachine.StoneFurnace: Integer(90),
    AssemblingMachine.OffshorePump: Integer(60),
    AssemblingMachine.AssemblingMachine1: Integer(75),
    AssemblingMachine.AssemblingMachine2: Integer(150),
    AssemblingMachine.Lab: Integer(60),
    AssemblingMachine.ElectricFurnace: Integer(180),
    AssemblingMachine.SteelFurnace: Integer(90),
    AssemblingMachine.AssemblingMachine3: Integer(375),
    AssemblingMachine.RocketSilo: Integer(250),
    AssemblingMachine.OilRefinery: Integer(420),
    AssemblingMachine.ChemicalPlant: Integer(210),
    AssemblingMachine.Centrifuge: Integer(350),
    AssemblingMachine.ElectricMiningDrill: Integer(90),
    AssemblingMachine.BurnerMiningDrill: Integer(150),
    AssemblingMachine.Pumpjack: Integer(90),
}

MODULE_SLOTS: dict[AssemblingMachine, Integer] = {
    AssemblingMachine.StoneFurnace: Integer(0),
    AssemblingMachine.OffshorePump: Integer(0),
    AssemblingMachine.AssemblingMachine1: Integer(0),
    AssemblingMachine.AssemblingMachine2: Integer(2),
    AssemblingMachine.Lab: Integer(2),
    AssemblingMachine.ElectricFurnace: Integer(2),
    AssemblingMachine.SteelFurnace: Integer(0),
    AssemblingMachine.AssemblingMachine3: Integer(4),
    AssemblingMachine.RocketSilo: Integer(4),
    AssemblingMachine.OilRefinery: Integer(3),
    AssemblingMachine.ChemicalPlant: Integer(3),
    AssemblingMachine.Centrifuge: Integer(2),
    AssemblingMachine.ElectricMiningDrill: Integer(3),
    AssemblingMachine.BurnerMiningDrill: Integer(0),
    AssemblingMachine.Pumpjack: Integer(2),
}
