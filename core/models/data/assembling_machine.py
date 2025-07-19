from sympy import Integer, Rational
from core.enums.assembling_machine import AssemblingMachine
from core.enums.operation_category import OperationCategory

TYPES: dict[AssemblingMachine, str] = {
    AssemblingMachine.AssemblingMachine3: "assembling-machine",
    AssemblingMachine.Centrifuge: "assembling-machine",
    AssemblingMachine.ChemicalPlant: "assembling-machine",
    AssemblingMachine.AssemblingMachine2: "assembling-machine",
    AssemblingMachine.OilRefinery: "assembling-machine",
    AssemblingMachine.AssemblingMachine1: "assembling-machine",
    AssemblingMachine.StoneFurnace: "furnace",
    AssemblingMachine.ElectricFurnace: "furnace",
    AssemblingMachine.SteelFurnace: "furnace",
    AssemblingMachine.Lab: "lab",
    AssemblingMachine.BurnerMiningDrill: "mining-drill",
    AssemblingMachine.ElectricMiningDrill: "mining-drill",
    AssemblingMachine.Pumpjack: "mining-drill",
}

SPEED: dict[AssemblingMachine, Rational] = {
    AssemblingMachine.AssemblingMachine3: Rational(5, 4),
    AssemblingMachine.Centrifuge: Integer(1),
    AssemblingMachine.ChemicalPlant: Integer(1),
    AssemblingMachine.AssemblingMachine2: Rational(3, 4),
    AssemblingMachine.OilRefinery: Integer(1),
    AssemblingMachine.AssemblingMachine1: Rational(1, 2),
    AssemblingMachine.StoneFurnace: Integer(1),
    AssemblingMachine.ElectricFurnace: Integer(2),
    AssemblingMachine.SteelFurnace: Integer(2),
    AssemblingMachine.Lab: Integer(0),
    AssemblingMachine.BurnerMiningDrill: Rational(1, 4),
    AssemblingMachine.ElectricMiningDrill: Rational(1, 2),
    AssemblingMachine.Pumpjack: Integer(1),
}

CATEGORIES: dict[AssemblingMachine, set[OperationCategory]] = {
    AssemblingMachine.AssemblingMachine3: {OperationCategory.AdvancedCrafting, OperationCategory.BasicCrafting, OperationCategory.Crafting, OperationCategory.CraftingWithFluid},
    AssemblingMachine.Centrifuge: {OperationCategory.Centrifuging},
    AssemblingMachine.ChemicalPlant: {OperationCategory.Chemistry},
    AssemblingMachine.AssemblingMachine2: {OperationCategory.AdvancedCrafting, OperationCategory.BasicCrafting, OperationCategory.Crafting, OperationCategory.CraftingWithFluid},
    AssemblingMachine.OilRefinery: {OperationCategory.OilProcessing},
    AssemblingMachine.AssemblingMachine1: {OperationCategory.AdvancedCrafting, OperationCategory.BasicCrafting, OperationCategory.Crafting},
    AssemblingMachine.StoneFurnace: {OperationCategory.Smelting},
    AssemblingMachine.ElectricFurnace: {OperationCategory.Smelting},
    AssemblingMachine.SteelFurnace: {OperationCategory.Smelting},
    AssemblingMachine.Lab: set(),
    AssemblingMachine.BurnerMiningDrill: {OperationCategory.Mining},
    AssemblingMachine.ElectricMiningDrill: {OperationCategory.Mining},
    AssemblingMachine.Pumpjack: {OperationCategory.Mining},
}

ENERGY_USAGE_KW: dict[AssemblingMachine, Rational] = {
    AssemblingMachine.AssemblingMachine3: Integer(375),
    AssemblingMachine.Centrifuge: Integer(350),
    AssemblingMachine.ChemicalPlant: Integer(210),
    AssemblingMachine.AssemblingMachine2: Integer(150),
    AssemblingMachine.OilRefinery: Integer(420),
    AssemblingMachine.AssemblingMachine1: Integer(75),
    AssemblingMachine.StoneFurnace: Integer(90),
    AssemblingMachine.ElectricFurnace: Integer(180),
    AssemblingMachine.SteelFurnace: Integer(90),
    AssemblingMachine.Lab: Integer(60),
    AssemblingMachine.BurnerMiningDrill: Integer(150),
    AssemblingMachine.ElectricMiningDrill: Integer(90),
    AssemblingMachine.Pumpjack: Integer(90),
}

ALLOWED_EFFECTS: dict[AssemblingMachine, set[str]] = {
    AssemblingMachine.AssemblingMachine3: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.Centrifuge: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.ChemicalPlant: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.AssemblingMachine2: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.OilRefinery: {'consumption', 'pollution', 'productivity', 'speed'},
    AssemblingMachine.AssemblingMachine1: {'consumption', 'pollution', 'speed'},
    AssemblingMachine.StoneFurnace: {'consumption', 'pollution', 'speed'},
    AssemblingMachine.ElectricFurnace: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.SteelFurnace: {'consumption', 'pollution', 'speed'},
    AssemblingMachine.Lab: set(),
    AssemblingMachine.BurnerMiningDrill: set(),
    AssemblingMachine.ElectricMiningDrill: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.Pumpjack: {'consumption', 'pollution', 'productivity', 'speed'},
}

MODULE_SLOTS: dict[AssemblingMachine, int] = {
    AssemblingMachine.AssemblingMachine3: 4,
    AssemblingMachine.Centrifuge: 2,
    AssemblingMachine.ChemicalPlant: 3,
    AssemblingMachine.AssemblingMachine2: 2,
    AssemblingMachine.OilRefinery: 3,
    AssemblingMachine.AssemblingMachine1: 0,
    AssemblingMachine.StoneFurnace: 0,
    AssemblingMachine.ElectricFurnace: 2,
    AssemblingMachine.SteelFurnace: 0,
    AssemblingMachine.Lab: 2,
    AssemblingMachine.BurnerMiningDrill: 0,
    AssemblingMachine.ElectricMiningDrill: 3,
    AssemblingMachine.Pumpjack: 2,
}