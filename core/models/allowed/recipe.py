from core.enums.operation import Operation

recipe_allowed: set[Operation] = {
    Operation.SpeedModule,
    Operation.SpeedModule2,
    Operation.SpeedModule3,
    Operation.ProductivityModule,
    Operation.ProductivityModule2,
    Operation.ProductivityModule3,
    Operation.EfficiencyModule,
    Operation.EfficiencyModule2,
    Operation.EfficiencyModule3,
    Operation.BulkInserter,
    Operation.BasicOilProcessing,
    Operation.AdvancedOilProcessing,
    Operation.CoalLiquefaction,
    Operation.HeavyOilCracking,
    Operation.LightOilCracking,
    Operation.SulfuricAcid,
    Operation.PlasticBar,
    Operation.SolidFuelFromLightOil,
    Operation.SolidFuelFromPetroleumGas,
    Operation.SolidFuelFromHeavyOil,
    Operation.Sulfur,
    Operation.Lubricant,
    Operation.Barrel,
    Operation.NightVisionEquipment,
    Operation.BeltImmunityEquipment,
    Operation.EnergyShieldEquipment,
    Operation.EnergyShieldMk2Equipment,
    Operation.BatteryEquipment,
    Operation.BatteryMk2Equipment,
    Operation.SolarPanelEquipment,
    Operation.FissionReactorEquipment,
    Operation.PersonalLaserDefenseEquipment,
    Operation.DischargeDefenseEquipment,
    Operation.ExoskeletonEquipment,
    Operation.PersonalRoboportEquipment,
    Operation.PersonalRoboportMk2Equipment,
    Operation.LaserTurret,
    Operation.FlamethrowerTurret,
    Operation.ArtilleryTurret,
    Operation.GunTurret,
    Operation.WoodenChest,
    Operation.DisplayPanel,
    Operation.IronStick,
    Operation.StoneFurnace,
    Operation.Boiler,
    Operation.SteamEngine,
    Operation.IronGearWheel,
    Operation.ElectronicCircuit,
    Operation.TransportBelt,
    Operation.ElectricMiningDrill,
    Operation.BurnerMiningDrill,
    Operation.Inserter,
    Operation.FastInserter,
    Operation.LongHandedInserter,
    Operation.BurnerInserter,
    Operation.Pipe,
    Operation.OffshorePump,
    Operation.CopperCable,
    Operation.SmallElectricPole,
    Operation.Pistol,
    Operation.SubmachineGun,
    Operation.FirearmMagazine,
    Operation.LightArmor,
    Operation.Radar,
    Operation.SmallLamp,
    Operation.PipeToGround,
    Operation.AssemblingMachine1,
    Operation.RepairPack,
    Operation.AutomationSciencePack,
    Operation.LogisticSciencePack,
    Operation.Lab,
    Operation.StoneWall,
    Operation.AssemblingMachine2,
    Operation.Splitter,
    Operation.UndergroundBelt,
    Operation.Loader,
    Operation.Car,
    Operation.EngineUnit,
    Operation.IronChest,
    Operation.BigElectricPole,
    Operation.MediumElectricPole,
    Operation.Shotgun,
    Operation.ShotgunShell,
    Operation.PiercingRoundsMagazine,
    Operation.Grenade,
    Operation.SteelFurnace,
    Operation.Gate,
    Operation.HeavyArmor,
    Operation.SteelChest,
    Operation.FastUndergroundBelt,
    Operation.FastSplitter,
    Operation.Concrete,
    Operation.HazardConcrete,
    Operation.RefinedConcrete,
    Operation.RefinedHazardConcrete,
    Operation.Landfill,
    Operation.FastTransportBelt,
    Operation.SolarPanel,
    Operation.Rail,
    Operation.Locomotive,
    Operation.CargoWagon,
    Operation.RailSignal,
    Operation.RailChainSignal,
    Operation.TrainStop,
    Operation.CopperPlate,
    Operation.IronPlate,
    Operation.StoneBrick,
    Operation.SteelPlate,
    Operation.ArithmeticCombinator,
    Operation.DeciderCombinator,
    Operation.ConstantCombinator,
    Operation.SelectorCombinator,
    Operation.PowerSwitch,
    Operation.ProgrammableSpeaker,
    Operation.PoisonCapsule,
    Operation.SlowdownCapsule,
    Operation.ClusterGrenade,
    Operation.DefenderCapsule,
    Operation.DistractorCapsule,
    Operation.DestroyerCapsule,
    Operation.CliffExplosives,
    Operation.UraniumRoundsMagazine,
    Operation.Rocket,
    Operation.ExplosiveRocket,
    Operation.AtomicBomb,
    Operation.PiercingShotgunShell,
    Operation.CannonShell,
    Operation.ExplosiveCannonShell,
    Operation.UraniumCannonShell,
    Operation.ExplosiveUraniumCannonShell,
    Operation.ArtilleryShell,
    Operation.FlamethrowerAmmo,
    Operation.ExpressTransportBelt,
    Operation.AssemblingMachine3,
    Operation.Tank,
    Operation.Spidertron,
    Operation.FluidWagon,
    Operation.ArtilleryWagon,
    Operation.ModularArmor,
    Operation.PowerArmor,
    Operation.PowerArmorMk2,
    Operation.Flamethrower,
    Operation.LandMine,
    Operation.RocketLauncher,
    Operation.CombatShotgun,
    Operation.ChemicalSciencePack,
    Operation.MilitarySciencePack,
    Operation.ProductionSciencePack,
    Operation.UtilitySciencePack,
    Operation.ExpressUndergroundBelt,
    Operation.FastLoader,
    Operation.ExpressLoader,
    Operation.ExpressSplitter,
    Operation.AdvancedCircuit,
    Operation.ProcessingUnit,
    Operation.LogisticRobot,
    Operation.ConstructionRobot,
    Operation.PassiveProviderChest,
    Operation.ActiveProviderChest,
    Operation.StorageChest,
    Operation.BufferChest,
    Operation.RequesterChest,
    Operation.RocketSilo,
    Operation.CargoLandingPad,
    Operation.Roboport,
    Operation.Substation,
    Operation.Accumulator,
    Operation.ElectricFurnace,
    Operation.Beacon,
    Operation.Pumpjack,
    Operation.OilRefinery,
    Operation.ElectricEngineUnit,
    Operation.FlyingRobotFrame,
    Operation.Explosives,
    Operation.Battery,
    Operation.StorageTank,
    Operation.Pump,
    Operation.ChemicalPlant,
    Operation.LowDensityStructure,
    Operation.RocketFuel,
    Operation.RocketPart,
    Operation.Satellite,
    Operation.NuclearReactor,
    Operation.Centrifuge,
    Operation.UraniumProcessing,
    Operation.KovarexEnrichmentProcess,
    Operation.NuclearFuel,
    Operation.NuclearFuelReprocessing,
    Operation.UraniumFuelCell,
    Operation.HeatExchanger,
    Operation.HeatPipe,
    Operation.SteamTurbine,
}
