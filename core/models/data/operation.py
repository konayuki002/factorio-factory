from sympy import Add, Expr, Integer, Mul, Pow, Symbol

from core.enums.material import Material
from core.enums.operation import Operation
from core.enums.operation_category import OperationCategory

L = Symbol("L")

INGREDIENTS: dict[Operation, dict[Material, Integer | Expr]] = {
    Operation.SpeedModule: {
        Material.AdvancedCircuit: Integer(5),
        Material.ElectronicCircuit: Integer(5),
    },
    Operation.SpeedModule2: {
        Material.SpeedModule: Integer(4),
        Material.AdvancedCircuit: Integer(5),
        Material.ProcessingUnit: Integer(5),
    },
    Operation.SpeedModule3: {
        Material.SpeedModule2: Integer(4),
        Material.AdvancedCircuit: Integer(5),
        Material.ProcessingUnit: Integer(5),
    },
    Operation.ProductivityModule: {
        Material.AdvancedCircuit: Integer(5),
        Material.ElectronicCircuit: Integer(5),
    },
    Operation.ProductivityModule2: {
        Material.ProductivityModule: Integer(4),
        Material.AdvancedCircuit: Integer(5),
        Material.ProcessingUnit: Integer(5),
    },
    Operation.ProductivityModule3: {
        Material.ProductivityModule2: Integer(4),
        Material.AdvancedCircuit: Integer(5),
        Material.ProcessingUnit: Integer(5),
    },
    Operation.EfficiencyModule: {
        Material.AdvancedCircuit: Integer(5),
        Material.ElectronicCircuit: Integer(5),
    },
    Operation.EfficiencyModule2: {
        Material.EfficiencyModule: Integer(4),
        Material.AdvancedCircuit: Integer(5),
        Material.ProcessingUnit: Integer(5),
    },
    Operation.EfficiencyModule3: {
        Material.EfficiencyModule2: Integer(4),
        Material.AdvancedCircuit: Integer(5),
        Material.ProcessingUnit: Integer(5),
    },
    Operation.BulkInserter: {
        Material.IronGearWheel: Integer(15),
        Material.ElectronicCircuit: Integer(15),
        Material.AdvancedCircuit: Integer(1),
        Material.FastInserter: Integer(1),
    },
    Operation.BasicOilProcessing: {Material.CrudeOil: Integer(100)},
    Operation.AdvancedOilProcessing: {
        Material.Water: Integer(50),
        Material.CrudeOil: Integer(100),
    },
    Operation.CoalLiquefaction: {
        Material.Coal: Integer(10),
        Material.HeavyOil: Integer(25),
        Material.Steam: Integer(50),
    },
    Operation.HeavyOilCracking: {
        Material.Water: Integer(30),
        Material.HeavyOil: Integer(40),
    },
    Operation.LightOilCracking: {
        Material.Water: Integer(30),
        Material.LightOil: Integer(30),
    },
    Operation.SulfuricAcid: {
        Material.Sulfur: Integer(5),
        Material.IronPlate: Integer(1),
        Material.Water: Integer(100),
    },
    Operation.PlasticBar: {
        Material.PetroleumGas: Integer(20),
        Material.Coal: Integer(1),
    },
    Operation.SolidFuelFromLightOil: {Material.LightOil: Integer(10)},
    Operation.SolidFuelFromPetroleumGas: {Material.PetroleumGas: Integer(20)},
    Operation.SolidFuelFromHeavyOil: {Material.HeavyOil: Integer(20)},
    Operation.Sulfur: {Material.Water: Integer(30), Material.PetroleumGas: Integer(30)},
    Operation.Lubricant: {Material.HeavyOil: Integer(10)},
    Operation.Barrel: {Material.SteelPlate: Integer(1)},
    Operation.NightVisionEquipment: {
        Material.AdvancedCircuit: Integer(5),
        Material.SteelPlate: Integer(10),
    },
    Operation.BeltImmunityEquipment: {
        Material.AdvancedCircuit: Integer(5),
        Material.SteelPlate: Integer(10),
    },
    Operation.EnergyShieldEquipment: {
        Material.AdvancedCircuit: Integer(5),
        Material.SteelPlate: Integer(10),
    },
    Operation.EnergyShieldMk2Equipment: {
        Material.EnergyShieldEquipment: Integer(10),
        Material.ProcessingUnit: Integer(5),
        Material.LowDensityStructure: Integer(5),
    },
    Operation.BatteryEquipment: {
        Material.Battery: Integer(5),
        Material.SteelPlate: Integer(10),
    },
    Operation.BatteryMk2Equipment: {
        Material.BatteryEquipment: Integer(10),
        Material.ProcessingUnit: Integer(15),
        Material.LowDensityStructure: Integer(5),
    },
    Operation.SolarPanelEquipment: {
        Material.SolarPanel: Integer(1),
        Material.AdvancedCircuit: Integer(2),
        Material.SteelPlate: Integer(5),
    },
    Operation.FissionReactorEquipment: {
        Material.ProcessingUnit: Integer(200),
        Material.LowDensityStructure: Integer(50),
        Material.UraniumFuelCell: Integer(4),
    },
    Operation.PersonalLaserDefenseEquipment: {
        Material.ProcessingUnit: Integer(20),
        Material.LowDensityStructure: Integer(5),
        Material.LaserTurret: Integer(5),
    },
    Operation.DischargeDefenseEquipment: {
        Material.ProcessingUnit: Integer(5),
        Material.SteelPlate: Integer(20),
        Material.LaserTurret: Integer(10),
    },
    Operation.ExoskeletonEquipment: {
        Material.ProcessingUnit: Integer(10),
        Material.ElectricEngineUnit: Integer(30),
        Material.SteelPlate: Integer(20),
    },
    Operation.PersonalRoboportEquipment: {
        Material.AdvancedCircuit: Integer(10),
        Material.IronGearWheel: Integer(40),
        Material.SteelPlate: Integer(20),
        Material.Battery: Integer(45),
    },
    Operation.PersonalRoboportMk2Equipment: {
        Material.PersonalRoboportEquipment: Integer(5),
        Material.ProcessingUnit: Integer(100),
        Material.LowDensityStructure: Integer(20),
    },
    Operation.LaserTurret: {
        Material.SteelPlate: Integer(20),
        Material.ElectronicCircuit: Integer(20),
        Material.Battery: Integer(12),
    },
    Operation.FlamethrowerTurret: {
        Material.SteelPlate: Integer(30),
        Material.IronGearWheel: Integer(15),
        Material.Pipe: Integer(10),
        Material.EngineUnit: Integer(5),
    },
    Operation.ArtilleryTurret: {
        Material.SteelPlate: Integer(60),
        Material.Concrete: Integer(60),
        Material.IronGearWheel: Integer(40),
        Material.AdvancedCircuit: Integer(20),
    },
    Operation.GunTurret: {
        Material.IronGearWheel: Integer(10),
        Material.CopperPlate: Integer(10),
        Material.IronPlate: Integer(20),
    },
    Operation.WoodenChest: {Material.Wood: Integer(2)},
    Operation.DisplayPanel: {
        Material.IronPlate: Integer(1),
        Material.ElectronicCircuit: Integer(1),
    },
    Operation.IronStick: {Material.IronPlate: Integer(1)},
    Operation.StoneFurnace: {Material.Stone: Integer(5)},
    Operation.Boiler: {Material.StoneFurnace: Integer(1), Material.Pipe: Integer(4)},
    Operation.SteamEngine: {
        Material.IronGearWheel: Integer(8),
        Material.Pipe: Integer(5),
        Material.IronPlate: Integer(10),
    },
    Operation.IronGearWheel: {Material.IronPlate: Integer(2)},
    Operation.ElectronicCircuit: {
        Material.IronPlate: Integer(1),
        Material.CopperCable: Integer(3),
    },
    Operation.TransportBelt: {
        Material.IronPlate: Integer(1),
        Material.IronGearWheel: Integer(1),
    },
    Operation.ElectricMiningDrill: {
        Material.ElectronicCircuit: Integer(3),
        Material.IronGearWheel: Integer(5),
        Material.IronPlate: Integer(10),
    },
    Operation.BurnerMiningDrill: {
        Material.IronGearWheel: Integer(3),
        Material.StoneFurnace: Integer(1),
        Material.IronPlate: Integer(3),
    },
    Operation.Inserter: {
        Material.ElectronicCircuit: Integer(1),
        Material.IronGearWheel: Integer(1),
        Material.IronPlate: Integer(1),
    },
    Operation.FastInserter: {
        Material.ElectronicCircuit: Integer(2),
        Material.IronPlate: Integer(2),
        Material.Inserter: Integer(1),
    },
    Operation.LongHandedInserter: {
        Material.IronGearWheel: Integer(1),
        Material.IronPlate: Integer(1),
        Material.Inserter: Integer(1),
    },
    Operation.BurnerInserter: {
        Material.IronPlate: Integer(1),
        Material.IronGearWheel: Integer(1),
    },
    Operation.Pipe: {Material.IronPlate: Integer(1)},
    Operation.OffshorePump: {
        Material.Pipe: Integer(3),
        Material.IronGearWheel: Integer(2),
    },
    Operation.CopperCable: {Material.CopperPlate: Integer(1)},
    Operation.SmallElectricPole: {
        Material.Wood: Integer(1),
        Material.CopperCable: Integer(2),
    },
    Operation.Pistol: {
        Material.CopperPlate: Integer(5),
        Material.IronPlate: Integer(5),
    },
    Operation.SubmachineGun: {
        Material.IronGearWheel: Integer(10),
        Material.CopperPlate: Integer(5),
        Material.IronPlate: Integer(10),
    },
    Operation.FirearmMagazine: {Material.IronPlate: Integer(4)},
    Operation.LightArmor: {Material.IronPlate: Integer(40)},
    Operation.Radar: {
        Material.ElectronicCircuit: Integer(5),
        Material.IronGearWheel: Integer(5),
        Material.IronPlate: Integer(10),
    },
    Operation.SmallLamp: {
        Material.ElectronicCircuit: Integer(1),
        Material.CopperCable: Integer(3),
        Material.IronPlate: Integer(1),
    },
    Operation.PipeToGround: {
        Material.Pipe: Integer(10),
        Material.IronPlate: Integer(5),
    },
    Operation.AssemblingMachine1: {
        Material.ElectronicCircuit: Integer(3),
        Material.IronGearWheel: Integer(5),
        Material.IronPlate: Integer(9),
    },
    Operation.RepairPack: {
        Material.ElectronicCircuit: Integer(2),
        Material.IronGearWheel: Integer(2),
    },
    Operation.AutomationSciencePack: {
        Material.CopperPlate: Integer(1),
        Material.IronGearWheel: Integer(1),
    },
    Operation.LogisticSciencePack: {
        Material.Inserter: Integer(1),
        Material.TransportBelt: Integer(1),
    },
    Operation.Lab: {
        Material.ElectronicCircuit: Integer(10),
        Material.IronGearWheel: Integer(10),
        Material.TransportBelt: Integer(4),
    },
    Operation.StoneWall: {Material.StoneBrick: Integer(5)},
    Operation.AssemblingMachine2: {
        Material.SteelPlate: Integer(2),
        Material.ElectronicCircuit: Integer(3),
        Material.IronGearWheel: Integer(5),
        Material.AssemblingMachine1: Integer(1),
    },
    Operation.Splitter: {
        Material.ElectronicCircuit: Integer(5),
        Material.IronPlate: Integer(5),
        Material.TransportBelt: Integer(4),
    },
    Operation.UndergroundBelt: {
        Material.IronPlate: Integer(10),
        Material.TransportBelt: Integer(5),
    },
    Operation.Loader: {
        Material.Inserter: Integer(5),
        Material.ElectronicCircuit: Integer(5),
        Material.IronGearWheel: Integer(5),
        Material.IronPlate: Integer(5),
        Material.TransportBelt: Integer(5),
    },
    Operation.Car: {
        Material.EngineUnit: Integer(8),
        Material.IronPlate: Integer(20),
        Material.SteelPlate: Integer(5),
    },
    Operation.EngineUnit: {
        Material.SteelPlate: Integer(1),
        Material.IronGearWheel: Integer(1),
        Material.Pipe: Integer(2),
    },
    Operation.IronChest: {Material.IronPlate: Integer(8)},
    Operation.BigElectricPole: {
        Material.IronStick: Integer(8),
        Material.SteelPlate: Integer(5),
        Material.CopperCable: Integer(4),
    },
    Operation.MediumElectricPole: {
        Material.IronStick: Integer(4),
        Material.SteelPlate: Integer(2),
        Material.CopperCable: Integer(2),
    },
    Operation.Shotgun: {
        Material.IronPlate: Integer(15),
        Material.IronGearWheel: Integer(5),
        Material.CopperPlate: Integer(10),
        Material.Wood: Integer(5),
    },
    Operation.ShotgunShell: {
        Material.CopperPlate: Integer(2),
        Material.IronPlate: Integer(2),
    },
    Operation.PiercingRoundsMagazine: {
        Material.FirearmMagazine: Integer(2),
        Material.SteelPlate: Integer(1),
        Material.CopperPlate: Integer(2),
    },
    Operation.Grenade: {Material.IronPlate: Integer(5), Material.Coal: Integer(10)},
    Operation.SteelFurnace: {
        Material.SteelPlate: Integer(6),
        Material.StoneBrick: Integer(10),
    },
    Operation.Gate: {
        Material.StoneWall: Integer(1),
        Material.SteelPlate: Integer(2),
        Material.ElectronicCircuit: Integer(2),
    },
    Operation.HeavyArmor: {
        Material.CopperPlate: Integer(100),
        Material.SteelPlate: Integer(50),
    },
    Operation.SteelChest: {Material.SteelPlate: Integer(8)},
    Operation.FastUndergroundBelt: {
        Material.IronGearWheel: Integer(40),
        Material.UndergroundBelt: Integer(2),
    },
    Operation.FastSplitter: {
        Material.Splitter: Integer(1),
        Material.IronGearWheel: Integer(10),
        Material.ElectronicCircuit: Integer(10),
    },
    Operation.Concrete: {
        Material.StoneBrick: Integer(5),
        Material.IronOre: Integer(1),
        Material.Water: Integer(100),
    },
    Operation.HazardConcrete: {Material.Concrete: Integer(10)},
    Operation.RefinedConcrete: {
        Material.Concrete: Integer(20),
        Material.IronStick: Integer(8),
        Material.SteelPlate: Integer(1),
        Material.Water: Integer(100),
    },
    Operation.RefinedHazardConcrete: {Material.RefinedConcrete: Integer(10)},
    Operation.Landfill: {Material.Stone: Integer(50)},
    Operation.FastTransportBelt: {
        Material.IronGearWheel: Integer(5),
        Material.TransportBelt: Integer(1),
    },
    Operation.SolarPanel: {
        Material.SteelPlate: Integer(5),
        Material.ElectronicCircuit: Integer(15),
        Material.CopperPlate: Integer(5),
    },
    Operation.Rail: {
        Material.Stone: Integer(1),
        Material.IronStick: Integer(1),
        Material.SteelPlate: Integer(1),
    },
    Operation.Locomotive: {
        Material.EngineUnit: Integer(20),
        Material.ElectronicCircuit: Integer(10),
        Material.SteelPlate: Integer(30),
    },
    Operation.CargoWagon: {
        Material.IronGearWheel: Integer(10),
        Material.IronPlate: Integer(20),
        Material.SteelPlate: Integer(20),
    },
    Operation.RailSignal: {
        Material.ElectronicCircuit: Integer(1),
        Material.IronPlate: Integer(5),
    },
    Operation.RailChainSignal: {
        Material.ElectronicCircuit: Integer(1),
        Material.IronPlate: Integer(5),
    },
    Operation.TrainStop: {
        Material.ElectronicCircuit: Integer(5),
        Material.IronPlate: Integer(6),
        Material.IronStick: Integer(6),
        Material.SteelPlate: Integer(3),
    },
    Operation.CopperPlate: {Material.CopperOre: Integer(1)},
    Operation.IronPlate: {Material.IronOre: Integer(1)},
    Operation.StoneBrick: {Material.Stone: Integer(2)},
    Operation.SteelPlate: {Material.IronPlate: Integer(5)},
    Operation.ArithmeticCombinator: {
        Material.CopperCable: Integer(5),
        Material.ElectronicCircuit: Integer(5),
    },
    Operation.DeciderCombinator: {
        Material.CopperCable: Integer(5),
        Material.ElectronicCircuit: Integer(5),
    },
    Operation.ConstantCombinator: {
        Material.CopperCable: Integer(5),
        Material.ElectronicCircuit: Integer(2),
    },
    Operation.SelectorCombinator: {
        Material.AdvancedCircuit: Integer(2),
        Material.DeciderCombinator: Integer(5),
    },
    Operation.PowerSwitch: {
        Material.IronPlate: Integer(5),
        Material.CopperCable: Integer(5),
        Material.ElectronicCircuit: Integer(2),
    },
    Operation.ProgrammableSpeaker: {
        Material.IronPlate: Integer(3),
        Material.IronStick: Integer(4),
        Material.CopperCable: Integer(5),
        Material.ElectronicCircuit: Integer(4),
    },
    Operation.PoisonCapsule: {
        Material.SteelPlate: Integer(3),
        Material.ElectronicCircuit: Integer(3),
        Material.Coal: Integer(10),
    },
    Operation.SlowdownCapsule: {
        Material.SteelPlate: Integer(2),
        Material.ElectronicCircuit: Integer(2),
        Material.Coal: Integer(5),
    },
    Operation.ClusterGrenade: {
        Material.Grenade: Integer(7),
        Material.Explosives: Integer(5),
        Material.SteelPlate: Integer(5),
    },
    Operation.DefenderCapsule: {
        Material.PiercingRoundsMagazine: Integer(3),
        Material.ElectronicCircuit: Integer(3),
        Material.IronGearWheel: Integer(3),
    },
    Operation.DistractorCapsule: {
        Material.DefenderCapsule: Integer(4),
        Material.AdvancedCircuit: Integer(3),
    },
    Operation.DestroyerCapsule: {
        Material.DistractorCapsule: Integer(4),
        Material.SpeedModule: Integer(1),
    },
    Operation.CliffExplosives: {
        Material.Explosives: Integer(10),
        Material.Grenade: Integer(1),
        Material.Barrel: Integer(1),
    },
    Operation.UraniumRoundsMagazine: {
        Material.PiercingRoundsMagazine: Integer(1),
        Material.Uranium238: Integer(1),
    },
    Operation.Rocket: {Material.Explosives: Integer(1), Material.IronPlate: Integer(2)},
    Operation.ExplosiveRocket: {
        Material.Rocket: Integer(1),
        Material.Explosives: Integer(2),
    },
    Operation.AtomicBomb: {
        Material.ProcessingUnit: Integer(10),
        Material.Explosives: Integer(10),
        Material.Uranium235: Integer(30),
    },
    Operation.PiercingShotgunShell: {
        Material.ShotgunShell: Integer(2),
        Material.CopperPlate: Integer(5),
        Material.SteelPlate: Integer(2),
    },
    Operation.CannonShell: {
        Material.SteelPlate: Integer(2),
        Material.PlasticBar: Integer(2),
        Material.Explosives: Integer(1),
    },
    Operation.ExplosiveCannonShell: {
        Material.SteelPlate: Integer(2),
        Material.PlasticBar: Integer(2),
        Material.Explosives: Integer(2),
    },
    Operation.UraniumCannonShell: {
        Material.CannonShell: Integer(1),
        Material.Uranium238: Integer(1),
    },
    Operation.ExplosiveUraniumCannonShell: {
        Material.ExplosiveCannonShell: Integer(1),
        Material.Uranium238: Integer(1),
    },
    Operation.ArtilleryShell: {
        Material.ExplosiveCannonShell: Integer(4),
        Material.Radar: Integer(1),
        Material.Explosives: Integer(8),
    },
    Operation.FlamethrowerAmmo: {
        Material.SteelPlate: Integer(5),
        Material.CrudeOil: Integer(100),
    },
    Operation.ExpressTransportBelt: {
        Material.IronGearWheel: Integer(10),
        Material.FastTransportBelt: Integer(1),
        Material.Lubricant: Integer(20),
    },
    Operation.AssemblingMachine3: {
        Material.SpeedModule: Integer(4),
        Material.AssemblingMachine2: Integer(2),
    },
    Operation.Tank: {
        Material.EngineUnit: Integer(32),
        Material.SteelPlate: Integer(50),
        Material.IronGearWheel: Integer(15),
        Material.AdvancedCircuit: Integer(10),
    },
    Operation.Spidertron: {
        Material.ExoskeletonEquipment: Integer(4),
        Material.FissionReactorEquipment: Integer(2),
        Material.RocketLauncher: Integer(4),
        Material.ProcessingUnit: Integer(16),
        Material.LowDensityStructure: Integer(150),
        Material.Radar: Integer(2),
        Material.EfficiencyModule3: Integer(2),
        Material.RawFish: Integer(1),
    },
    Operation.FluidWagon: {
        Material.IronGearWheel: Integer(10),
        Material.SteelPlate: Integer(16),
        Material.Pipe: Integer(8),
        Material.StorageTank: Integer(1),
    },
    Operation.ArtilleryWagon: {
        Material.EngineUnit: Integer(64),
        Material.IronGearWheel: Integer(10),
        Material.SteelPlate: Integer(40),
        Material.Pipe: Integer(16),
        Material.AdvancedCircuit: Integer(20),
    },
    Operation.ModularArmor: {
        Material.AdvancedCircuit: Integer(30),
        Material.SteelPlate: Integer(50),
    },
    Operation.PowerArmor: {
        Material.ProcessingUnit: Integer(40),
        Material.ElectricEngineUnit: Integer(20),
        Material.SteelPlate: Integer(40),
    },
    Operation.PowerArmorMk2: {
        Material.EfficiencyModule2: Integer(25),
        Material.SpeedModule2: Integer(25),
        Material.ProcessingUnit: Integer(60),
        Material.ElectricEngineUnit: Integer(40),
        Material.LowDensityStructure: Integer(30),
    },
    Operation.Flamethrower: {
        Material.SteelPlate: Integer(5),
        Material.IronGearWheel: Integer(10),
    },
    Operation.LandMine: {
        Material.SteelPlate: Integer(1),
        Material.Explosives: Integer(2),
    },
    Operation.RocketLauncher: {
        Material.IronPlate: Integer(5),
        Material.IronGearWheel: Integer(5),
        Material.ElectronicCircuit: Integer(5),
    },
    Operation.CombatShotgun: {
        Material.SteelPlate: Integer(15),
        Material.IronGearWheel: Integer(5),
        Material.CopperPlate: Integer(10),
        Material.Wood: Integer(10),
    },
    Operation.ChemicalSciencePack: {
        Material.EngineUnit: Integer(2),
        Material.AdvancedCircuit: Integer(3),
        Material.Sulfur: Integer(1),
    },
    Operation.MilitarySciencePack: {
        Material.PiercingRoundsMagazine: Integer(1),
        Material.Grenade: Integer(1),
        Material.StoneWall: Integer(2),
    },
    Operation.ProductionSciencePack: {
        Material.ElectricFurnace: Integer(1),
        Material.ProductivityModule: Integer(1),
        Material.Rail: Integer(30),
    },
    Operation.UtilitySciencePack: {
        Material.LowDensityStructure: Integer(3),
        Material.ProcessingUnit: Integer(2),
        Material.FlyingRobotFrame: Integer(1),
    },
    Operation.ExpressUndergroundBelt: {
        Material.IronGearWheel: Integer(80),
        Material.FastUndergroundBelt: Integer(2),
        Material.Lubricant: Integer(40),
    },
    Operation.FastLoader: {
        Material.FastTransportBelt: Integer(5),
        Material.Loader: Integer(1),
    },
    Operation.ExpressLoader: {
        Material.ExpressTransportBelt: Integer(5),
        Material.FastLoader: Integer(1),
    },
    Operation.ExpressSplitter: {
        Material.FastSplitter: Integer(1),
        Material.IronGearWheel: Integer(10),
        Material.AdvancedCircuit: Integer(10),
        Material.Lubricant: Integer(80),
    },
    Operation.AdvancedCircuit: {
        Material.ElectronicCircuit: Integer(2),
        Material.PlasticBar: Integer(2),
        Material.CopperCable: Integer(4),
    },
    Operation.ProcessingUnit: {
        Material.ElectronicCircuit: Integer(20),
        Material.AdvancedCircuit: Integer(2),
        Material.SulfuricAcid: Integer(5),
    },
    Operation.LogisticRobot: {
        Material.FlyingRobotFrame: Integer(1),
        Material.AdvancedCircuit: Integer(2),
    },
    Operation.ConstructionRobot: {
        Material.FlyingRobotFrame: Integer(1),
        Material.ElectronicCircuit: Integer(2),
    },
    Operation.PassiveProviderChest: {
        Material.SteelChest: Integer(1),
        Material.ElectronicCircuit: Integer(3),
        Material.AdvancedCircuit: Integer(1),
    },
    Operation.ActiveProviderChest: {
        Material.SteelChest: Integer(1),
        Material.ElectronicCircuit: Integer(3),
        Material.AdvancedCircuit: Integer(1),
    },
    Operation.StorageChest: {
        Material.SteelChest: Integer(1),
        Material.ElectronicCircuit: Integer(3),
        Material.AdvancedCircuit: Integer(1),
    },
    Operation.BufferChest: {
        Material.SteelChest: Integer(1),
        Material.ElectronicCircuit: Integer(3),
        Material.AdvancedCircuit: Integer(1),
    },
    Operation.RequesterChest: {
        Material.SteelChest: Integer(1),
        Material.ElectronicCircuit: Integer(3),
        Material.AdvancedCircuit: Integer(1),
    },
    Operation.RocketSilo: {
        Material.SteelPlate: Integer(1000),
        Material.Concrete: Integer(1000),
        Material.Pipe: Integer(100),
        Material.ProcessingUnit: Integer(200),
        Material.ElectricEngineUnit: Integer(200),
    },
    Operation.CargoLandingPad: {
        Material.Concrete: Integer(200),
        Material.SteelPlate: Integer(25),
        Material.ProcessingUnit: Integer(10),
    },
    Operation.Roboport: {
        Material.SteelPlate: Integer(45),
        Material.IronGearWheel: Integer(45),
        Material.AdvancedCircuit: Integer(45),
    },
    Operation.Substation: {
        Material.SteelPlate: Integer(10),
        Material.AdvancedCircuit: Integer(5),
        Material.CopperCable: Integer(6),
    },
    Operation.Accumulator: {
        Material.IronPlate: Integer(2),
        Material.Battery: Integer(5),
    },
    Operation.ElectricFurnace: {
        Material.SteelPlate: Integer(10),
        Material.AdvancedCircuit: Integer(5),
        Material.StoneBrick: Integer(10),
    },
    Operation.Beacon: {
        Material.ElectronicCircuit: Integer(20),
        Material.AdvancedCircuit: Integer(20),
        Material.SteelPlate: Integer(10),
        Material.CopperCable: Integer(10),
    },
    Operation.Pumpjack: {
        Material.SteelPlate: Integer(5),
        Material.IronGearWheel: Integer(10),
        Material.ElectronicCircuit: Integer(5),
        Material.Pipe: Integer(10),
    },
    Operation.OilRefinery: {
        Material.SteelPlate: Integer(15),
        Material.IronGearWheel: Integer(10),
        Material.StoneBrick: Integer(10),
        Material.ElectronicCircuit: Integer(10),
        Material.Pipe: Integer(10),
    },
    Operation.ElectricEngineUnit: {
        Material.EngineUnit: Integer(1),
        Material.Lubricant: Integer(15),
        Material.ElectronicCircuit: Integer(2),
    },
    Operation.FlyingRobotFrame: {
        Material.ElectricEngineUnit: Integer(1),
        Material.Battery: Integer(2),
        Material.SteelPlate: Integer(1),
        Material.ElectronicCircuit: Integer(3),
    },
    Operation.Explosives: {
        Material.Sulfur: Integer(1),
        Material.Coal: Integer(1),
        Material.Water: Integer(10),
    },
    Operation.Battery: {
        Material.SulfuricAcid: Integer(20),
        Material.IronPlate: Integer(1),
        Material.CopperPlate: Integer(1),
    },
    Operation.StorageTank: {
        Material.IronPlate: Integer(20),
        Material.SteelPlate: Integer(5),
    },
    Operation.Pump: {
        Material.EngineUnit: Integer(1),
        Material.SteelPlate: Integer(1),
        Material.Pipe: Integer(1),
    },
    Operation.ChemicalPlant: {
        Material.SteelPlate: Integer(5),
        Material.IronGearWheel: Integer(5),
        Material.ElectronicCircuit: Integer(5),
        Material.Pipe: Integer(5),
    },
    Operation.LowDensityStructure: {
        Material.SteelPlate: Integer(2),
        Material.CopperPlate: Integer(20),
        Material.PlasticBar: Integer(5),
    },
    Operation.RocketFuel: {
        Material.SolidFuel: Integer(10),
        Material.LightOil: Integer(10),
    },
    Operation.RocketPart: {
        Material.ProcessingUnit: Integer(10),
        Material.LowDensityStructure: Integer(10),
        Material.RocketFuel: Integer(10),
    },
    Operation.Satellite: {
        Material.LowDensityStructure: Integer(100),
        Material.SolarPanel: Integer(100),
        Material.Accumulator: Integer(100),
        Material.Radar: Integer(5),
        Material.ProcessingUnit: Integer(100),
        Material.RocketFuel: Integer(50),
    },
    Operation.NuclearReactor: {
        Material.Concrete: Integer(500),
        Material.SteelPlate: Integer(500),
        Material.AdvancedCircuit: Integer(500),
        Material.CopperPlate: Integer(500),
    },
    Operation.Centrifuge: {
        Material.Concrete: Integer(100),
        Material.SteelPlate: Integer(50),
        Material.AdvancedCircuit: Integer(100),
        Material.IronGearWheel: Integer(100),
    },
    Operation.UraniumProcessing: {Material.UraniumOre: Integer(10)},
    Operation.KovarexEnrichmentProcess: {
        Material.Uranium235: Integer(40),
        Material.Uranium238: Integer(5),
    },
    Operation.NuclearFuel: {
        Material.Uranium235: Integer(1),
        Material.RocketFuel: Integer(1),
    },
    Operation.NuclearFuelReprocessing: {Material.DepletedUraniumFuelCell: Integer(5)},
    Operation.UraniumFuelCell: {
        Material.IronPlate: Integer(10),
        Material.Uranium235: Integer(1),
        Material.Uranium238: Integer(19),
    },
    Operation.HeatExchanger: {
        Material.SteelPlate: Integer(10),
        Material.CopperPlate: Integer(100),
        Material.Pipe: Integer(10),
    },
    Operation.HeatPipe: {
        Material.SteelPlate: Integer(10),
        Material.CopperPlate: Integer(20),
    },
    Operation.SteamTurbine: {
        Material.IronGearWheel: Integer(50),
        Material.CopperPlate: Integer(50),
        Material.Pipe: Integer(20),
    },
    Operation.ResearchSteamPower: {},
    Operation.ResearchElectronics: {},
    Operation.ResearchAutomationSciencePack: {},
    Operation.ResearchElectricMiningDrill: {
        Material.AutomationSciencePack: Integer(25)
    },
    Operation.ResearchRepairPack: {Material.AutomationSciencePack: Integer(25)},
    Operation.ResearchRadar: {Material.AutomationSciencePack: Integer(20)},
    Operation.ResearchPhysicalProjectileDamage1: {
        Material.AutomationSciencePack: Integer(100)
    },
    Operation.ResearchPhysicalProjectileDamage2: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
    },
    Operation.ResearchWeaponShootingSpeed1: {
        Material.AutomationSciencePack: Integer(100)
    },
    Operation.ResearchWeaponShootingSpeed2: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
    },
    Operation.ResearchStrongerExplosives1: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
    },
    Operation.ResearchPhysicalProjectileDamage3: {
        Material.AutomationSciencePack: Integer(300),
        Material.LogisticSciencePack: Integer(300),
        Material.MilitarySciencePack: Integer(300),
    },
    Operation.ResearchPhysicalProjectileDamage4: {
        Material.AutomationSciencePack: Integer(400),
        Material.LogisticSciencePack: Integer(400),
        Material.MilitarySciencePack: Integer(400),
    },
    Operation.ResearchPhysicalProjectileDamage5: {
        Material.AutomationSciencePack: Integer(500),
        Material.LogisticSciencePack: Integer(500),
        Material.ChemicalSciencePack: Integer(500),
        Material.MilitarySciencePack: Integer(500),
    },
    Operation.ResearchPhysicalProjectileDamage6: {
        Material.AutomationSciencePack: Integer(600),
        Material.LogisticSciencePack: Integer(600),
        Material.ChemicalSciencePack: Integer(600),
        Material.MilitarySciencePack: Integer(600),
        Material.UtilitySciencePack: Integer(600),
    },
    Operation.ResearchPhysicalProjectileDamage7: {
        Material.AutomationSciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
        Material.LogisticSciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
        Material.ChemicalSciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
        Material.MilitarySciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
        Material.UtilitySciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
        Material.SpaceSciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
    },
    Operation.ResearchStrongerExplosives2: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
        Material.MilitarySciencePack: Integer(200),
    },
    Operation.ResearchStrongerExplosives3: {
        Material.AutomationSciencePack: Integer(300),
        Material.LogisticSciencePack: Integer(300),
        Material.MilitarySciencePack: Integer(300),
        Material.ChemicalSciencePack: Integer(300),
    },
    Operation.ResearchStrongerExplosives4: {
        Material.AutomationSciencePack: Integer(400),
        Material.LogisticSciencePack: Integer(400),
        Material.MilitarySciencePack: Integer(400),
        Material.ChemicalSciencePack: Integer(400),
        Material.UtilitySciencePack: Integer(400),
    },
    Operation.ResearchStrongerExplosives5: {
        Material.AutomationSciencePack: Integer(500),
        Material.LogisticSciencePack: Integer(500),
        Material.MilitarySciencePack: Integer(500),
        Material.ChemicalSciencePack: Integer(500),
        Material.UtilitySciencePack: Integer(500),
    },
    Operation.ResearchStrongerExplosives6: {
        Material.AutomationSciencePack: Integer(600),
        Material.LogisticSciencePack: Integer(600),
        Material.ChemicalSciencePack: Integer(600),
        Material.MilitarySciencePack: Integer(600),
        Material.UtilitySciencePack: Integer(600),
    },
    Operation.ResearchStrongerExplosives7: {
        Material.AutomationSciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
        Material.LogisticSciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
        Material.ChemicalSciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
        Material.MilitarySciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
        Material.UtilitySciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
        Material.SpaceSciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
    },
    Operation.ResearchRefinedFlammables1: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
        Material.MilitarySciencePack: Integer(100),
    },
    Operation.ResearchRefinedFlammables2: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
        Material.MilitarySciencePack: Integer(200),
    },
    Operation.ResearchRefinedFlammables3: {
        Material.AutomationSciencePack: Integer(300),
        Material.LogisticSciencePack: Integer(300),
        Material.MilitarySciencePack: Integer(300),
        Material.ChemicalSciencePack: Integer(300),
    },
    Operation.ResearchRefinedFlammables4: {
        Material.AutomationSciencePack: Integer(400),
        Material.LogisticSciencePack: Integer(400),
        Material.MilitarySciencePack: Integer(400),
        Material.ChemicalSciencePack: Integer(400),
        Material.UtilitySciencePack: Integer(400),
    },
    Operation.ResearchRefinedFlammables5: {
        Material.AutomationSciencePack: Integer(500),
        Material.LogisticSciencePack: Integer(500),
        Material.MilitarySciencePack: Integer(500),
        Material.ChemicalSciencePack: Integer(500),
        Material.UtilitySciencePack: Integer(500),
    },
    Operation.ResearchRefinedFlammables6: {
        Material.AutomationSciencePack: Integer(600),
        Material.LogisticSciencePack: Integer(600),
        Material.ChemicalSciencePack: Integer(600),
        Material.MilitarySciencePack: Integer(600),
        Material.UtilitySciencePack: Integer(600),
    },
    Operation.ResearchRefinedFlammables7: {
        Material.AutomationSciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
        Material.LogisticSciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
        Material.ChemicalSciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
        Material.MilitarySciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
        Material.UtilitySciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
        Material.SpaceSciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
    },
    Operation.ResearchLaserWeaponsDamage1: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
        Material.MilitarySciencePack: Integer(100),
        Material.ChemicalSciencePack: Integer(100),
    },
    Operation.ResearchLaserWeaponsDamage2: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
        Material.MilitarySciencePack: Integer(200),
        Material.ChemicalSciencePack: Integer(200),
    },
    Operation.ResearchLaserWeaponsDamage3: {
        Material.AutomationSciencePack: Integer(300),
        Material.LogisticSciencePack: Integer(300),
        Material.MilitarySciencePack: Integer(300),
        Material.ChemicalSciencePack: Integer(300),
    },
    Operation.ResearchLaserWeaponsDamage4: {
        Material.AutomationSciencePack: Integer(400),
        Material.LogisticSciencePack: Integer(400),
        Material.MilitarySciencePack: Integer(400),
        Material.ChemicalSciencePack: Integer(400),
    },
    Operation.ResearchLaserWeaponsDamage5: {
        Material.AutomationSciencePack: Integer(500),
        Material.LogisticSciencePack: Integer(500),
        Material.ChemicalSciencePack: Integer(500),
        Material.MilitarySciencePack: Integer(500),
        Material.UtilitySciencePack: Integer(500),
    },
    Operation.ResearchLaserWeaponsDamage6: {
        Material.AutomationSciencePack: Integer(600),
        Material.LogisticSciencePack: Integer(600),
        Material.ChemicalSciencePack: Integer(600),
        Material.MilitarySciencePack: Integer(600),
        Material.UtilitySciencePack: Integer(600),
    },
    Operation.ResearchLaserWeaponsDamage7: {
        Material.AutomationSciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
        Material.LogisticSciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
        Material.ChemicalSciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
        Material.MilitarySciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
        Material.UtilitySciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
        Material.SpaceSciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-7)))
        ),
    },
    Operation.ResearchWeaponShootingSpeed3: {
        Material.AutomationSciencePack: Integer(300),
        Material.LogisticSciencePack: Integer(300),
        Material.MilitarySciencePack: Integer(300),
    },
    Operation.ResearchWeaponShootingSpeed4: {
        Material.AutomationSciencePack: Integer(400),
        Material.LogisticSciencePack: Integer(400),
        Material.MilitarySciencePack: Integer(400),
    },
    Operation.ResearchWeaponShootingSpeed5: {
        Material.AutomationSciencePack: Integer(500),
        Material.LogisticSciencePack: Integer(500),
        Material.ChemicalSciencePack: Integer(500),
        Material.MilitarySciencePack: Integer(500),
    },
    Operation.ResearchWeaponShootingSpeed6: {
        Material.AutomationSciencePack: Integer(600),
        Material.LogisticSciencePack: Integer(600),
        Material.ChemicalSciencePack: Integer(600),
        Material.MilitarySciencePack: Integer(600),
        Material.UtilitySciencePack: Integer(600),
    },
    Operation.ResearchLaserShootingSpeed1: {
        Material.AutomationSciencePack: Integer(50),
        Material.LogisticSciencePack: Integer(50),
        Material.MilitarySciencePack: Integer(50),
        Material.ChemicalSciencePack: Integer(50),
    },
    Operation.ResearchLaserShootingSpeed2: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
        Material.MilitarySciencePack: Integer(100),
        Material.ChemicalSciencePack: Integer(100),
    },
    Operation.ResearchLaserShootingSpeed3: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
        Material.ChemicalSciencePack: Integer(200),
        Material.MilitarySciencePack: Integer(200),
    },
    Operation.ResearchLaserShootingSpeed4: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
        Material.ChemicalSciencePack: Integer(200),
        Material.MilitarySciencePack: Integer(200),
    },
    Operation.ResearchLaserShootingSpeed5: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
        Material.ChemicalSciencePack: Integer(200),
        Material.MilitarySciencePack: Integer(200),
        Material.UtilitySciencePack: Integer(200),
    },
    Operation.ResearchLaserShootingSpeed6: {
        Material.AutomationSciencePack: Integer(350),
        Material.LogisticSciencePack: Integer(350),
        Material.ChemicalSciencePack: Integer(350),
        Material.MilitarySciencePack: Integer(350),
        Material.UtilitySciencePack: Integer(350),
    },
    Operation.ResearchLaserShootingSpeed7: {
        Material.AutomationSciencePack: Integer(450),
        Material.LogisticSciencePack: Integer(450),
        Material.ChemicalSciencePack: Integer(450),
        Material.MilitarySciencePack: Integer(450),
        Material.UtilitySciencePack: Integer(450),
    },
    Operation.ResearchArtilleryShellRange1: {
        Material.AutomationSciencePack: Mul(Integer(1000), Pow(Integer(2), L)),
        Material.LogisticSciencePack: Mul(Integer(1000), Pow(Integer(2), L)),
        Material.ChemicalSciencePack: Mul(Integer(1000), Pow(Integer(2), L)),
        Material.MilitarySciencePack: Mul(Integer(1000), Pow(Integer(2), L)),
        Material.UtilitySciencePack: Mul(Integer(1000), Pow(Integer(2), L)),
        Material.SpaceSciencePack: Mul(Integer(1000), Pow(Integer(2), L)),
    },
    Operation.ResearchArtilleryShellSpeed1: {
        Material.AutomationSciencePack: Add(
            Mul(Integer(1000), Pow(Integer(3), Add(L, Integer(-1)))), Integer(1000)
        ),
        Material.LogisticSciencePack: Add(
            Mul(Integer(1000), Pow(Integer(3), Add(L, Integer(-1)))), Integer(1000)
        ),
        Material.ChemicalSciencePack: Add(
            Mul(Integer(1000), Pow(Integer(3), Add(L, Integer(-1)))), Integer(1000)
        ),
        Material.MilitarySciencePack: Add(
            Mul(Integer(1000), Pow(Integer(3), Add(L, Integer(-1)))), Integer(1000)
        ),
        Material.UtilitySciencePack: Add(
            Mul(Integer(1000), Pow(Integer(3), Add(L, Integer(-1)))), Integer(1000)
        ),
        Material.SpaceSciencePack: Add(
            Mul(Integer(1000), Pow(Integer(3), Add(L, Integer(-1)))), Integer(1000)
        ),
    },
    Operation.ResearchFollowerRobotCount5: {
        Material.AutomationSciencePack: Add(Mul(Integer(1000), L), Integer(-4000)),
        Material.LogisticSciencePack: Add(Mul(Integer(1000), L), Integer(-4000)),
        Material.ChemicalSciencePack: Add(Mul(Integer(1000), L), Integer(-4000)),
        Material.MilitarySciencePack: Add(Mul(Integer(1000), L), Integer(-4000)),
        Material.ProductionSciencePack: Add(Mul(Integer(1000), L), Integer(-4000)),
        Material.UtilitySciencePack: Add(Mul(Integer(1000), L), Integer(-4000)),
        Material.SpaceSciencePack: Add(Mul(Integer(1000), L), Integer(-4000)),
    },
    Operation.ResearchBulkInserter: {
        Material.AutomationSciencePack: Integer(150),
        Material.LogisticSciencePack: Integer(150),
    },
    Operation.ResearchInserterCapacityBonus1: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
    },
    Operation.ResearchInserterCapacityBonus2: {
        Material.AutomationSciencePack: Integer(250),
        Material.LogisticSciencePack: Integer(250),
    },
    Operation.ResearchInserterCapacityBonus3: {
        Material.AutomationSciencePack: Integer(250),
        Material.LogisticSciencePack: Integer(250),
        Material.ChemicalSciencePack: Integer(250),
    },
    Operation.ResearchInserterCapacityBonus4: {
        Material.AutomationSciencePack: Integer(250),
        Material.LogisticSciencePack: Integer(250),
        Material.ChemicalSciencePack: Integer(250),
        Material.ProductionSciencePack: Integer(250),
    },
    Operation.ResearchInserterCapacityBonus5: {
        Material.AutomationSciencePack: Integer(300),
        Material.LogisticSciencePack: Integer(300),
        Material.ChemicalSciencePack: Integer(300),
        Material.ProductionSciencePack: Integer(300),
    },
    Operation.ResearchInserterCapacityBonus6: {
        Material.AutomationSciencePack: Integer(400),
        Material.LogisticSciencePack: Integer(400),
        Material.ChemicalSciencePack: Integer(400),
        Material.ProductionSciencePack: Integer(400),
    },
    Operation.ResearchInserterCapacityBonus7: {
        Material.AutomationSciencePack: Integer(600),
        Material.LogisticSciencePack: Integer(600),
        Material.ChemicalSciencePack: Integer(600),
        Material.ProductionSciencePack: Integer(600),
        Material.UtilitySciencePack: Integer(600),
    },
    Operation.ResearchAutomation: {Material.AutomationSciencePack: Integer(10)},
    Operation.ResearchAutomation2: {
        Material.AutomationSciencePack: Integer(40),
        Material.LogisticSciencePack: Integer(40),
    },
    Operation.ResearchLogisticSciencePack: {
        Material.AutomationSciencePack: Integer(75)
    },
    Operation.ResearchSteelProcessing: {Material.AutomationSciencePack: Integer(50)},
    Operation.ResearchSteelAxe: {},
    Operation.ResearchMilitary: {Material.AutomationSciencePack: Integer(10)},
    Operation.ResearchMilitary2: {
        Material.AutomationSciencePack: Integer(20),
        Material.LogisticSciencePack: Integer(20),
    },
    Operation.ResearchFastInserter: {Material.AutomationSciencePack: Integer(30)},
    Operation.ResearchLogistics: {Material.AutomationSciencePack: Integer(20)},
    Operation.ResearchRailway: {
        Material.AutomationSciencePack: Integer(75),
        Material.LogisticSciencePack: Integer(75),
    },
    Operation.ResearchAutomatedRailTransportation: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
    },
    Operation.ResearchAutomobilism: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
    },
    Operation.ResearchLamp: {Material.AutomationSciencePack: Integer(10)},
    Operation.ResearchSolarEnergy: {
        Material.AutomationSciencePack: Integer(250),
        Material.LogisticSciencePack: Integer(250),
    },
    Operation.ResearchHeavyArmor: {Material.AutomationSciencePack: Integer(30)},
    Operation.ResearchGunTurret: {Material.AutomationSciencePack: Integer(10)},
    Operation.ResearchResearchSpeed1: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
    },
    Operation.ResearchResearchSpeed2: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
    },
    Operation.ResearchElectricEnergyDistribution1: {
        Material.AutomationSciencePack: Integer(120),
        Material.LogisticSciencePack: Integer(120),
    },
    Operation.ResearchAdvancedMaterialProcessing: {
        Material.AutomationSciencePack: Integer(75),
        Material.LogisticSciencePack: Integer(75),
    },
    Operation.ResearchConcrete: {
        Material.AutomationSciencePack: Integer(250),
        Material.LogisticSciencePack: Integer(250),
    },
    Operation.ResearchEngine: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
    },
    Operation.ResearchLandfill: {
        Material.AutomationSciencePack: Integer(50),
        Material.LogisticSciencePack: Integer(50),
    },
    Operation.ResearchLogistics2: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
    },
    Operation.ResearchToolbelt: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
    },
    Operation.ResearchStoneWall: {Material.AutomationSciencePack: Integer(10)},
    Operation.ResearchGate: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
    },
    Operation.ResearchChemicalSciencePack: {
        Material.AutomationSciencePack: Integer(75),
        Material.LogisticSciencePack: Integer(75),
    },
    Operation.ResearchMilitarySciencePack: {
        Material.AutomationSciencePack: Integer(30),
        Material.LogisticSciencePack: Integer(30),
    },
    Operation.ResearchProductionSciencePack: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
        Material.ChemicalSciencePack: Integer(100),
    },
    Operation.ResearchUtilitySciencePack: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
        Material.ChemicalSciencePack: Integer(100),
    },
    Operation.ResearchSpaceSciencePack: {},
    Operation.ResearchMilitary3: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
        Material.ChemicalSciencePack: Integer(100),
        Material.MilitarySciencePack: Integer(100),
    },
    Operation.ResearchMilitary4: {
        Material.AutomationSciencePack: Integer(150),
        Material.LogisticSciencePack: Integer(150),
        Material.ChemicalSciencePack: Integer(150),
        Material.MilitarySciencePack: Integer(150),
        Material.UtilitySciencePack: Integer(150),
    },
    Operation.ResearchUraniumAmmo: {
        Material.AutomationSciencePack: Integer(1000),
        Material.LogisticSciencePack: Integer(1000),
        Material.ChemicalSciencePack: Integer(1000),
        Material.MilitarySciencePack: Integer(1000),
        Material.UtilitySciencePack: Integer(1000),
    },
    Operation.ResearchAtomicBomb: {
        Material.AutomationSciencePack: Integer(5000),
        Material.LogisticSciencePack: Integer(5000),
        Material.ChemicalSciencePack: Integer(5000),
        Material.MilitarySciencePack: Integer(5000),
        Material.ProductionSciencePack: Integer(5000),
        Material.UtilitySciencePack: Integer(5000),
    },
    Operation.ResearchAutomation3: {
        Material.AutomationSciencePack: Integer(150),
        Material.LogisticSciencePack: Integer(150),
        Material.ChemicalSciencePack: Integer(150),
        Material.ProductionSciencePack: Integer(150),
    },
    Operation.ResearchExplosives: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
    },
    Operation.ResearchCliffExplosives: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
    },
    Operation.ResearchFlammables: {
        Material.AutomationSciencePack: Integer(50),
        Material.LogisticSciencePack: Integer(50),
    },
    Operation.ResearchLandMine: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
        Material.MilitarySciencePack: Integer(100),
    },
    Operation.ResearchFlamethrower: {
        Material.AutomationSciencePack: Integer(50),
        Material.LogisticSciencePack: Integer(50),
        Material.MilitarySciencePack: Integer(50),
    },
    Operation.ResearchAdvancedCircuit: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
    },
    Operation.ResearchProcessingUnit: {
        Material.AutomationSciencePack: Integer(300),
        Material.LogisticSciencePack: Integer(300),
        Material.ChemicalSciencePack: Integer(300),
    },
    Operation.ResearchFluidWagon: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
    },
    Operation.ResearchBrakingForce1: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
        Material.ChemicalSciencePack: Integer(100),
    },
    Operation.ResearchBrakingForce2: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
        Material.ChemicalSciencePack: Integer(200),
    },
    Operation.ResearchBrakingForce3: {
        Material.AutomationSciencePack: Integer(250),
        Material.LogisticSciencePack: Integer(250),
        Material.ChemicalSciencePack: Integer(250),
        Material.ProductionSciencePack: Integer(250),
    },
    Operation.ResearchBrakingForce4: {
        Material.AutomationSciencePack: Integer(350),
        Material.LogisticSciencePack: Integer(350),
        Material.ChemicalSciencePack: Integer(350),
        Material.ProductionSciencePack: Integer(350),
    },
    Operation.ResearchBrakingForce5: {
        Material.AutomationSciencePack: Integer(450),
        Material.LogisticSciencePack: Integer(450),
        Material.ChemicalSciencePack: Integer(450),
        Material.ProductionSciencePack: Integer(450),
    },
    Operation.ResearchBrakingForce6: {
        Material.AutomationSciencePack: Integer(550),
        Material.LogisticSciencePack: Integer(550),
        Material.ChemicalSciencePack: Integer(550),
        Material.ProductionSciencePack: Integer(550),
        Material.UtilitySciencePack: Integer(550),
    },
    Operation.ResearchBrakingForce7: {
        Material.AutomationSciencePack: Integer(650),
        Material.LogisticSciencePack: Integer(650),
        Material.ChemicalSciencePack: Integer(650),
        Material.ProductionSciencePack: Integer(650),
        Material.UtilitySciencePack: Integer(650),
    },
    Operation.ResearchTank: {
        Material.AutomationSciencePack: Integer(250),
        Material.LogisticSciencePack: Integer(250),
        Material.ChemicalSciencePack: Integer(250),
        Material.MilitarySciencePack: Integer(250),
    },
    Operation.ResearchLogistics3: {
        Material.AutomationSciencePack: Integer(300),
        Material.LogisticSciencePack: Integer(300),
        Material.ChemicalSciencePack: Integer(300),
        Material.ProductionSciencePack: Integer(300),
    },
    Operation.ResearchLaser: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
        Material.ChemicalSciencePack: Integer(100),
    },
    Operation.ResearchRocketry: {
        Material.AutomationSciencePack: Integer(120),
        Material.LogisticSciencePack: Integer(120),
        Material.MilitarySciencePack: Integer(120),
    },
    Operation.ResearchExplosiveRocketry: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
        Material.ChemicalSciencePack: Integer(100),
        Material.MilitarySciencePack: Integer(100),
    },
    Operation.ResearchModularArmor: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
    },
    Operation.ResearchPowerArmor: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
        Material.ChemicalSciencePack: Integer(200),
    },
    Operation.ResearchPowerArmorMk2: {
        Material.AutomationSciencePack: Integer(400),
        Material.LogisticSciencePack: Integer(400),
        Material.ChemicalSciencePack: Integer(400),
        Material.MilitarySciencePack: Integer(400),
        Material.UtilitySciencePack: Integer(400),
    },
    Operation.ResearchLaserTurret: {
        Material.AutomationSciencePack: Integer(150),
        Material.LogisticSciencePack: Integer(150),
        Material.MilitarySciencePack: Integer(150),
        Material.ChemicalSciencePack: Integer(150),
    },
    Operation.ResearchRobotics: {
        Material.AutomationSciencePack: Integer(75),
        Material.LogisticSciencePack: Integer(75),
        Material.ChemicalSciencePack: Integer(75),
    },
    Operation.ResearchRocketFuel: {
        Material.AutomationSciencePack: Integer(300),
        Material.LogisticSciencePack: Integer(300),
        Material.ChemicalSciencePack: Integer(300),
    },
    Operation.ResearchLowDensityStructure: {
        Material.AutomationSciencePack: Integer(300),
        Material.LogisticSciencePack: Integer(300),
        Material.ChemicalSciencePack: Integer(300),
    },
    Operation.ResearchRocketSilo: {
        Material.AutomationSciencePack: Integer(1000),
        Material.LogisticSciencePack: Integer(1000),
        Material.ChemicalSciencePack: Integer(1000),
        Material.ProductionSciencePack: Integer(1000),
        Material.UtilitySciencePack: Integer(1000),
    },
    Operation.ResearchResearchSpeed3: {
        Material.AutomationSciencePack: Integer(250),
        Material.LogisticSciencePack: Integer(250),
        Material.ChemicalSciencePack: Integer(250),
    },
    Operation.ResearchResearchSpeed4: {
        Material.AutomationSciencePack: Integer(500),
        Material.LogisticSciencePack: Integer(500),
        Material.ChemicalSciencePack: Integer(500),
    },
    Operation.ResearchResearchSpeed5: {
        Material.AutomationSciencePack: Integer(500),
        Material.LogisticSciencePack: Integer(500),
        Material.ChemicalSciencePack: Integer(500),
        Material.ProductionSciencePack: Integer(500),
    },
    Operation.ResearchResearchSpeed6: {
        Material.AutomationSciencePack: Integer(500),
        Material.LogisticSciencePack: Integer(500),
        Material.ChemicalSciencePack: Integer(500),
        Material.ProductionSciencePack: Integer(500),
        Material.UtilitySciencePack: Integer(500),
    },
    Operation.ResearchElectricEnergyDistribution2: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
        Material.ChemicalSciencePack: Integer(100),
    },
    Operation.ResearchElectricEnergyAccumulators: {
        Material.AutomationSciencePack: Integer(150),
        Material.LogisticSciencePack: Integer(150),
    },
    Operation.ResearchAdvancedMaterialProcessing2: {
        Material.AutomationSciencePack: Integer(250),
        Material.LogisticSciencePack: Integer(250),
        Material.ChemicalSciencePack: Integer(250),
    },
    Operation.ResearchEffectTransmission: {
        Material.AutomationSciencePack: Integer(75),
        Material.LogisticSciencePack: Integer(75),
        Material.ChemicalSciencePack: Integer(75),
        Material.ProductionSciencePack: Integer(75),
    },
    Operation.ResearchLubricant: {
        Material.AutomationSciencePack: Integer(50),
        Material.LogisticSciencePack: Integer(50),
        Material.ChemicalSciencePack: Integer(50),
    },
    Operation.ResearchElectricEngine: {
        Material.AutomationSciencePack: Integer(50),
        Material.LogisticSciencePack: Integer(50),
        Material.ChemicalSciencePack: Integer(50),
    },
    Operation.ResearchBattery: {
        Material.AutomationSciencePack: Integer(150),
        Material.LogisticSciencePack: Integer(150),
    },
    Operation.ResearchConstructionRobotics: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
        Material.ChemicalSciencePack: Integer(100),
    },
    Operation.ResearchLogisticRobotics: {
        Material.AutomationSciencePack: Integer(250),
        Material.LogisticSciencePack: Integer(250),
        Material.ChemicalSciencePack: Integer(250),
    },
    Operation.ResearchLogisticSystem: {
        Material.AutomationSciencePack: Integer(500),
        Material.LogisticSciencePack: Integer(500),
        Material.ChemicalSciencePack: Integer(500),
        Material.UtilitySciencePack: Integer(500),
    },
    Operation.ResearchWorkerRobotsSpeed1: {
        Material.AutomationSciencePack: Integer(50),
        Material.LogisticSciencePack: Integer(50),
        Material.ChemicalSciencePack: Integer(50),
    },
    Operation.ResearchWorkerRobotsSpeed2: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
        Material.ChemicalSciencePack: Integer(100),
    },
    Operation.ResearchWorkerRobotsSpeed3: {
        Material.AutomationSciencePack: Integer(150),
        Material.LogisticSciencePack: Integer(150),
        Material.ChemicalSciencePack: Integer(150),
        Material.UtilitySciencePack: Integer(150),
    },
    Operation.ResearchWorkerRobotsSpeed4: {
        Material.AutomationSciencePack: Integer(250),
        Material.LogisticSciencePack: Integer(250),
        Material.ChemicalSciencePack: Integer(250),
        Material.UtilitySciencePack: Integer(250),
    },
    Operation.ResearchWorkerRobotsSpeed5: {
        Material.AutomationSciencePack: Integer(500),
        Material.LogisticSciencePack: Integer(500),
        Material.ChemicalSciencePack: Integer(500),
        Material.ProductionSciencePack: Integer(500),
        Material.UtilitySciencePack: Integer(500),
    },
    Operation.ResearchWorkerRobotsSpeed6: {
        Material.AutomationSciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-6)))
        ),
        Material.LogisticSciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-6)))
        ),
        Material.ChemicalSciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-6)))
        ),
        Material.ProductionSciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-6)))
        ),
        Material.UtilitySciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-6)))
        ),
        Material.SpaceSciencePack: Mul(
            Integer(1000), Pow(Integer(2), Add(L, Integer(-6)))
        ),
    },
    Operation.ResearchWorkerRobotsStorage1: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
        Material.ChemicalSciencePack: Integer(200),
    },
    Operation.ResearchWorkerRobotsStorage2: {
        Material.AutomationSciencePack: Integer(300),
        Material.LogisticSciencePack: Integer(300),
        Material.ChemicalSciencePack: Integer(300),
        Material.ProductionSciencePack: Integer(300),
    },
    Operation.ResearchWorkerRobotsStorage3: {
        Material.AutomationSciencePack: Integer(450),
        Material.LogisticSciencePack: Integer(450),
        Material.ChemicalSciencePack: Integer(450),
        Material.ProductionSciencePack: Integer(450),
        Material.UtilitySciencePack: Integer(450),
    },
    Operation.ResearchEnergyShieldEquipment: {
        Material.AutomationSciencePack: Integer(150),
        Material.LogisticSciencePack: Integer(150),
        Material.MilitarySciencePack: Integer(150),
    },
    Operation.ResearchNightVisionEquipment: {
        Material.AutomationSciencePack: Integer(50),
        Material.LogisticSciencePack: Integer(50),
    },
    Operation.ResearchBeltImmunityEquipment: {
        Material.AutomationSciencePack: Integer(50),
        Material.LogisticSciencePack: Integer(50),
    },
    Operation.ResearchEnergyShieldMk2Equipment: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
        Material.ChemicalSciencePack: Integer(200),
        Material.MilitarySciencePack: Integer(200),
    },
    Operation.ResearchBatteryEquipment: {
        Material.AutomationSciencePack: Integer(50),
        Material.LogisticSciencePack: Integer(50),
    },
    Operation.ResearchBatteryMk2Equipment: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
        Material.ChemicalSciencePack: Integer(100),
    },
    Operation.ResearchSolarPanelEquipment: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
    },
    Operation.ResearchPersonalLaserDefenseEquipment: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
        Material.ChemicalSciencePack: Integer(100),
        Material.MilitarySciencePack: Integer(100),
    },
    Operation.ResearchDischargeDefenseEquipment: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
        Material.ChemicalSciencePack: Integer(100),
        Material.MilitarySciencePack: Integer(100),
    },
    Operation.ResearchFissionReactorEquipment: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
        Material.ChemicalSciencePack: Integer(200),
        Material.MilitarySciencePack: Integer(200),
        Material.UtilitySciencePack: Integer(200),
    },
    Operation.ResearchExoskeletonEquipment: {
        Material.AutomationSciencePack: Integer(50),
        Material.LogisticSciencePack: Integer(50),
        Material.ChemicalSciencePack: Integer(50),
    },
    Operation.ResearchPersonalRoboportEquipment: {
        Material.AutomationSciencePack: Integer(50),
        Material.LogisticSciencePack: Integer(50),
        Material.ChemicalSciencePack: Integer(50),
    },
    Operation.ResearchPersonalRoboportMk2Equipment: {
        Material.AutomationSciencePack: Integer(250),
        Material.LogisticSciencePack: Integer(250),
        Material.ChemicalSciencePack: Integer(250),
        Material.UtilitySciencePack: Integer(250),
    },
    Operation.ResearchFluidHandling: {
        Material.AutomationSciencePack: Integer(50),
        Material.LogisticSciencePack: Integer(50),
    },
    Operation.ResearchOilGathering: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
    },
    Operation.ResearchOilProcessing: {},
    Operation.ResearchAdvancedOilProcessing: {
        Material.AutomationSciencePack: Integer(75),
        Material.LogisticSciencePack: Integer(75),
        Material.ChemicalSciencePack: Integer(75),
    },
    Operation.ResearchCoalLiquefaction: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
        Material.ChemicalSciencePack: Integer(200),
        Material.ProductionSciencePack: Integer(200),
    },
    Operation.ResearchSulfurProcessing: {
        Material.AutomationSciencePack: Integer(150),
        Material.LogisticSciencePack: Integer(150),
    },
    Operation.ResearchPlastics: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
    },
    Operation.ResearchModules: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
    },
    Operation.ResearchSpeedModule: {
        Material.AutomationSciencePack: Integer(50),
        Material.LogisticSciencePack: Integer(50),
    },
    Operation.ResearchSpeedModule2: {
        Material.AutomationSciencePack: Integer(75),
        Material.LogisticSciencePack: Integer(75),
        Material.ChemicalSciencePack: Integer(75),
    },
    Operation.ResearchSpeedModule3: {
        Material.AutomationSciencePack: Integer(300),
        Material.LogisticSciencePack: Integer(300),
        Material.ChemicalSciencePack: Integer(300),
        Material.ProductionSciencePack: Integer(300),
    },
    Operation.ResearchProductivityModule: {
        Material.AutomationSciencePack: Integer(50),
        Material.LogisticSciencePack: Integer(50),
    },
    Operation.ResearchProductivityModule2: {
        Material.AutomationSciencePack: Integer(75),
        Material.LogisticSciencePack: Integer(75),
        Material.ChemicalSciencePack: Integer(75),
    },
    Operation.ResearchProductivityModule3: {
        Material.AutomationSciencePack: Integer(300),
        Material.LogisticSciencePack: Integer(300),
        Material.ChemicalSciencePack: Integer(300),
        Material.ProductionSciencePack: Integer(300),
    },
    Operation.ResearchEfficiencyModule: {
        Material.AutomationSciencePack: Integer(50),
        Material.LogisticSciencePack: Integer(50),
    },
    Operation.ResearchEfficiencyModule2: {
        Material.AutomationSciencePack: Integer(75),
        Material.LogisticSciencePack: Integer(75),
        Material.ChemicalSciencePack: Integer(75),
    },
    Operation.ResearchEfficiencyModule3: {
        Material.AutomationSciencePack: Integer(300),
        Material.LogisticSciencePack: Integer(300),
        Material.ChemicalSciencePack: Integer(300),
        Material.ProductionSciencePack: Integer(300),
    },
    Operation.ResearchDefender: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
        Material.MilitarySciencePack: Integer(100),
    },
    Operation.ResearchDistractor: {
        Material.AutomationSciencePack: Integer(200),
        Material.LogisticSciencePack: Integer(200),
        Material.ChemicalSciencePack: Integer(200),
        Material.MilitarySciencePack: Integer(200),
    },
    Operation.ResearchDestroyer: {
        Material.AutomationSciencePack: Integer(300),
        Material.LogisticSciencePack: Integer(300),
        Material.ChemicalSciencePack: Integer(300),
        Material.MilitarySciencePack: Integer(300),
        Material.UtilitySciencePack: Integer(300),
    },
    Operation.ResearchUraniumMining: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
        Material.ChemicalSciencePack: Integer(100),
    },
    Operation.ResearchUraniumProcessing: {},
    Operation.ResearchNuclearPower: {
        Material.AutomationSciencePack: Integer(800),
        Material.LogisticSciencePack: Integer(800),
        Material.ChemicalSciencePack: Integer(800),
    },
    Operation.ResearchKovarexEnrichmentProcess: {
        Material.AutomationSciencePack: Integer(1500),
        Material.LogisticSciencePack: Integer(1500),
        Material.ChemicalSciencePack: Integer(1500),
        Material.ProductionSciencePack: Integer(1500),
    },
    Operation.ResearchNuclearFuelReprocessing: {
        Material.AutomationSciencePack: Integer(50),
        Material.LogisticSciencePack: Integer(50),
        Material.ChemicalSciencePack: Integer(50),
        Material.ProductionSciencePack: Integer(50),
    },
    Operation.ResearchMiningProductivity1: {
        Material.AutomationSciencePack: Integer(250),
        Material.LogisticSciencePack: Integer(250),
    },
    Operation.ResearchMiningProductivity2: {
        Material.AutomationSciencePack: Integer(500),
        Material.LogisticSciencePack: Integer(500),
        Material.ChemicalSciencePack: Integer(500),
    },
    Operation.ResearchMiningProductivity3: {
        Material.AutomationSciencePack: Integer(1000),
        Material.LogisticSciencePack: Integer(1000),
        Material.ChemicalSciencePack: Integer(1000),
        Material.ProductionSciencePack: Integer(1000),
        Material.UtilitySciencePack: Integer(1000),
    },
    Operation.ResearchMiningProductivity4: {
        Material.AutomationSciencePack: Add(Mul(Integer(2500), L), Integer(-7500)),
        Material.LogisticSciencePack: Add(Mul(Integer(2500), L), Integer(-7500)),
        Material.ChemicalSciencePack: Add(Mul(Integer(2500), L), Integer(-7500)),
        Material.ProductionSciencePack: Add(Mul(Integer(2500), L), Integer(-7500)),
        Material.UtilitySciencePack: Add(Mul(Integer(2500), L), Integer(-7500)),
        Material.SpaceSciencePack: Add(Mul(Integer(2500), L), Integer(-7500)),
    },
    Operation.ResearchArtillery: {
        Material.AutomationSciencePack: Integer(2000),
        Material.LogisticSciencePack: Integer(2000),
        Material.ChemicalSciencePack: Integer(2000),
        Material.MilitarySciencePack: Integer(2000),
        Material.UtilitySciencePack: Integer(2000),
    },
    Operation.ResearchSpidertron: {
        Material.AutomationSciencePack: Integer(2500),
        Material.LogisticSciencePack: Integer(2500),
        Material.MilitarySciencePack: Integer(2500),
        Material.ChemicalSciencePack: Integer(2500),
        Material.ProductionSciencePack: Integer(2500),
        Material.UtilitySciencePack: Integer(2500),
    },
    Operation.ResearchCircuitNetwork: {
        Material.AutomationSciencePack: Integer(100),
        Material.LogisticSciencePack: Integer(100),
    },
    Operation.ResearchAdvancedCombinators: {
        Material.AutomationSciencePack: Integer(50),
        Material.LogisticSciencePack: Integer(50),
        Material.ChemicalSciencePack: Integer(50),
    },
    Operation.MiningIronOre: {Material.ResourceIronOre: Integer(1)},
    Operation.MiningCopperOre: {Material.ResourceCopperOre: Integer(1)},
    Operation.MiningCoal: {Material.ResourceCoal: Integer(1)},
    Operation.MiningStone: {Material.ResourceStone: Integer(1)},
    Operation.MiningUraniumOre: {
        Material.ResourceUraniumOre: Integer(1),
        Material.SulfuricAcid: Integer(10),
    },
    Operation.MiningCrudeOil: {Material.ResourceCrudeOil: Integer(1)},
}

