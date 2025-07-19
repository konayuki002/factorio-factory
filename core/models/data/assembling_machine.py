from sympy import Integer, Rational
from core.enums.assembling_machine import AssemblingMachine
from core.enums.operation_category import OperationCategory

TYPES: dict[AssemblingMachine, str] = {
    AssemblingMachine.AssemblingMachine1: "assembling-machine",
    AssemblingMachine.AssemblingMachine2: "assembling-machine",
    AssemblingMachine.AssemblingMachine3: "assembling-machine",
    AssemblingMachine.BurnerMiningDrill: "mining-drill",
    AssemblingMachine.Centrifuge: "assembling-machine",
    AssemblingMachine.ChemicalPlant: "assembling-machine",
    AssemblingMachine.ElectricFurnace: "furnace",
    AssemblingMachine.ElectricMiningDrill: "mining-drill",
    AssemblingMachine.Lab: "lab",
    AssemblingMachine.OilRefinery: "assembling-machine",
    AssemblingMachine.Pumpjack: "mining-drill",
    AssemblingMachine.SteelFurnace: "furnace",
    AssemblingMachine.StoneFurnace: "furnace",
}

SPEED: dict[AssemblingMachine, Rational] = {
    AssemblingMachine.AssemblingMachine1: Rational(1, 2),
    AssemblingMachine.AssemblingMachine2: Rational(3, 4),
    AssemblingMachine.AssemblingMachine3: Rational(5, 4),
    AssemblingMachine.BurnerMiningDrill: Rational(1, 4),
    AssemblingMachine.Centrifuge: Integer(1),
    AssemblingMachine.ChemicalPlant: Integer(1),
    AssemblingMachine.ElectricFurnace: Integer(2),
    AssemblingMachine.ElectricMiningDrill: Rational(1, 2),
    AssemblingMachine.Lab: Integer(0),
    AssemblingMachine.OilRefinery: Integer(1),
    AssemblingMachine.Pumpjack: Integer(1),
    AssemblingMachine.SteelFurnace: Integer(2),
    AssemblingMachine.StoneFurnace: Integer(1),
}

CATEGORIES: dict[AssemblingMachine, set[OperationCategory]] = {
    AssemblingMachine.AssemblingMachine1: {OperationCategory.AdvancedCrafting, OperationCategory.BasicCrafting, OperationCategory.Crafting},
    AssemblingMachine.AssemblingMachine2: {OperationCategory.AdvancedCrafting, OperationCategory.BasicCrafting, OperationCategory.Crafting, OperationCategory.CraftingWithFluid},
    AssemblingMachine.AssemblingMachine3: {OperationCategory.AdvancedCrafting, OperationCategory.BasicCrafting, OperationCategory.Crafting, OperationCategory.CraftingWithFluid},
    AssemblingMachine.BurnerMiningDrill: {OperationCategory.Mining},
    AssemblingMachine.Centrifuge: {OperationCategory.Centrifuging},
    AssemblingMachine.ChemicalPlant: {OperationCategory.Chemistry},
    AssemblingMachine.ElectricFurnace: {OperationCategory.Smelting},
    AssemblingMachine.ElectricMiningDrill: {OperationCategory.Mining},
    AssemblingMachine.Lab: set(),
    AssemblingMachine.OilRefinery: {OperationCategory.OilProcessing},
    AssemblingMachine.Pumpjack: {OperationCategory.Mining},
    AssemblingMachine.SteelFurnace: {OperationCategory.Smelting},
    AssemblingMachine.StoneFurnace: {OperationCategory.Smelting},
}

ENERGY_USAGE_KW: dict[AssemblingMachine, Rational] = {
    AssemblingMachine.AssemblingMachine1: Integer(75),
    AssemblingMachine.AssemblingMachine2: Integer(150),
    AssemblingMachine.AssemblingMachine3: Integer(375),
    AssemblingMachine.BurnerMiningDrill: Integer(150),
    AssemblingMachine.Centrifuge: Integer(350),
    AssemblingMachine.ChemicalPlant: Integer(210),
    AssemblingMachine.ElectricFurnace: Integer(180),
    AssemblingMachine.ElectricMiningDrill: Integer(90),
    AssemblingMachine.Lab: Integer(60),
    AssemblingMachine.OilRefinery: Integer(420),
    AssemblingMachine.Pumpjack: Integer(90),
    AssemblingMachine.SteelFurnace: Integer(90),
    AssemblingMachine.StoneFurnace: Integer(90),
}

ALLOWED_EFFECTS: dict[AssemblingMachine, set[str]] = {
    AssemblingMachine.AssemblingMachine1: {'consumption', 'pollution', 'speed'},
    AssemblingMachine.AssemblingMachine2: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.AssemblingMachine3: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.BurnerMiningDrill: set(),
    AssemblingMachine.Centrifuge: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.ChemicalPlant: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.ElectricFurnace: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.ElectricMiningDrill: {'consumption', 'pollution', 'productivity', 'quality', 'speed'},
    AssemblingMachine.Lab: set(),
    AssemblingMachine.OilRefinery: {'consumption', 'pollution', 'productivity', 'speed'},
    AssemblingMachine.Pumpjack: {'consumption', 'pollution', 'productivity', 'speed'},
    AssemblingMachine.SteelFurnace: {'consumption', 'pollution', 'speed'},
    AssemblingMachine.StoneFurnace: {'consumption', 'pollution', 'speed'},
}

MODULE_SLOTS: dict[AssemblingMachine, int] = {
    AssemblingMachine.AssemblingMachine1: 0,
    AssemblingMachine.AssemblingMachine2: 2,
    AssemblingMachine.AssemblingMachine3: 4,
    AssemblingMachine.BurnerMiningDrill: 0,
    AssemblingMachine.Centrifuge: 2,
    AssemblingMachine.ChemicalPlant: 3,
    AssemblingMachine.ElectricFurnace: 2,
    AssemblingMachine.ElectricMiningDrill: 3,
    AssemblingMachine.Lab: 2,
    AssemblingMachine.OilRefinery: 3,
    AssemblingMachine.Pumpjack: 2,
    AssemblingMachine.SteelFurnace: 0,
    AssemblingMachine.StoneFurnace: 0,
}