from sympy import Integer, Rational
from core.enums.assembling_machine import AssemblingMachine
from core.enums.operation_category import OperationCategory

TYPES: dict[AssemblingMachine, str] = {
    AssemblingMachine.AssemblingMachine1: "assembling-machine",
    AssemblingMachine.ChemicalPlant: "assembling-machine",
    AssemblingMachine.AssemblingMachine2: "assembling-machine",
    AssemblingMachine.OilRefinery: "assembling-machine",
    AssemblingMachine.AssemblingMachine3: "assembling-machine",
    AssemblingMachine.Centrifuge: "assembling-machine",
    AssemblingMachine.ElectricFurnace: "furnace",
    AssemblingMachine.SteelFurnace: "furnace",
    AssemblingMachine.StoneFurnace: "furnace",
    AssemblingMachine.Lab: "lab",
    AssemblingMachine.Pumpjack: "mining-drill",
    AssemblingMachine.ElectricMiningDrill: "mining-drill",
    AssemblingMachine.BurnerMiningDrill: "mining-drill",
}

SPEED: dict[AssemblingMachine, Rational] = {
    AssemblingMachine.AssemblingMachine1: Rational(1, 2),
    AssemblingMachine.ChemicalPlant: Integer(1),
    AssemblingMachine.AssemblingMachine2: Rational(3, 4),
    AssemblingMachine.OilRefinery: Integer(1),
    AssemblingMachine.AssemblingMachine3: Rational(5, 4),
    AssemblingMachine.Centrifuge: Integer(1),
    AssemblingMachine.ElectricFurnace: Integer(2),
    AssemblingMachine.SteelFurnace: Integer(2),
    AssemblingMachine.StoneFurnace: Integer(1),
    AssemblingMachine.Lab: Integer(0),
    AssemblingMachine.Pumpjack: Integer(1),
    AssemblingMachine.ElectricMiningDrill: Rational(1, 2),
    AssemblingMachine.BurnerMiningDrill: Rational(1, 4),
}

CATEGORIES: dict[AssemblingMachine, set[OperationCategory]] = {
    AssemblingMachine.AssemblingMachine1: {OperationCategory.AdvancedCrafting, OperationCategory.BasicCrafting, OperationCategory.Crafting},
    AssemblingMachine.ChemicalPlant: {OperationCategory.Chemistry},
    AssemblingMachine.AssemblingMachine2: {OperationCategory.AdvancedCrafting, OperationCategory.BasicCrafting, OperationCategory.Crafting, OperationCategory.CraftingWithFluid},
    AssemblingMachine.OilRefinery: {OperationCategory.OilProcessing},
    AssemblingMachine.AssemblingMachine3: {OperationCategory.AdvancedCrafting, OperationCategory.BasicCrafting, OperationCategory.Crafting, OperationCategory.CraftingWithFluid},
    AssemblingMachine.Centrifuge: {OperationCategory.Centrifuging},
    AssemblingMachine.ElectricFurnace: {OperationCategory.Smelting},
    AssemblingMachine.SteelFurnace: {OperationCategory.Smelting},
    AssemblingMachine.StoneFurnace: {OperationCategory.Smelting},
    AssemblingMachine.Lab: set(),
    AssemblingMachine.Pumpjack: {OperationCategory.Mining},
    AssemblingMachine.ElectricMiningDrill: {OperationCategory.Mining},
    AssemblingMachine.BurnerMiningDrill: {OperationCategory.Mining},
}

ENERGY_USAGE_KW: dict[AssemblingMachine, Rational] = {
    AssemblingMachine.AssemblingMachine1: Integer(75),
    AssemblingMachine.ChemicalPlant: Integer(210),
    AssemblingMachine.AssemblingMachine2: Integer(150),
    AssemblingMachine.OilRefinery: Integer(420),
    AssemblingMachine.AssemblingMachine3: Integer(375),
    AssemblingMachine.Centrifuge: Integer(350),
    AssemblingMachine.ElectricFurnace: Integer(180),
    AssemblingMachine.SteelFurnace: Integer(90),
    AssemblingMachine.StoneFurnace: Integer(90),
    AssemblingMachine.Lab: Integer(60),
    AssemblingMachine.Pumpjack: Integer(90),
    AssemblingMachine.ElectricMiningDrill: Integer(90),
    AssemblingMachine.BurnerMiningDrill: Integer(150),
}

ALLOWED_EFFECTS: dict[AssemblingMachine, set[str]] = {
    AssemblingMachine.AssemblingMachine1: {'consumption', 'pollution', 'speed'},
    AssemblingMachine.ChemicalPlant: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.AssemblingMachine2: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.OilRefinery: {'consumption', 'pollution', 'productivity', 'speed'},
    AssemblingMachine.AssemblingMachine3: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.Centrifuge: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.ElectricFurnace: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.SteelFurnace: {'consumption', 'pollution', 'speed'},
    AssemblingMachine.StoneFurnace: {'consumption', 'pollution', 'speed'},
    AssemblingMachine.Lab: set(),
    AssemblingMachine.Pumpjack: {'consumption', 'pollution', 'productivity', 'speed'},
    AssemblingMachine.ElectricMiningDrill: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.BurnerMiningDrill: set(),
}

MODULE_SLOTS: dict[AssemblingMachine, int] = {
    AssemblingMachine.AssemblingMachine1: 0,
    AssemblingMachine.ChemicalPlant: 3,
    AssemblingMachine.AssemblingMachine2: 2,
    AssemblingMachine.OilRefinery: 3,
    AssemblingMachine.AssemblingMachine3: 4,
    AssemblingMachine.Centrifuge: 2,
    AssemblingMachine.ElectricFurnace: 2,
    AssemblingMachine.SteelFurnace: 0,
    AssemblingMachine.StoneFurnace: 0,
    AssemblingMachine.Lab: 2,
    AssemblingMachine.Pumpjack: 2,
    AssemblingMachine.ElectricMiningDrill: 3,
    AssemblingMachine.BurnerMiningDrill: 0,
}