RESULTS: dict[Operation, dict[Material, Integer]] = {
    Operation.SpeedModule: {Material.SpeedModule: Integer(1)},
    Operation.SpeedModule2: {Material.SpeedModule2: Integer(1)},
    Operation.SpeedModule3: {Material.SpeedModule3: Integer(1)},
    Operation.ProductivityModule: {Material.ProductivityModule: Integer(1)},
    Operation.ProductivityModule2: {Material.ProductivityModule2: Integer(1)},
    Operation.ProductivityModule3: {Material.ProductivityModule3: Integer(1)},
    Operation.EfficiencyModule: {Material.EfficiencyModule: Integer(1)},
    Operation.EfficiencyModule2: {Material.EfficiencyModule2: Integer(1)},
    Operation.EfficiencyModule3: {Material.EfficiencyModule3: Integer(1)},
    Operation.BulkInserter: {Material.BulkInserter: Integer(1)},
    Operation.BasicOilProcessing: {Material.PetroleumGas: Integer(45)},
    Operation.AdvancedOilProcessing: {
        Material.HeavyOil: Integer(25),
        Material.LightOil: Integer(45),
        Material.PetroleumGas: Integer(55),
    },
    Operation.CoalLiquefaction: {
        Material.HeavyOil: Integer(90),
        Material.LightOil: Integer(20),
        Material.PetroleumGas: Integer(10),
    },
    Operation.HeavyOilCracking: {Material.LightOil: Integer(30)},
    Operation.LightOilCracking: {Material.PetroleumGas: Integer(20)},
    Operation.SulfuricAcid: {Material.SulfuricAcid: Integer(50)},
    Operation.PlasticBar: {Material.PlasticBar: Integer(2)},
    Operation.SolidFuelFromLightOil: {Material.SolidFuel: Integer(1)},
    Operation.SolidFuelFromPetroleumGas: {Material.SolidFuel: Integer(1)},
    Operation.SolidFuelFromHeavyOil: {Material.SolidFuel: Integer(1)},
    Operation.Sulfur: {Material.Sulfur: Integer(2)},
    Operation.Lubricant: {Material.Lubricant: Integer(10)},
    Operation.Barrel: {Material.Barrel: Integer(1)},
    Operation.NightVisionEquipment: {Material.NightVisionEquipment: Integer(1)},
    Operation.BeltImmunityEquipment: {Material.BeltImmunityEquipment: Integer(1)},
    Operation.EnergyShieldEquipment: {Material.EnergyShieldEquipment: Integer(1)},
    Operation.EnergyShieldMk2Equipment: {Material.EnergyShieldMk2Equipment: Integer(1)},
    Operation.BatteryEquipment: {Material.BatteryEquipment: Integer(1)},
    Operation.BatteryMk2Equipment: {Material.BatteryMk2Equipment: Integer(1)},
    Operation.SolarPanelEquipment: {Material.SolarPanelEquipment: Integer(1)},
    Operation.FissionReactorEquipment: {Material.FissionReactorEquipment: Integer(1)},
    Operation.PersonalLaserDefenseEquipment: {
        Material.PersonalLaserDefenseEquipment: Integer(1)
    },
    Operation.DischargeDefenseEquipment: {
        Material.DischargeDefenseEquipment: Integer(1)
    },
    Operation.ExoskeletonEquipment: {Material.ExoskeletonEquipment: Integer(1)},
    Operation.PersonalRoboportEquipment: {
        Material.PersonalRoboportEquipment: Integer(1)
    },
    Operation.PersonalRoboportMk2Equipment: {
        Material.PersonalRoboportMk2Equipment: Integer(1)
    },
    Operation.LaserTurret: {Material.LaserTurret: Integer(1)},
    Operation.FlamethrowerTurret: {Material.FlamethrowerTurret: Integer(1)},
    Operation.ArtilleryTurret: {Material.ArtilleryTurret: Integer(1)},
    Operation.GunTurret: {Material.GunTurret: Integer(1)},
    Operation.WoodenChest: {Material.WoodenChest: Integer(1)},
    Operation.DisplayPanel: {Material.DisplayPanel: Integer(1)},
    Operation.IronStick: {Material.IronStick: Integer(2)},
    Operation.StoneFurnace: {Material.StoneFurnace: Integer(1)},
    Operation.Boiler: {Material.Boiler: Integer(1)},
    Operation.SteamEngine: {Material.SteamEngine: Integer(1)},
    Operation.IronGearWheel: {Material.IronGearWheel: Integer(1)},
    Operation.ElectronicCircuit: {Material.ElectronicCircuit: Integer(1)},
    Operation.TransportBelt: {Material.TransportBelt: Integer(2)},
    Operation.ElectricMiningDrill: {Material.ElectricMiningDrill: Integer(1)},
    Operation.BurnerMiningDrill: {Material.BurnerMiningDrill: Integer(1)},
    Operation.Inserter: {Material.Inserter: Integer(1)},
    Operation.FastInserter: {Material.FastInserter: Integer(1)},
    Operation.LongHandedInserter: {Material.LongHandedInserter: Integer(1)},
    Operation.BurnerInserter: {Material.BurnerInserter: Integer(1)},
    Operation.Pipe: {Material.Pipe: Integer(1)},
    Operation.OffshorePump: {Material.OffshorePump: Integer(1)},
    Operation.CopperCable: {Material.CopperCable: Integer(2)},
    Operation.SmallElectricPole: {Material.SmallElectricPole: Integer(2)},
    Operation.Pistol: {Material.Pistol: Integer(1)},
    Operation.SubmachineGun: {Material.SubmachineGun: Integer(1)},
    Operation.FirearmMagazine: {Material.FirearmMagazine: Integer(1)},
    Operation.LightArmor: {Material.LightArmor: Integer(1)},
    Operation.Radar: {Material.Radar: Integer(1)},
    Operation.SmallLamp: {Material.SmallLamp: Integer(1)},
    Operation.PipeToGround: {Material.PipeToGround: Integer(2)},
    Operation.AssemblingMachine1: {Material.AssemblingMachine1: Integer(1)},
    Operation.RepairPack: {Material.RepairPack: Integer(1)},
    Operation.AutomationSciencePack: {Material.AutomationSciencePack: Integer(1)},
    Operation.LogisticSciencePack: {Material.LogisticSciencePack: Integer(1)},
    Operation.Lab: {Material.Lab: Integer(1)},
    Operation.StoneWall: {Material.StoneWall: Integer(1)},
    Operation.AssemblingMachine2: {Material.AssemblingMachine2: Integer(1)},
    Operation.Splitter: {Material.Splitter: Integer(1)},
    Operation.UndergroundBelt: {Material.UndergroundBelt: Integer(2)},
    Operation.Loader: {Material.Loader: Integer(1)},
    Operation.Car: {Material.Car: Integer(1)},
    Operation.EngineUnit: {Material.EngineUnit: Integer(1)},
    Operation.IronChest: {Material.IronChest: Integer(1)},
    Operation.BigElectricPole: {Material.BigElectricPole: Integer(1)},
    Operation.MediumElectricPole: {Material.MediumElectricPole: Integer(1)},
    Operation.Shotgun: {Material.Shotgun: Integer(1)},
    Operation.ShotgunShell: {Material.ShotgunShell: Integer(1)},
    Operation.PiercingRoundsMagazine: {Material.PiercingRoundsMagazine: Integer(2)},
    Operation.Grenade: {Material.Grenade: Integer(1)},
    Operation.SteelFurnace: {Material.SteelFurnace: Integer(1)},
    Operation.Gate: {Material.Gate: Integer(1)},
    Operation.HeavyArmor: {Material.HeavyArmor: Integer(1)},
    Operation.SteelChest: {Material.SteelChest: Integer(1)},
    Operation.FastUndergroundBelt: {Material.FastUndergroundBelt: Integer(2)},
    Operation.FastSplitter: {Material.FastSplitter: Integer(1)},
    Operation.Concrete: {Material.Concrete: Integer(10)},
    Operation.HazardConcrete: {Material.HazardConcrete: Integer(10)},
    Operation.RefinedConcrete: {Material.RefinedConcrete: Integer(10)},
    Operation.RefinedHazardConcrete: {Material.RefinedHazardConcrete: Integer(10)},
    Operation.Landfill: {Material.Landfill: Integer(1)},
    Operation.FastTransportBelt: {Material.FastTransportBelt: Integer(1)},
    Operation.SolarPanel: {Material.SolarPanel: Integer(1)},
    Operation.Rail: {Material.Rail: Integer(2)},
    Operation.Locomotive: {Material.Locomotive: Integer(1)},
    Operation.CargoWagon: {Material.CargoWagon: Integer(1)},
    Operation.RailSignal: {Material.RailSignal: Integer(1)},
    Operation.RailChainSignal: {Material.RailChainSignal: Integer(1)},
    Operation.TrainStop: {Material.TrainStop: Integer(1)},
    Operation.CopperPlate: {Material.CopperPlate: Integer(1)},
    Operation.IronPlate: {Material.IronPlate: Integer(1)},
    Operation.StoneBrick: {Material.StoneBrick: Integer(1)},
    Operation.SteelPlate: {Material.SteelPlate: Integer(1)},
    Operation.ArithmeticCombinator: {Material.ArithmeticCombinator: Integer(1)},
    Operation.DeciderCombinator: {Material.DeciderCombinator: Integer(1)},
    Operation.ConstantCombinator: {Material.ConstantCombinator: Integer(1)},
    Operation.SelectorCombinator: {Material.SelectorCombinator: Integer(1)},
    Operation.PowerSwitch: {Material.PowerSwitch: Integer(1)},
    Operation.ProgrammableSpeaker: {Material.ProgrammableSpeaker: Integer(1)},
    Operation.PoisonCapsule: {Material.PoisonCapsule: Integer(1)},
    Operation.SlowdownCapsule: {Material.SlowdownCapsule: Integer(1)},
    Operation.ClusterGrenade: {Material.ClusterGrenade: Integer(1)},
    Operation.DefenderCapsule: {Material.DefenderCapsule: Integer(1)},
    Operation.DistractorCapsule: {Material.DistractorCapsule: Integer(1)},
    Operation.DestroyerCapsule: {Material.DestroyerCapsule: Integer(1)},
    Operation.CliffExplosives: {Material.CliffExplosives: Integer(1)},
    Operation.UraniumRoundsMagazine: {Material.UraniumRoundsMagazine: Integer(1)},
    Operation.Rocket: {Material.Rocket: Integer(1)},
    Operation.ExplosiveRocket: {Material.ExplosiveRocket: Integer(1)},
    Operation.AtomicBomb: {Material.AtomicBomb: Integer(1)},
    Operation.PiercingShotgunShell: {Material.PiercingShotgunShell: Integer(1)},
    Operation.CannonShell: {Material.CannonShell: Integer(1)},
    Operation.ExplosiveCannonShell: {Material.ExplosiveCannonShell: Integer(1)},
    Operation.UraniumCannonShell: {Material.UraniumCannonShell: Integer(1)},
    Operation.ExplosiveUraniumCannonShell: {
        Material.ExplosiveUraniumCannonShell: Integer(1)
    },
    Operation.ArtilleryShell: {Material.ArtilleryShell: Integer(1)},
    Operation.FlamethrowerAmmo: {Material.FlamethrowerAmmo: Integer(1)},
    Operation.ExpressTransportBelt: {Material.ExpressTransportBelt: Integer(1)},
    Operation.AssemblingMachine3: {Material.AssemblingMachine3: Integer(1)},
    Operation.Tank: {Material.Tank: Integer(1)},
    Operation.Spidertron: {Material.Spidertron: Integer(1)},
    Operation.FluidWagon: {Material.FluidWagon: Integer(1)},
    Operation.ArtilleryWagon: {Material.ArtilleryWagon: Integer(1)},
    Operation.ModularArmor: {Material.ModularArmor: Integer(1)},
    Operation.PowerArmor: {Material.PowerArmor: Integer(1)},
    Operation.PowerArmorMk2: {Material.PowerArmorMk2: Integer(1)},
    Operation.Flamethrower: {Material.Flamethrower: Integer(1)},
    Operation.LandMine: {Material.LandMine: Integer(4)},
    Operation.RocketLauncher: {Material.RocketLauncher: Integer(1)},
    Operation.CombatShotgun: {Material.CombatShotgun: Integer(1)},
    Operation.ChemicalSciencePack: {Material.ChemicalSciencePack: Integer(2)},
    Operation.MilitarySciencePack: {Material.MilitarySciencePack: Integer(2)},
    Operation.ProductionSciencePack: {Material.ProductionSciencePack: Integer(3)},
    Operation.UtilitySciencePack: {Material.UtilitySciencePack: Integer(3)},
    Operation.ExpressUndergroundBelt: {Material.ExpressUndergroundBelt: Integer(2)},
    Operation.FastLoader: {Material.FastLoader: Integer(1)},
    Operation.ExpressLoader: {Material.ExpressLoader: Integer(1)},
    Operation.ExpressSplitter: {Material.ExpressSplitter: Integer(1)},
    Operation.AdvancedCircuit: {Material.AdvancedCircuit: Integer(1)},
    Operation.ProcessingUnit: {Material.ProcessingUnit: Integer(1)},
    Operation.LogisticRobot: {Material.LogisticRobot: Integer(1)},
    Operation.ConstructionRobot: {Material.ConstructionRobot: Integer(1)},
    Operation.PassiveProviderChest: {Material.PassiveProviderChest: Integer(1)},
    Operation.ActiveProviderChest: {Material.ActiveProviderChest: Integer(1)},
    Operation.StorageChest: {Material.StorageChest: Integer(1)},
    Operation.BufferChest: {Material.BufferChest: Integer(1)},
    Operation.RequesterChest: {Material.RequesterChest: Integer(1)},
    Operation.RocketSilo: {Material.RocketSilo: Integer(1)},
    Operation.CargoLandingPad: {Material.CargoLandingPad: Integer(1)},
    Operation.Roboport: {Material.Roboport: Integer(1)},
    Operation.Substation: {Material.Substation: Integer(1)},
    Operation.Accumulator: {Material.Accumulator: Integer(1)},
    Operation.ElectricFurnace: {Material.ElectricFurnace: Integer(1)},
    Operation.Beacon: {Material.Beacon: Integer(1)},
    Operation.Pumpjack: {Material.Pumpjack: Integer(1)},
    Operation.OilRefinery: {Material.OilRefinery: Integer(1)},
    Operation.ElectricEngineUnit: {Material.ElectricEngineUnit: Integer(1)},
    Operation.FlyingRobotFrame: {Material.FlyingRobotFrame: Integer(1)},
    Operation.Explosives: {Material.Explosives: Integer(2)},
    Operation.Battery: {Material.Battery: Integer(1)},
    Operation.StorageTank: {Material.StorageTank: Integer(1)},
    Operation.Pump: {Material.Pump: Integer(1)},
    Operation.ChemicalPlant: {Material.ChemicalPlant: Integer(1)},
    Operation.LowDensityStructure: {Material.LowDensityStructure: Integer(1)},
    Operation.RocketFuel: {Material.RocketFuel: Integer(1)},
    Operation.RocketPart: {Material.RocketPart: Integer(1)},
    Operation.Satellite: {Material.Satellite: Integer(1)},
    Operation.NuclearReactor: {Material.NuclearReactor: Integer(1)},
    Operation.Centrifuge: {Material.Centrifuge: Integer(1)},
    Operation.UraniumProcessing: {
        Material.Uranium235: Integer(1),
        Material.Uranium238: Integer(1),
    },
    Operation.KovarexEnrichmentProcess: {
        Material.Uranium235: Integer(41),
        Material.Uranium238: Integer(2),
    },
    Operation.NuclearFuel: {Material.NuclearFuel: Integer(1)},
    Operation.NuclearFuelReprocessing: {Material.Uranium238: Integer(3)},
    Operation.UraniumFuelCell: {Material.UraniumFuelCell: Integer(10)},
    Operation.HeatExchanger: {Material.HeatExchanger: Integer(1)},
    Operation.HeatPipe: {Material.HeatPipe: Integer(1)},
    Operation.SteamTurbine: {Material.SteamTurbine: Integer(1)},
    Operation.ResearchSteamPower: {Material.TechnologySteamPower: Integer(1)},
    Operation.ResearchElectronics: {Material.TechnologyElectronics: Integer(1)},
    Operation.ResearchAutomationSciencePack: {
        Material.TechnologyAutomationSciencePack: Integer(1)
    },
    Operation.ResearchElectricMiningDrill: {
        Material.TechnologyElectricMiningDrill: Integer(1)
    },
    Operation.ResearchRepairPack: {Material.TechnologyRepairPack: Integer(1)},
    Operation.ResearchRadar: {Material.TechnologyRadar: Integer(1)},
    Operation.ResearchPhysicalProjectileDamage1: {
        Material.TechnologyPhysicalProjectileDamage1: Integer(1)
    },
    Operation.ResearchPhysicalProjectileDamage2: {
        Material.TechnologyPhysicalProjectileDamage2: Integer(1)
    },
    Operation.ResearchWeaponShootingSpeed1: {
        Material.TechnologyWeaponShootingSpeed1: Integer(1)
    },
    Operation.ResearchWeaponShootingSpeed2: {
        Material.TechnologyWeaponShootingSpeed2: Integer(1)
    },
    Operation.ResearchStrongerExplosives1: {
        Material.TechnologyStrongerExplosives1: Integer(1)
    },
    Operation.ResearchPhysicalProjectileDamage3: {
        Material.TechnologyPhysicalProjectileDamage3: Integer(1)
    },
    Operation.ResearchPhysicalProjectileDamage4: {
        Material.TechnologyPhysicalProjectileDamage4: Integer(1)
    },
    Operation.ResearchPhysicalProjectileDamage5: {
        Material.TechnologyPhysicalProjectileDamage5: Integer(1)
    },
    Operation.ResearchPhysicalProjectileDamage6: {
        Material.TechnologyPhysicalProjectileDamage6: Integer(1)
    },
    Operation.ResearchPhysicalProjectileDamage7: {
        Material.TechnologyPhysicalProjectileDamage7: Integer(1)
    },
    Operation.ResearchStrongerExplosives2: {
        Material.TechnologyStrongerExplosives2: Integer(1)
    },
    Operation.ResearchStrongerExplosives3: {
        Material.TechnologyStrongerExplosives3: Integer(1)
    },
    Operation.ResearchStrongerExplosives4: {
        Material.TechnologyStrongerExplosives4: Integer(1)
    },
    Operation.ResearchStrongerExplosives5: {
        Material.TechnologyStrongerExplosives5: Integer(1)
    },
    Operation.ResearchStrongerExplosives6: {
        Material.TechnologyStrongerExplosives6: Integer(1)
    },
    Operation.ResearchStrongerExplosives7: {
        Material.TechnologyStrongerExplosives7: Integer(1)
    },
    Operation.ResearchRefinedFlammables1: {
        Material.TechnologyRefinedFlammables1: Integer(1)
    },
    Operation.ResearchRefinedFlammables2: {
        Material.TechnologyRefinedFlammables2: Integer(1)
    },
    Operation.ResearchRefinedFlammables3: {
        Material.TechnologyRefinedFlammables3: Integer(1)
    },
    Operation.ResearchRefinedFlammables4: {
        Material.TechnologyRefinedFlammables4: Integer(1)
    },
    Operation.ResearchRefinedFlammables5: {
        Material.TechnologyRefinedFlammables5: Integer(1)
    },
    Operation.ResearchRefinedFlammables6: {
        Material.TechnologyRefinedFlammables6: Integer(1)
    },
    Operation.ResearchRefinedFlammables7: {
        Material.TechnologyRefinedFlammables7: Integer(1)
    },
    Operation.ResearchLaserWeaponsDamage1: {
        Material.TechnologyLaserWeaponsDamage1: Integer(1)
    },
    Operation.ResearchLaserWeaponsDamage2: {
        Material.TechnologyLaserWeaponsDamage2: Integer(1)
    },
    Operation.ResearchLaserWeaponsDamage3: {
        Material.TechnologyLaserWeaponsDamage3: Integer(1)
    },
    Operation.ResearchLaserWeaponsDamage4: {
        Material.TechnologyLaserWeaponsDamage4: Integer(1)
    },
    Operation.ResearchLaserWeaponsDamage5: {
        Material.TechnologyLaserWeaponsDamage5: Integer(1)
    },
    Operation.ResearchLaserWeaponsDamage6: {
        Material.TechnologyLaserWeaponsDamage6: Integer(1)
    },
    Operation.ResearchLaserWeaponsDamage7: {
        Material.TechnologyLaserWeaponsDamage7: Integer(1)
    },
    Operation.ResearchWeaponShootingSpeed3: {
        Material.TechnologyWeaponShootingSpeed3: Integer(1)
    },
    Operation.ResearchWeaponShootingSpeed4: {
        Material.TechnologyWeaponShootingSpeed4: Integer(1)
    },
    Operation.ResearchWeaponShootingSpeed5: {
        Material.TechnologyWeaponShootingSpeed5: Integer(1)
    },
    Operation.ResearchWeaponShootingSpeed6: {
        Material.TechnologyWeaponShootingSpeed6: Integer(1)
    },
    Operation.ResearchLaserShootingSpeed1: {
        Material.TechnologyLaserShootingSpeed1: Integer(1)
    },
    Operation.ResearchLaserShootingSpeed2: {
        Material.TechnologyLaserShootingSpeed2: Integer(1)
    },
    Operation.ResearchLaserShootingSpeed3: {
        Material.TechnologyLaserShootingSpeed3: Integer(1)
    },
    Operation.ResearchLaserShootingSpeed4: {
        Material.TechnologyLaserShootingSpeed4: Integer(1)
    },
    Operation.ResearchLaserShootingSpeed5: {
        Material.TechnologyLaserShootingSpeed5: Integer(1)
    },
    Operation.ResearchLaserShootingSpeed6: {
        Material.TechnologyLaserShootingSpeed6: Integer(1)
    },
    Operation.ResearchLaserShootingSpeed7: {
        Material.TechnologyLaserShootingSpeed7: Integer(1)
    },
    Operation.ResearchArtilleryShellRange1: {
        Material.TechnologyArtilleryShellRange1: Integer(1)
    },
    Operation.ResearchArtilleryShellSpeed1: {
        Material.TechnologyArtilleryShellSpeed1: Integer(1)
    },
    Operation.ResearchFollowerRobotCount5: {
        Material.TechnologyFollowerRobotCount5: Integer(1)
    },
    Operation.ResearchBulkInserter: {Material.TechnologyBulkInserter: Integer(1)},
    Operation.ResearchInserterCapacityBonus1: {
        Material.TechnologyInserterCapacityBonus1: Integer(1)
    },
    Operation.ResearchInserterCapacityBonus2: {
        Material.TechnologyInserterCapacityBonus2: Integer(1)
    },
    Operation.ResearchInserterCapacityBonus3: {
        Material.TechnologyInserterCapacityBonus3: Integer(1)
    },
    Operation.ResearchInserterCapacityBonus4: {
        Material.TechnologyInserterCapacityBonus4: Integer(1)
    },
    Operation.ResearchInserterCapacityBonus5: {
        Material.TechnologyInserterCapacityBonus5: Integer(1)
    },
    Operation.ResearchInserterCapacityBonus6: {
        Material.TechnologyInserterCapacityBonus6: Integer(1)
    },
    Operation.ResearchInserterCapacityBonus7: {
        Material.TechnologyInserterCapacityBonus7: Integer(1)
    },
    Operation.ResearchAutomation: {Material.TechnologyAutomation: Integer(1)},
    Operation.ResearchAutomation2: {Material.TechnologyAutomation2: Integer(1)},
    Operation.ResearchLogisticSciencePack: {
        Material.TechnologyLogisticSciencePack: Integer(1)
    },
    Operation.ResearchSteelProcessing: {Material.TechnologySteelProcessing: Integer(1)},
    Operation.ResearchSteelAxe: {Material.TechnologySteelAxe: Integer(1)},
    Operation.ResearchMilitary: {Material.TechnologyMilitary: Integer(1)},
    Operation.ResearchMilitary2: {Material.TechnologyMilitary2: Integer(1)},
    Operation.ResearchFastInserter: {Material.TechnologyFastInserter: Integer(1)},
    Operation.ResearchLogistics: {Material.TechnologyLogistics: Integer(1)},
    Operation.ResearchRailway: {Material.TechnologyRailway: Integer(1)},
    Operation.ResearchAutomatedRailTransportation: {
        Material.TechnologyAutomatedRailTransportation: Integer(1)
    },
    Operation.ResearchAutomobilism: {Material.TechnologyAutomobilism: Integer(1)},
    Operation.ResearchLamp: {Material.TechnologyLamp: Integer(1)},
    Operation.ResearchSolarEnergy: {Material.TechnologySolarEnergy: Integer(1)},
    Operation.ResearchHeavyArmor: {Material.TechnologyHeavyArmor: Integer(1)},
    Operation.ResearchGunTurret: {Material.TechnologyGunTurret: Integer(1)},
    Operation.ResearchResearchSpeed1: {Material.TechnologyResearchSpeed1: Integer(1)},
    Operation.ResearchResearchSpeed2: {Material.TechnologyResearchSpeed2: Integer(1)},
    Operation.ResearchElectricEnergyDistribution1: {
        Material.TechnologyElectricEnergyDistribution1: Integer(1)
    },
    Operation.ResearchAdvancedMaterialProcessing: {
        Material.TechnologyAdvancedMaterialProcessing: Integer(1)
    },
    Operation.ResearchConcrete: {Material.TechnologyConcrete: Integer(1)},
    Operation.ResearchEngine: {Material.TechnologyEngine: Integer(1)},
    Operation.ResearchLandfill: {Material.TechnologyLandfill: Integer(1)},
    Operation.ResearchLogistics2: {Material.TechnologyLogistics2: Integer(1)},
    Operation.ResearchToolbelt: {Material.TechnologyToolbelt: Integer(1)},
    Operation.ResearchStoneWall: {Material.TechnologyStoneWall: Integer(1)},
    Operation.ResearchGate: {Material.TechnologyGate: Integer(1)},
    Operation.ResearchChemicalSciencePack: {
        Material.TechnologyChemicalSciencePack: Integer(1)
    },
    Operation.ResearchMilitarySciencePack: {
        Material.TechnologyMilitarySciencePack: Integer(1)
    },
    Operation.ResearchProductionSciencePack: {
        Material.TechnologyProductionSciencePack: Integer(1)
    },
    Operation.ResearchUtilitySciencePack: {
        Material.TechnologyUtilitySciencePack: Integer(1)
    },
    Operation.ResearchSpaceSciencePack: {
        Material.TechnologySpaceSciencePack: Integer(1)
    },
    Operation.ResearchMilitary3: {Material.TechnologyMilitary3: Integer(1)},
    Operation.ResearchMilitary4: {Material.TechnologyMilitary4: Integer(1)},
    Operation.ResearchUraniumAmmo: {Material.TechnologyUraniumAmmo: Integer(1)},
    Operation.ResearchAtomicBomb: {Material.TechnologyAtomicBomb: Integer(1)},
    Operation.ResearchAutomation3: {Material.TechnologyAutomation3: Integer(1)},
    Operation.ResearchExplosives: {Material.TechnologyExplosives: Integer(1)},
    Operation.ResearchCliffExplosives: {Material.TechnologyCliffExplosives: Integer(1)},
    Operation.ResearchFlammables: {Material.TechnologyFlammables: Integer(1)},
    Operation.ResearchLandMine: {Material.TechnologyLandMine: Integer(1)},
    Operation.ResearchFlamethrower: {Material.TechnologyFlamethrower: Integer(1)},
    Operation.ResearchAdvancedCircuit: {Material.TechnologyAdvancedCircuit: Integer(1)},
    Operation.ResearchProcessingUnit: {Material.TechnologyProcessingUnit: Integer(1)},
    Operation.ResearchFluidWagon: {Material.TechnologyFluidWagon: Integer(1)},
    Operation.ResearchBrakingForce1: {Material.TechnologyBrakingForce1: Integer(1)},
    Operation.ResearchBrakingForce2: {Material.TechnologyBrakingForce2: Integer(1)},
    Operation.ResearchBrakingForce3: {Material.TechnologyBrakingForce3: Integer(1)},
    Operation.ResearchBrakingForce4: {Material.TechnologyBrakingForce4: Integer(1)},
    Operation.ResearchBrakingForce5: {Material.TechnologyBrakingForce5: Integer(1)},
    Operation.ResearchBrakingForce6: {Material.TechnologyBrakingForce6: Integer(1)},
    Operation.ResearchBrakingForce7: {Material.TechnologyBrakingForce7: Integer(1)},
    Operation.ResearchTank: {Material.TechnologyTank: Integer(1)},
    Operation.ResearchLogistics3: {Material.TechnologyLogistics3: Integer(1)},
    Operation.ResearchLaser: {Material.TechnologyLaser: Integer(1)},
    Operation.ResearchRocketry: {Material.TechnologyRocketry: Integer(1)},
    Operation.ResearchExplosiveRocketry: {
        Material.TechnologyExplosiveRocketry: Integer(1)
    },
    Operation.ResearchModularArmor: {Material.TechnologyModularArmor: Integer(1)},
    Operation.ResearchPowerArmor: {Material.TechnologyPowerArmor: Integer(1)},
    Operation.ResearchPowerArmorMk2: {Material.TechnologyPowerArmorMk2: Integer(1)},
    Operation.ResearchLaserTurret: {Material.TechnologyLaserTurret: Integer(1)},
    Operation.ResearchRobotics: {Material.TechnologyRobotics: Integer(1)},
    Operation.ResearchRocketFuel: {Material.TechnologyRocketFuel: Integer(1)},
    Operation.ResearchLowDensityStructure: {
        Material.TechnologyLowDensityStructure: Integer(1)
    },
    Operation.ResearchRocketSilo: {Material.TechnologyRocketSilo: Integer(1)},
    Operation.ResearchResearchSpeed3: {Material.TechnologyResearchSpeed3: Integer(1)},
    Operation.ResearchResearchSpeed4: {Material.TechnologyResearchSpeed4: Integer(1)},
    Operation.ResearchResearchSpeed5: {Material.TechnologyResearchSpeed5: Integer(1)},
    Operation.ResearchResearchSpeed6: {Material.TechnologyResearchSpeed6: Integer(1)},
    Operation.ResearchElectricEnergyDistribution2: {
        Material.TechnologyElectricEnergyDistribution2: Integer(1)
    },
    Operation.ResearchElectricEnergyAccumulators: {
        Material.TechnologyElectricEnergyAccumulators: Integer(1)
    },
    Operation.ResearchAdvancedMaterialProcessing2: {
        Material.TechnologyAdvancedMaterialProcessing2: Integer(1)
    },
    Operation.ResearchEffectTransmission: {
        Material.TechnologyEffectTransmission: Integer(1)
    },
    Operation.ResearchLubricant: {Material.TechnologyLubricant: Integer(1)},
    Operation.ResearchElectricEngine: {Material.TechnologyElectricEngine: Integer(1)},
    Operation.ResearchBattery: {Material.TechnologyBattery: Integer(1)},
    Operation.ResearchConstructionRobotics: {
        Material.TechnologyConstructionRobotics: Integer(1)
    },
    Operation.ResearchLogisticRobotics: {
        Material.TechnologyLogisticRobotics: Integer(1)
    },
    Operation.ResearchLogisticSystem: {Material.TechnologyLogisticSystem: Integer(1)},
    Operation.ResearchWorkerRobotsSpeed1: {
        Material.TechnologyWorkerRobotsSpeed1: Integer(1)
    },
    Operation.ResearchWorkerRobotsSpeed2: {
        Material.TechnologyWorkerRobotsSpeed2: Integer(1)
    },
    Operation.ResearchWorkerRobotsSpeed3: {
        Material.TechnologyWorkerRobotsSpeed3: Integer(1)
    },
    Operation.ResearchWorkerRobotsSpeed4: {
        Material.TechnologyWorkerRobotsSpeed4: Integer(1)
    },
    Operation.ResearchWorkerRobotsSpeed5: {
        Material.TechnologyWorkerRobotsSpeed5: Integer(1)
    },
    Operation.ResearchWorkerRobotsSpeed6: {
        Material.TechnologyWorkerRobotsSpeed6: Integer(1)
    },
    Operation.ResearchWorkerRobotsStorage1: {
        Material.TechnologyWorkerRobotsStorage1: Integer(1)
    },
    Operation.ResearchWorkerRobotsStorage2: {
        Material.TechnologyWorkerRobotsStorage2: Integer(1)
    },
    Operation.ResearchWorkerRobotsStorage3: {
        Material.TechnologyWorkerRobotsStorage3: Integer(1)
    },
    Operation.ResearchEnergyShieldEquipment: {
        Material.TechnologyEnergyShieldEquipment: Integer(1)
    },
    Operation.ResearchNightVisionEquipment: {
        Material.TechnologyNightVisionEquipment: Integer(1)
    },
    Operation.ResearchBeltImmunityEquipment: {
        Material.TechnologyBeltImmunityEquipment: Integer(1)
    },
    Operation.ResearchEnergyShieldMk2Equipment: {
        Material.TechnologyEnergyShieldMk2Equipment: Integer(1)
    },
    Operation.ResearchBatteryEquipment: {
        Material.TechnologyBatteryEquipment: Integer(1)
    },
    Operation.ResearchBatteryMk2Equipment: {
        Material.TechnologyBatteryMk2Equipment: Integer(1)
    },
    Operation.ResearchSolarPanelEquipment: {
        Material.TechnologySolarPanelEquipment: Integer(1)
    },
    Operation.ResearchPersonalLaserDefenseEquipment: {
        Material.TechnologyPersonalLaserDefenseEquipment: Integer(1)
    },
    Operation.ResearchDischargeDefenseEquipment: {
        Material.TechnologyDischargeDefenseEquipment: Integer(1)
    },
    Operation.ResearchFissionReactorEquipment: {
        Material.TechnologyFissionReactorEquipment: Integer(1)
    },
    Operation.ResearchExoskeletonEquipment: {
        Material.TechnologyExoskeletonEquipment: Integer(1)
    },
    Operation.ResearchPersonalRoboportEquipment: {
        Material.TechnologyPersonalRoboportEquipment: Integer(1)
    },
    Operation.ResearchPersonalRoboportMk2Equipment: {
        Material.TechnologyPersonalRoboportMk2Equipment: Integer(1)
    },
    Operation.ResearchFluidHandling: {Material.TechnologyFluidHandling: Integer(1)},
    Operation.ResearchOilGathering: {Material.TechnologyOilGathering: Integer(1)},
    Operation.ResearchOilProcessing: {Material.TechnologyOilProcessing: Integer(1)},
    Operation.ResearchAdvancedOilProcessing: {
        Material.TechnologyAdvancedOilProcessing: Integer(1)
    },
    Operation.ResearchCoalLiquefaction: {
        Material.TechnologyCoalLiquefaction: Integer(1)
    },
    Operation.ResearchSulfurProcessing: {
        Material.TechnologySulfurProcessing: Integer(1)
    },
    Operation.ResearchPlastics: {Material.TechnologyPlastics: Integer(1)},
    Operation.ResearchModules: {Material.TechnologyModules: Integer(1)},
    Operation.ResearchSpeedModule: {Material.TechnologySpeedModule: Integer(1)},
    Operation.ResearchSpeedModule2: {Material.TechnologySpeedModule2: Integer(1)},
    Operation.ResearchSpeedModule3: {Material.TechnologySpeedModule3: Integer(1)},
    Operation.ResearchProductivityModule: {
        Material.TechnologyProductivityModule: Integer(1)
    },
    Operation.ResearchProductivityModule2: {
        Material.TechnologyProductivityModule2: Integer(1)
    },
    Operation.ResearchProductivityModule3: {
        Material.TechnologyProductivityModule3: Integer(1)
    },
    Operation.ResearchEfficiencyModule: {
        Material.TechnologyEfficiencyModule: Integer(1)
    },
    Operation.ResearchEfficiencyModule2: {
        Material.TechnologyEfficiencyModule2: Integer(1)
    },
    Operation.ResearchEfficiencyModule3: {
        Material.TechnologyEfficiencyModule3: Integer(1)
    },
    Operation.ResearchDefender: {Material.TechnologyDefender: Integer(1)},
    Operation.ResearchDistractor: {Material.TechnologyDistractor: Integer(1)},
    Operation.ResearchDestroyer: {Material.TechnologyDestroyer: Integer(1)},
    Operation.ResearchUraniumMining: {Material.TechnologyUraniumMining: Integer(1)},
    Operation.ResearchUraniumProcessing: {
        Material.TechnologyUraniumProcessing: Integer(1)
    },
    Operation.ResearchNuclearPower: {Material.TechnologyNuclearPower: Integer(1)},
    Operation.ResearchKovarexEnrichmentProcess: {
        Material.TechnologyKovarexEnrichmentProcess: Integer(1)
    },
    Operation.ResearchNuclearFuelReprocessing: {
        Material.TechnologyNuclearFuelReprocessing: Integer(1)
    },
    Operation.ResearchMiningProductivity1: {
        Material.TechnologyMiningProductivity1: Integer(1)
    },
    Operation.ResearchMiningProductivity2: {
        Material.TechnologyMiningProductivity2: Integer(1)
    },
    Operation.ResearchMiningProductivity3: {
        Material.TechnologyMiningProductivity3: Integer(1)
    },
    Operation.ResearchMiningProductivity4: {
        Material.TechnologyMiningProductivity4: Integer(1)
    },
    Operation.ResearchArtillery: {Material.TechnologyArtillery: Integer(1)},
    Operation.ResearchSpidertron: {Material.TechnologySpidertron: Integer(1)},
    Operation.ResearchCircuitNetwork: {Material.TechnologyCircuitNetwork: Integer(1)},
    Operation.ResearchAdvancedCombinators: {
        Material.TechnologyAdvancedCombinators: Integer(1)
    },
    Operation.MiningIronOre: {Material.IronOre: Integer(1)},
    Operation.MiningCopperOre: {Material.CopperOre: Integer(1)},
    Operation.MiningCoal: {Material.Coal: Integer(1)},
    Operation.MiningStone: {Material.Stone: Integer(1)},
    Operation.MiningUraniumOre: {Material.UraniumOre: Integer(1)},
    Operation.MiningCrudeOil: {Material.CrudeOil: Integer(10)},
}

