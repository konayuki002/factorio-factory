from sympy import Integer, Rational
from core.enums.assembling_machine import AssemblingMachine
from core.enums.operation_category import OperationCategory

TYPES: dict[AssemblingMachine, str] = {
    AssemblingMachine.OilRefinery: "assembling-machine",
    AssemblingMachine.Centrifuge: "assembling-machine",
    AssemblingMachine.ChemicalPlant: "assembling-machine",
    AssemblingMachine.AssemblingMachine2: "assembling-machine",
    AssemblingMachine.AssemblingMachine1: "assembling-machine",
    AssemblingMachine.AssemblingMachine3: "assembling-machine",
    AssemblingMachine.StoneFurnace: "furnace",
    AssemblingMachine.ElectricFurnace: "furnace",
    AssemblingMachine.SteelFurnace: "furnace",
    AssemblingMachine.Lab: "lab",
    AssemblingMachine.Pumpjack: "mining-drill",
    AssemblingMachine.ElectricMiningDrill: "mining-drill",
    AssemblingMachine.BurnerMiningDrill: "mining-drill",
}

SPEED: dict[AssemblingMachine, Rational] = {
    AssemblingMachine.OilRefinery: Integer(1),
    AssemblingMachine.Centrifuge: Integer(1),
    AssemblingMachine.ChemicalPlant: Integer(1),
    AssemblingMachine.AssemblingMachine2: Rational(3, 4),
    AssemblingMachine.AssemblingMachine1: Rational(1, 2),
    AssemblingMachine.AssemblingMachine3: Rational(5, 4),
    AssemblingMachine.StoneFurnace: Integer(1),
    AssemblingMachine.ElectricFurnace: Integer(2),
    AssemblingMachine.SteelFurnace: Integer(2),
    AssemblingMachine.Lab: Integer(0),
    AssemblingMachine.Pumpjack: Integer(1),
    AssemblingMachine.ElectricMiningDrill: Rational(1, 2),
    AssemblingMachine.BurnerMiningDrill: Rational(1, 4),
}

CATEGORIES: dict[AssemblingMachine, set[OperationCategory]] = {
    AssemblingMachine.OilRefinery: {OperationCategory.OilProcessing},
    AssemblingMachine.Centrifuge: {OperationCategory.Centrifuging},
    AssemblingMachine.ChemicalPlant: {OperationCategory.Chemistry},
    AssemblingMachine.AssemblingMachine2: {OperationCategory.AdvancedCrafting, OperationCategory.BasicCrafting, OperationCategory.Crafting, OperationCategory.CraftingWithFluid},
    AssemblingMachine.AssemblingMachine1: {OperationCategory.AdvancedCrafting, OperationCategory.BasicCrafting, OperationCategory.Crafting},
    AssemblingMachine.AssemblingMachine3: {OperationCategory.AdvancedCrafting, OperationCategory.BasicCrafting, OperationCategory.Crafting, OperationCategory.CraftingWithFluid},
    AssemblingMachine.StoneFurnace: {OperationCategory.Smelting},
    AssemblingMachine.ElectricFurnace: {OperationCategory.Smelting},
    AssemblingMachine.SteelFurnace: {OperationCategory.Smelting},
    AssemblingMachine.Lab: set(),
    AssemblingMachine.Pumpjack: {OperationCategory.Mining},
    AssemblingMachine.ElectricMiningDrill: {OperationCategory.Mining},
    AssemblingMachine.BurnerMiningDrill: {OperationCategory.Mining},
}

ENERGY_USAGE_KW: dict[AssemblingMachine, Rational] = {
    AssemblingMachine.OilRefinery: Integer(420),
    AssemblingMachine.Centrifuge: Integer(350),
    AssemblingMachine.ChemicalPlant: Integer(210),
    AssemblingMachine.AssemblingMachine2: Integer(150),
    AssemblingMachine.AssemblingMachine1: Integer(75),
    AssemblingMachine.AssemblingMachine3: Integer(375),
    AssemblingMachine.StoneFurnace: Integer(90),
    AssemblingMachine.ElectricFurnace: Integer(180),
    AssemblingMachine.SteelFurnace: Integer(90),
    AssemblingMachine.Lab: Integer(60),
    AssemblingMachine.Pumpjack: Integer(90),
    AssemblingMachine.ElectricMiningDrill: Integer(90),
    AssemblingMachine.BurnerMiningDrill: Integer(150),
}

ALLOWED_EFFECTS: dict[AssemblingMachine, set[str]] = {
    AssemblingMachine.OilRefinery: {'consumption', 'pollution', 'productivity', 'speed'},
    AssemblingMachine.Centrifuge: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.ChemicalPlant: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.AssemblingMachine2: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.AssemblingMachine1: {'consumption', 'pollution', 'speed'},
    AssemblingMachine.AssemblingMachine3: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.StoneFurnace: {'consumption', 'pollution', 'speed'},
    AssemblingMachine.ElectricFurnace: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.SteelFurnace: {'consumption', 'pollution', 'speed'},
    AssemblingMachine.Lab: set(),
    AssemblingMachine.Pumpjack: {'consumption', 'pollution', 'productivity', 'speed'},
    AssemblingMachine.ElectricMiningDrill: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.BurnerMiningDrill: set(),
}

MODULE_SLOTS: dict[AssemblingMachine, int] = {
    AssemblingMachine.OilRefinery: 3,
    AssemblingMachine.Centrifuge: 2,
    AssemblingMachine.ChemicalPlant: 3,
    AssemblingMachine.AssemblingMachine2: 2,
    AssemblingMachine.AssemblingMachine1: 0,
    AssemblingMachine.AssemblingMachine3: 4,
    AssemblingMachine.StoneFurnace: 0,
    AssemblingMachine.ElectricFurnace: 2,
    AssemblingMachine.SteelFurnace: 0,
    AssemblingMachine.Lab: 2,
    AssemblingMachine.Pumpjack: 2,
    AssemblingMachine.ElectricMiningDrill: 3,
    AssemblingMachine.BurnerMiningDrill: 0,
}