CATEGORY_OF_RECIPE: dict[Operation, OperationCategory] = {
    Operation.SpeedModule: OperationCategory.Crafting,
    Operation.SpeedModule2: OperationCategory.Crafting,
    Operation.SpeedModule3: OperationCategory.Crafting,
    Operation.ProductivityModule: OperationCategory.Crafting,
    Operation.ProductivityModule2: OperationCategory.Crafting,
    Operation.ProductivityModule3: OperationCategory.Crafting,
    Operation.EfficiencyModule: OperationCategory.Crafting,
    Operation.EfficiencyModule2: OperationCategory.Crafting,
    Operation.EfficiencyModule3: OperationCategory.Crafting,
    Operation.BulkInserter: OperationCategory.Crafting,
    Operation.BasicOilProcessing: OperationCategory.OilProcessing,
    Operation.AdvancedOilProcessing: OperationCategory.OilProcessing,
    Operation.CoalLiquefaction: OperationCategory.OilProcessing,
    Operation.HeavyOilCracking: OperationCategory.Chemistry,
    Operation.LightOilCracking: OperationCategory.Chemistry,
    Operation.SulfuricAcid: OperationCategory.Chemistry,
    Operation.PlasticBar: OperationCategory.Chemistry,
    Operation.SolidFuelFromLightOil: OperationCategory.Chemistry,
    Operation.SolidFuelFromPetroleumGas: OperationCategory.Chemistry,
    Operation.SolidFuelFromHeavyOil: OperationCategory.Chemistry,
    Operation.Sulfur: OperationCategory.Chemistry,
    Operation.Lubricant: OperationCategory.Chemistry,
    Operation.Barrel: OperationCategory.Crafting,
    Operation.NightVisionEquipment: OperationCategory.Crafting,
    Operation.BeltImmunityEquipment: OperationCategory.Crafting,
    Operation.EnergyShieldEquipment: OperationCategory.Crafting,
    Operation.EnergyShieldMk2Equipment: OperationCategory.Crafting,
    Operation.BatteryEquipment: OperationCategory.Crafting,
    Operation.BatteryMk2Equipment: OperationCategory.Crafting,
    Operation.SolarPanelEquipment: OperationCategory.Crafting,
    Operation.FissionReactorEquipment: OperationCategory.Crafting,
    Operation.PersonalLaserDefenseEquipment: OperationCategory.Crafting,
    Operation.DischargeDefenseEquipment: OperationCategory.Crafting,
    Operation.ExoskeletonEquipment: OperationCategory.Crafting,
    Operation.PersonalRoboportEquipment: OperationCategory.Crafting,
    Operation.PersonalRoboportMk2Equipment: OperationCategory.Crafting,
    Operation.LaserTurret: OperationCategory.Crafting,
    Operation.FlamethrowerTurret: OperationCategory.Crafting,
    Operation.ArtilleryTurret: OperationCategory.Crafting,
    Operation.GunTurret: OperationCategory.Crafting,
    Operation.WoodenChest: OperationCategory.Crafting,
    Operation.DisplayPanel: OperationCategory.Crafting,
    Operation.IronStick: OperationCategory.Crafting,
    Operation.StoneFurnace: OperationCategory.Crafting,
    Operation.Boiler: OperationCategory.Crafting,
    Operation.SteamEngine: OperationCategory.Crafting,
    Operation.IronGearWheel: OperationCategory.Crafting,
    Operation.ElectronicCircuit: OperationCategory.Crafting,
    Operation.TransportBelt: OperationCategory.Crafting,
    Operation.ElectricMiningDrill: OperationCategory.Crafting,
    Operation.BurnerMiningDrill: OperationCategory.Crafting,
    Operation.Inserter: OperationCategory.Crafting,
    Operation.FastInserter: OperationCategory.Crafting,
    Operation.LongHandedInserter: OperationCategory.Crafting,
    Operation.BurnerInserter: OperationCategory.Crafting,
    Operation.Pipe: OperationCategory.Crafting,
    Operation.OffshorePump: OperationCategory.Crafting,
    Operation.CopperCable: OperationCategory.Crafting,
    Operation.SmallElectricPole: OperationCategory.Crafting,
    Operation.Pistol: OperationCategory.Crafting,
    Operation.SubmachineGun: OperationCategory.Crafting,
    Operation.FirearmMagazine: OperationCategory.Crafting,
    Operation.LightArmor: OperationCategory.Crafting,
    Operation.Radar: OperationCategory.Crafting,
    Operation.SmallLamp: OperationCategory.Crafting,
    Operation.PipeToGround: OperationCategory.Crafting,
    Operation.AssemblingMachine1: OperationCategory.Crafting,
    Operation.RepairPack: OperationCategory.Crafting,
    Operation.AutomationSciencePack: OperationCategory.Crafting,
    Operation.LogisticSciencePack: OperationCategory.Crafting,
    Operation.Lab: OperationCategory.Crafting,
    Operation.StoneWall: OperationCategory.Crafting,
    Operation.AssemblingMachine2: OperationCategory.Crafting,
    Operation.Splitter: OperationCategory.Crafting,
    Operation.UndergroundBelt: OperationCategory.Crafting,
    Operation.Loader: OperationCategory.Crafting,
    Operation.Car: OperationCategory.Crafting,
    Operation.EngineUnit: OperationCategory.AdvancedCrafting,
    Operation.IronChest: OperationCategory.Crafting,
    Operation.BigElectricPole: OperationCategory.Crafting,
    Operation.MediumElectricPole: OperationCategory.Crafting,
    Operation.Shotgun: OperationCategory.Crafting,
    Operation.ShotgunShell: OperationCategory.Crafting,
    Operation.PiercingRoundsMagazine: OperationCategory.Crafting,
    Operation.Grenade: OperationCategory.Crafting,
    Operation.SteelFurnace: OperationCategory.Crafting,
    Operation.Gate: OperationCategory.Crafting,
    Operation.HeavyArmor: OperationCategory.Crafting,
    Operation.SteelChest: OperationCategory.Crafting,
    Operation.FastUndergroundBelt: OperationCategory.Crafting,
    Operation.FastSplitter: OperationCategory.Crafting,
    Operation.Concrete: OperationCategory.CraftingWithFluid,
    Operation.HazardConcrete: OperationCategory.Crafting,
    Operation.RefinedConcrete: OperationCategory.CraftingWithFluid,
    Operation.RefinedHazardConcrete: OperationCategory.Crafting,
    Operation.Landfill: OperationCategory.Crafting,
    Operation.FastTransportBelt: OperationCategory.Crafting,
    Operation.SolarPanel: OperationCategory.Crafting,
    Operation.Rail: OperationCategory.Crafting,
    Operation.Locomotive: OperationCategory.Crafting,
    Operation.CargoWagon: OperationCategory.Crafting,
    Operation.RailSignal: OperationCategory.Crafting,
    Operation.RailChainSignal: OperationCategory.Crafting,
    Operation.TrainStop: OperationCategory.Crafting,
    Operation.CopperPlate: OperationCategory.Smelting,
    Operation.IronPlate: OperationCategory.Smelting,
    Operation.StoneBrick: OperationCategory.Smelting,
    Operation.SteelPlate: OperationCategory.Smelting,
    Operation.ArithmeticCombinator: OperationCategory.Crafting,
    Operation.DeciderCombinator: OperationCategory.Crafting,
    Operation.ConstantCombinator: OperationCategory.Crafting,
    Operation.SelectorCombinator: OperationCategory.Crafting,
    Operation.PowerSwitch: OperationCategory.Crafting,
    Operation.ProgrammableSpeaker: OperationCategory.Crafting,
    Operation.PoisonCapsule: OperationCategory.Crafting,
    Operation.SlowdownCapsule: OperationCategory.Crafting,
    Operation.ClusterGrenade: OperationCategory.Crafting,
    Operation.DefenderCapsule: OperationCategory.Crafting,
    Operation.DistractorCapsule: OperationCategory.Crafting,
    Operation.DestroyerCapsule: OperationCategory.Crafting,
    Operation.CliffExplosives: OperationCategory.Crafting,
    Operation.UraniumRoundsMagazine: OperationCategory.Crafting,
    Operation.Rocket: OperationCategory.Crafting,
    Operation.ExplosiveRocket: OperationCategory.Crafting,
    Operation.AtomicBomb: OperationCategory.Crafting,
    Operation.PiercingShotgunShell: OperationCategory.Crafting,
    Operation.CannonShell: OperationCategory.Crafting,
    Operation.ExplosiveCannonShell: OperationCategory.Crafting,
    Operation.UraniumCannonShell: OperationCategory.Crafting,
    Operation.ExplosiveUraniumCannonShell: OperationCategory.Crafting,
    Operation.ArtilleryShell: OperationCategory.Crafting,
    Operation.FlamethrowerAmmo: OperationCategory.Chemistry,
    Operation.ExpressTransportBelt: OperationCategory.CraftingWithFluid,
    Operation.AssemblingMachine3: OperationCategory.Crafting,
    Operation.Tank: OperationCategory.Crafting,
    Operation.Spidertron: OperationCategory.Crafting,
    Operation.FluidWagon: OperationCategory.Crafting,
    Operation.ArtilleryWagon: OperationCategory.Crafting,
    Operation.ModularArmor: OperationCategory.Crafting,
    Operation.PowerArmor: OperationCategory.Crafting,
    Operation.PowerArmorMk2: OperationCategory.Crafting,
    Operation.Flamethrower: OperationCategory.Crafting,
    Operation.LandMine: OperationCategory.Crafting,
    Operation.RocketLauncher: OperationCategory.Crafting,
    Operation.CombatShotgun: OperationCategory.Crafting,
    Operation.ChemicalSciencePack: OperationCategory.Crafting,
    Operation.MilitarySciencePack: OperationCategory.Crafting,
    Operation.ProductionSciencePack: OperationCategory.Crafting,
    Operation.UtilitySciencePack: OperationCategory.Crafting,
    Operation.ExpressUndergroundBelt: OperationCategory.CraftingWithFluid,
    Operation.FastLoader: OperationCategory.Crafting,
    Operation.ExpressLoader: OperationCategory.Crafting,
    Operation.ExpressSplitter: OperationCategory.CraftingWithFluid,
    Operation.AdvancedCircuit: OperationCategory.Crafting,
    Operation.ProcessingUnit: OperationCategory.CraftingWithFluid,
    Operation.LogisticRobot: OperationCategory.Crafting,
    Operation.ConstructionRobot: OperationCategory.Crafting,
    Operation.PassiveProviderChest: OperationCategory.Crafting,
    Operation.ActiveProviderChest: OperationCategory.Crafting,
    Operation.StorageChest: OperationCategory.Crafting,
    Operation.BufferChest: OperationCategory.Crafting,
    Operation.RequesterChest: OperationCategory.Crafting,
    Operation.RocketSilo: OperationCategory.Crafting,
    Operation.CargoLandingPad: OperationCategory.Crafting,
    Operation.Roboport: OperationCategory.Crafting,
    Operation.Substation: OperationCategory.Crafting,
    Operation.Accumulator: OperationCategory.Crafting,
    Operation.ElectricFurnace: OperationCategory.Crafting,
    Operation.Beacon: OperationCategory.Crafting,
    Operation.Pumpjack: OperationCategory.Crafting,
    Operation.OilRefinery: OperationCategory.Crafting,
    Operation.ElectricEngineUnit: OperationCategory.CraftingWithFluid,
    Operation.FlyingRobotFrame: OperationCategory.Crafting,
    Operation.Explosives: OperationCategory.Chemistry,
    Operation.Battery: OperationCategory.Chemistry,
    Operation.StorageTank: OperationCategory.Crafting,
    Operation.Pump: OperationCategory.Crafting,
    Operation.ChemicalPlant: OperationCategory.Crafting,
    Operation.LowDensityStructure: OperationCategory.Crafting,
    Operation.RocketFuel: OperationCategory.CraftingWithFluid,
    Operation.RocketPart: OperationCategory.RocketBuilding,
    Operation.Satellite: OperationCategory.Crafting,
    Operation.NuclearReactor: OperationCategory.Crafting,
    Operation.Centrifuge: OperationCategory.Crafting,
    Operation.UraniumProcessing: OperationCategory.Centrifuging,
    Operation.KovarexEnrichmentProcess: OperationCategory.Centrifuging,
    Operation.NuclearFuel: OperationCategory.Centrifuging,
    Operation.NuclearFuelReprocessing: OperationCategory.Centrifuging,
    Operation.UraniumFuelCell: OperationCategory.Crafting,
    Operation.HeatExchanger: OperationCategory.Crafting,
    Operation.HeatPipe: OperationCategory.Crafting,
    Operation.SteamTurbine: OperationCategory.Crafting,
    Operation.ResearchSteamPower: OperationCategory.Research,
    Operation.ResearchElectronics: OperationCategory.Research,
    Operation.ResearchAutomationSciencePack: OperationCategory.Research,
    Operation.ResearchElectricMiningDrill: OperationCategory.Research,
    Operation.ResearchRepairPack: OperationCategory.Research,
    Operation.ResearchRadar: OperationCategory.Research,
    Operation.ResearchPhysicalProjectileDamage1: OperationCategory.Research,
    Operation.ResearchPhysicalProjectileDamage2: OperationCategory.Research,
    Operation.ResearchWeaponShootingSpeed1: OperationCategory.Research,
    Operation.ResearchWeaponShootingSpeed2: OperationCategory.Research,
    Operation.ResearchStrongerExplosives1: OperationCategory.Research,
    Operation.ResearchPhysicalProjectileDamage3: OperationCategory.Research,
    Operation.ResearchPhysicalProjectileDamage4: OperationCategory.Research,
    Operation.ResearchPhysicalProjectileDamage5: OperationCategory.Research,
    Operation.ResearchPhysicalProjectileDamage6: OperationCategory.Research,
    Operation.ResearchPhysicalProjectileDamage7: OperationCategory.Research,
    Operation.ResearchStrongerExplosives2: OperationCategory.Research,
    Operation.ResearchStrongerExplosives3: OperationCategory.Research,
    Operation.ResearchStrongerExplosives4: OperationCategory.Research,
    Operation.ResearchStrongerExplosives5: OperationCategory.Research,
    Operation.ResearchStrongerExplosives6: OperationCategory.Research,
    Operation.ResearchStrongerExplosives7: OperationCategory.Research,
    Operation.ResearchRefinedFlammables1: OperationCategory.Research,
    Operation.ResearchRefinedFlammables2: OperationCategory.Research,
    Operation.ResearchRefinedFlammables3: OperationCategory.Research,
    Operation.ResearchRefinedFlammables4: OperationCategory.Research,
    Operation.ResearchRefinedFlammables5: OperationCategory.Research,
    Operation.ResearchRefinedFlammables6: OperationCategory.Research,
    Operation.ResearchRefinedFlammables7: OperationCategory.Research,
    Operation.ResearchLaserWeaponsDamage1: OperationCategory.Research,
    Operation.ResearchLaserWeaponsDamage2: OperationCategory.Research,
    Operation.ResearchLaserWeaponsDamage3: OperationCategory.Research,
    Operation.ResearchLaserWeaponsDamage4: OperationCategory.Research,
    Operation.ResearchLaserWeaponsDamage5: OperationCategory.Research,
    Operation.ResearchLaserWeaponsDamage6: OperationCategory.Research,
    Operation.ResearchLaserWeaponsDamage7: OperationCategory.Research,
    Operation.ResearchWeaponShootingSpeed3: OperationCategory.Research,
    Operation.ResearchWeaponShootingSpeed4: OperationCategory.Research,
    Operation.ResearchWeaponShootingSpeed5: OperationCategory.Research,
    Operation.ResearchWeaponShootingSpeed6: OperationCategory.Research,
    Operation.ResearchLaserShootingSpeed1: OperationCategory.Research,
    Operation.ResearchLaserShootingSpeed2: OperationCategory.Research,
    Operation.ResearchLaserShootingSpeed3: OperationCategory.Research,
    Operation.ResearchLaserShootingSpeed4: OperationCategory.Research,
    Operation.ResearchLaserShootingSpeed5: OperationCategory.Research,
    Operation.ResearchLaserShootingSpeed6: OperationCategory.Research,
    Operation.ResearchLaserShootingSpeed7: OperationCategory.Research,
    Operation.ResearchArtilleryShellRange1: OperationCategory.Research,
    Operation.ResearchArtilleryShellSpeed1: OperationCategory.Research,
    Operation.ResearchFollowerRobotCount5: OperationCategory.Research,
    Operation.ResearchBulkInserter: OperationCategory.Research,
    Operation.ResearchInserterCapacityBonus1: OperationCategory.Research,
    Operation.ResearchInserterCapacityBonus2: OperationCategory.Research,
    Operation.ResearchInserterCapacityBonus3: OperationCategory.Research,
    Operation.ResearchInserterCapacityBonus4: OperationCategory.Research,
    Operation.ResearchInserterCapacityBonus5: OperationCategory.Research,
    Operation.ResearchInserterCapacityBonus6: OperationCategory.Research,
    Operation.ResearchInserterCapacityBonus7: OperationCategory.Research,
    Operation.ResearchAutomation: OperationCategory.Research,
    Operation.ResearchAutomation2: OperationCategory.Research,
    Operation.ResearchLogisticSciencePack: OperationCategory.Research,
    Operation.ResearchSteelProcessing: OperationCategory.Research,
    Operation.ResearchSteelAxe: OperationCategory.Research,
    Operation.ResearchMilitary: OperationCategory.Research,
    Operation.ResearchMilitary2: OperationCategory.Research,
    Operation.ResearchFastInserter: OperationCategory.Research,
    Operation.ResearchLogistics: OperationCategory.Research,
    Operation.ResearchRailway: OperationCategory.Research,
    Operation.ResearchAutomatedRailTransportation: OperationCategory.Research,
    Operation.ResearchAutomobilism: OperationCategory.Research,
    Operation.ResearchLamp: OperationCategory.Research,
    Operation.ResearchSolarEnergy: OperationCategory.Research,
    Operation.ResearchHeavyArmor: OperationCategory.Research,
    Operation.ResearchGunTurret: OperationCategory.Research,
    Operation.ResearchResearchSpeed1: OperationCategory.Research,
    Operation.ResearchResearchSpeed2: OperationCategory.Research,
    Operation.ResearchElectricEnergyDistribution1: OperationCategory.Research,
    Operation.ResearchAdvancedMaterialProcessing: OperationCategory.Research,
    Operation.ResearchConcrete: OperationCategory.Research,
    Operation.ResearchEngine: OperationCategory.Research,
    Operation.ResearchLandfill: OperationCategory.Research,
    Operation.ResearchLogistics2: OperationCategory.Research,
    Operation.ResearchToolbelt: OperationCategory.Research,
    Operation.ResearchStoneWall: OperationCategory.Research,
    Operation.ResearchGate: OperationCategory.Research,
    Operation.ResearchChemicalSciencePack: OperationCategory.Research,
    Operation.ResearchMilitarySciencePack: OperationCategory.Research,
    Operation.ResearchProductionSciencePack: OperationCategory.Research,
    Operation.ResearchUtilitySciencePack: OperationCategory.Research,
    Operation.ResearchSpaceSciencePack: OperationCategory.Research,
    Operation.ResearchMilitary3: OperationCategory.Research,
    Operation.ResearchMilitary4: OperationCategory.Research,
    Operation.ResearchUraniumAmmo: OperationCategory.Research,
    Operation.ResearchAtomicBomb: OperationCategory.Research,
    Operation.ResearchAutomation3: OperationCategory.Research,
    Operation.ResearchExplosives: OperationCategory.Research,
    Operation.ResearchCliffExplosives: OperationCategory.Research,
    Operation.ResearchFlammables: OperationCategory.Research,
    Operation.ResearchLandMine: OperationCategory.Research,
    Operation.ResearchFlamethrower: OperationCategory.Research,
    Operation.ResearchAdvancedCircuit: OperationCategory.Research,
    Operation.ResearchProcessingUnit: OperationCategory.Research,
    Operation.ResearchFluidWagon: OperationCategory.Research,
    Operation.ResearchBrakingForce1: OperationCategory.Research,
    Operation.ResearchBrakingForce2: OperationCategory.Research,
    Operation.ResearchBrakingForce3: OperationCategory.Research,
    Operation.ResearchBrakingForce4: OperationCategory.Research,
    Operation.ResearchBrakingForce5: OperationCategory.Research,
    Operation.ResearchBrakingForce6: OperationCategory.Research,
    Operation.ResearchBrakingForce7: OperationCategory.Research,
    Operation.ResearchTank: OperationCategory.Research,
    Operation.ResearchLogistics3: OperationCategory.Research,
    Operation.ResearchLaser: OperationCategory.Research,
    Operation.ResearchRocketry: OperationCategory.Research,
    Operation.ResearchExplosiveRocketry: OperationCategory.Research,
    Operation.ResearchModularArmor: OperationCategory.Research,
    Operation.ResearchPowerArmor: OperationCategory.Research,
    Operation.ResearchPowerArmorMk2: OperationCategory.Research,
    Operation.ResearchLaserTurret: OperationCategory.Research,
    Operation.ResearchRobotics: OperationCategory.Research,
    Operation.ResearchRocketFuel: OperationCategory.Research,
    Operation.ResearchLowDensityStructure: OperationCategory.Research,
    Operation.ResearchRocketSilo: OperationCategory.Research,
    Operation.ResearchResearchSpeed3: OperationCategory.Research,
    Operation.ResearchResearchSpeed4: OperationCategory.Research,
    Operation.ResearchResearchSpeed5: OperationCategory.Research,
    Operation.ResearchResearchSpeed6: OperationCategory.Research,
    Operation.ResearchElectricEnergyDistribution2: OperationCategory.Research,
    Operation.ResearchElectricEnergyAccumulators: OperationCategory.Research,
    Operation.ResearchAdvancedMaterialProcessing2: OperationCategory.Research,
    Operation.ResearchEffectTransmission: OperationCategory.Research,
    Operation.ResearchLubricant: OperationCategory.Research,
    Operation.ResearchElectricEngine: OperationCategory.Research,
    Operation.ResearchBattery: OperationCategory.Research,
    Operation.ResearchConstructionRobotics: OperationCategory.Research,
    Operation.ResearchLogisticRobotics: OperationCategory.Research,
    Operation.ResearchLogisticSystem: OperationCategory.Research,
    Operation.ResearchWorkerRobotsSpeed1: OperationCategory.Research,
    Operation.ResearchWorkerRobotsSpeed2: OperationCategory.Research,
    Operation.ResearchWorkerRobotsSpeed3: OperationCategory.Research,
    Operation.ResearchWorkerRobotsSpeed4: OperationCategory.Research,
    Operation.ResearchWorkerRobotsSpeed5: OperationCategory.Research,
    Operation.ResearchWorkerRobotsSpeed6: OperationCategory.Research,
    Operation.ResearchWorkerRobotsStorage1: OperationCategory.Research,
    Operation.ResearchWorkerRobotsStorage2: OperationCategory.Research,
    Operation.ResearchWorkerRobotsStorage3: OperationCategory.Research,
    Operation.ResearchEnergyShieldEquipment: OperationCategory.Research,
    Operation.ResearchNightVisionEquipment: OperationCategory.Research,
    Operation.ResearchBeltImmunityEquipment: OperationCategory.Research,
    Operation.ResearchEnergyShieldMk2Equipment: OperationCategory.Research,
    Operation.ResearchBatteryEquipment: OperationCategory.Research,
    Operation.ResearchBatteryMk2Equipment: OperationCategory.Research,
    Operation.ResearchSolarPanelEquipment: OperationCategory.Research,
    Operation.ResearchPersonalLaserDefenseEquipment: OperationCategory.Research,
    Operation.ResearchDischargeDefenseEquipment: OperationCategory.Research,
    Operation.ResearchFissionReactorEquipment: OperationCategory.Research,
    Operation.ResearchExoskeletonEquipment: OperationCategory.Research,
    Operation.ResearchPersonalRoboportEquipment: OperationCategory.Research,
    Operation.ResearchPersonalRoboportMk2Equipment: OperationCategory.Research,
    Operation.ResearchFluidHandling: OperationCategory.Research,
    Operation.ResearchOilGathering: OperationCategory.Research,
    Operation.ResearchOilProcessing: OperationCategory.Research,
    Operation.ResearchAdvancedOilProcessing: OperationCategory.Research,
    Operation.ResearchCoalLiquefaction: OperationCategory.Research,
    Operation.ResearchSulfurProcessing: OperationCategory.Research,
    Operation.ResearchPlastics: OperationCategory.Research,
    Operation.ResearchModules: OperationCategory.Research,
    Operation.ResearchSpeedModule: OperationCategory.Research,
    Operation.ResearchSpeedModule2: OperationCategory.Research,
    Operation.ResearchSpeedModule3: OperationCategory.Research,
    Operation.ResearchProductivityModule: OperationCategory.Research,
    Operation.ResearchProductivityModule2: OperationCategory.Research,
    Operation.ResearchProductivityModule3: OperationCategory.Research,
    Operation.ResearchEfficiencyModule: OperationCategory.Research,
    Operation.ResearchEfficiencyModule2: OperationCategory.Research,
    Operation.ResearchEfficiencyModule3: OperationCategory.Research,
    Operation.ResearchDefender: OperationCategory.Research,
    Operation.ResearchDistractor: OperationCategory.Research,
    Operation.ResearchDestroyer: OperationCategory.Research,
    Operation.ResearchUraniumMining: OperationCategory.Research,
    Operation.ResearchUraniumProcessing: OperationCategory.Research,
    Operation.ResearchNuclearPower: OperationCategory.Research,
    Operation.ResearchKovarexEnrichmentProcess: OperationCategory.Research,
    Operation.ResearchNuclearFuelReprocessing: OperationCategory.Research,
    Operation.ResearchMiningProductivity1: OperationCategory.Research,
    Operation.ResearchMiningProductivity2: OperationCategory.Research,
    Operation.ResearchMiningProductivity3: OperationCategory.Research,
    Operation.ResearchMiningProductivity4: OperationCategory.Research,
    Operation.ResearchArtillery: OperationCategory.Research,
    Operation.ResearchSpidertron: OperationCategory.Research,
    Operation.ResearchCircuitNetwork: OperationCategory.Research,
    Operation.ResearchAdvancedCombinators: OperationCategory.Research,
    Operation.MiningIronOre: OperationCategory.Mining,
    Operation.MiningCopperOre: OperationCategory.Mining,
    Operation.MiningCoal: OperationCategory.Mining,
    Operation.MiningStone: OperationCategory.Mining,
    Operation.MiningUraniumOre: OperationCategory.Mining,
    Operation.MiningCrudeOil: OperationCategory.Mining,
}
