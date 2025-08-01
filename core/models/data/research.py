from sympy import Integer

from core.enums.operation import Operation

TIME: dict[Operation, Integer] = {
    Operation.ResearchElectricMiningDrill: Integer(10),
    Operation.ResearchRepairPack: Integer(10),
    Operation.ResearchRadar: Integer(10),
    Operation.ResearchPhysicalProjectileDamage1: Integer(30),
    Operation.ResearchPhysicalProjectileDamage2: Integer(30),
    Operation.ResearchWeaponShootingSpeed1: Integer(30),
    Operation.ResearchWeaponShootingSpeed2: Integer(30),
    Operation.ResearchStrongerExplosives1: Integer(30),
    Operation.ResearchPhysicalProjectileDamage3: Integer(60),
    Operation.ResearchPhysicalProjectileDamage4: Integer(60),
    Operation.ResearchPhysicalProjectileDamage5: Integer(60),
    Operation.ResearchPhysicalProjectileDamage6: Integer(60),
    Operation.ResearchPhysicalProjectileDamage7: Integer(60),
    Operation.ResearchStrongerExplosives2: Integer(30),
    Operation.ResearchStrongerExplosives3: Integer(60),
    Operation.ResearchStrongerExplosives4: Integer(60),
    Operation.ResearchStrongerExplosives5: Integer(60),
    Operation.ResearchStrongerExplosives6: Integer(60),
    Operation.ResearchStrongerExplosives7: Integer(60),
    Operation.ResearchRefinedFlammables1: Integer(30),
    Operation.ResearchRefinedFlammables2: Integer(30),
    Operation.ResearchRefinedFlammables3: Integer(60),
    Operation.ResearchRefinedFlammables4: Integer(60),
    Operation.ResearchRefinedFlammables5: Integer(60),
    Operation.ResearchRefinedFlammables6: Integer(60),
    Operation.ResearchRefinedFlammables7: Integer(60),
    Operation.ResearchLaserWeaponsDamage1: Integer(30),
    Operation.ResearchLaserWeaponsDamage2: Integer(30),
    Operation.ResearchLaserWeaponsDamage3: Integer(60),
    Operation.ResearchLaserWeaponsDamage4: Integer(60),
    Operation.ResearchLaserWeaponsDamage5: Integer(60),
    Operation.ResearchLaserWeaponsDamage6: Integer(60),
    Operation.ResearchLaserWeaponsDamage7: Integer(60),
    Operation.ResearchWeaponShootingSpeed3: Integer(60),
    Operation.ResearchWeaponShootingSpeed4: Integer(60),
    Operation.ResearchWeaponShootingSpeed5: Integer(60),
    Operation.ResearchWeaponShootingSpeed6: Integer(60),
    Operation.ResearchLaserShootingSpeed1: Integer(30),
    Operation.ResearchLaserShootingSpeed2: Integer(30),
    Operation.ResearchLaserShootingSpeed3: Integer(60),
    Operation.ResearchLaserShootingSpeed4: Integer(60),
    Operation.ResearchLaserShootingSpeed5: Integer(60),
    Operation.ResearchLaserShootingSpeed6: Integer(60),
    Operation.ResearchLaserShootingSpeed7: Integer(60),
    Operation.ResearchArtilleryShellRange1: Integer(60),
    Operation.ResearchArtilleryShellSpeed1: Integer(60),
    Operation.ResearchFollowerRobotCount5: Integer(30),
    Operation.ResearchBulkInserter: Integer(30),
    Operation.ResearchInserterCapacityBonus1: Integer(30),
    Operation.ResearchInserterCapacityBonus2: Integer(30),
    Operation.ResearchInserterCapacityBonus3: Integer(30),
    Operation.ResearchInserterCapacityBonus4: Integer(30),
    Operation.ResearchInserterCapacityBonus5: Integer(30),
    Operation.ResearchInserterCapacityBonus6: Integer(30),
    Operation.ResearchInserterCapacityBonus7: Integer(30),
    Operation.ResearchAutomation: Integer(10),
    Operation.ResearchAutomation2: Integer(15),
    Operation.ResearchLogisticSciencePack: Integer(5),
    Operation.ResearchSteelProcessing: Integer(5),
    Operation.ResearchMilitary: Integer(15),
    Operation.ResearchMilitary2: Integer(15),
    Operation.ResearchFastInserter: Integer(15),
    Operation.ResearchLogistics: Integer(15),
    Operation.ResearchRailway: Integer(30),
    Operation.ResearchAutomatedRailTransportation: Integer(30),
    Operation.ResearchAutomobilism: Integer(30),
    Operation.ResearchLamp: Integer(15),
    Operation.ResearchSolarEnergy: Integer(30),
    Operation.ResearchHeavyArmor: Integer(30),
    Operation.ResearchGunTurret: Integer(10),
    Operation.ResearchResearchSpeed1: Integer(30),
    Operation.ResearchResearchSpeed2: Integer(30),
    Operation.ResearchElectricEnergyDistribution1: Integer(30),
    Operation.ResearchAdvancedMaterialProcessing: Integer(30),
    Operation.ResearchConcrete: Integer(30),
    Operation.ResearchEngine: Integer(15),
    Operation.ResearchLandfill: Integer(30),
    Operation.ResearchLogistics2: Integer(30),
    Operation.ResearchToolbelt: Integer(30),
    Operation.ResearchStoneWall: Integer(10),
    Operation.ResearchGate: Integer(30),
    Operation.ResearchChemicalSciencePack: Integer(10),
    Operation.ResearchMilitarySciencePack: Integer(15),
    Operation.ResearchProductionSciencePack: Integer(30),
    Operation.ResearchUtilitySciencePack: Integer(30),
    Operation.ResearchMilitary3: Integer(30),
    Operation.ResearchMilitary4: Integer(45),
    Operation.ResearchUraniumAmmo: Integer(45),
    Operation.ResearchAtomicBomb: Integer(45),
    Operation.ResearchAutomation3: Integer(60),
    Operation.ResearchExplosives: Integer(15),
    Operation.ResearchCliffExplosives: Integer(15),
    Operation.ResearchFlammables: Integer(30),
    Operation.ResearchLandMine: Integer(30),
    Operation.ResearchFlamethrower: Integer(30),
    Operation.ResearchAdvancedCircuit: Integer(15),
    Operation.ResearchProcessingUnit: Integer(30),
    Operation.ResearchFluidWagon: Integer(30),
    Operation.ResearchBrakingForce1: Integer(30),
    Operation.ResearchBrakingForce2: Integer(30),
    Operation.ResearchBrakingForce3: Integer(30),
    Operation.ResearchBrakingForce4: Integer(30),
    Operation.ResearchBrakingForce5: Integer(35),
    Operation.ResearchBrakingForce6: Integer(45),
    Operation.ResearchBrakingForce7: Integer(60),
    Operation.ResearchTank: Integer(30),
    Operation.ResearchLogistics3: Integer(15),
    Operation.ResearchLaser: Integer(30),
    Operation.ResearchRocketry: Integer(15),
    Operation.ResearchExplosiveRocketry: Integer(30),
    Operation.ResearchModularArmor: Integer(30),
    Operation.ResearchPowerArmor: Integer(30),
    Operation.ResearchPowerArmorMk2: Integer(30),
    Operation.ResearchLaserTurret: Integer(30),
    Operation.ResearchRobotics: Integer(30),
    Operation.ResearchRocketFuel: Integer(45),
    Operation.ResearchLowDensityStructure: Integer(45),
    Operation.ResearchRocketSilo: Integer(60),
    Operation.ResearchResearchSpeed3: Integer(30),
    Operation.ResearchResearchSpeed4: Integer(30),
    Operation.ResearchResearchSpeed5: Integer(30),
    Operation.ResearchResearchSpeed6: Integer(30),
    Operation.ResearchElectricEnergyDistribution2: Integer(45),
    Operation.ResearchElectricEnergyAccumulators: Integer(30),
    Operation.ResearchAdvancedMaterialProcessing2: Integer(30),
    Operation.ResearchEffectTransmission: Integer(30),
    Operation.ResearchLubricant: Integer(30),
    Operation.ResearchElectricEngine: Integer(30),
    Operation.ResearchBattery: Integer(30),
    Operation.ResearchConstructionRobotics: Integer(30),
    Operation.ResearchLogisticRobotics: Integer(30),
    Operation.ResearchLogisticSystem: Integer(30),
    Operation.ResearchWorkerRobotsSpeed1: Integer(30),
    Operation.ResearchWorkerRobotsSpeed2: Integer(30),
    Operation.ResearchWorkerRobotsSpeed3: Integer(60),
    Operation.ResearchWorkerRobotsSpeed4: Integer(60),
    Operation.ResearchWorkerRobotsSpeed5: Integer(60),
    Operation.ResearchWorkerRobotsSpeed6: Integer(60),
    Operation.ResearchWorkerRobotsStorage1: Integer(30),
    Operation.ResearchWorkerRobotsStorage2: Integer(60),
    Operation.ResearchWorkerRobotsStorage3: Integer(60),
    Operation.ResearchEnergyShieldEquipment: Integer(15),
    Operation.ResearchNightVisionEquipment: Integer(15),
    Operation.ResearchBeltImmunityEquipment: Integer(15),
    Operation.ResearchEnergyShieldMk2Equipment: Integer(30),
    Operation.ResearchBatteryEquipment: Integer(15),
    Operation.ResearchBatteryMk2Equipment: Integer(30),
    Operation.ResearchSolarPanelEquipment: Integer(15),
    Operation.ResearchPersonalLaserDefenseEquipment: Integer(30),
    Operation.ResearchDischargeDefenseEquipment: Integer(30),
    Operation.ResearchFissionReactorEquipment: Integer(30),
    Operation.ResearchExoskeletonEquipment: Integer(30),
    Operation.ResearchPersonalRoboportEquipment: Integer(30),
    Operation.ResearchPersonalRoboportMk2Equipment: Integer(30),
    Operation.ResearchFluidHandling: Integer(15),
    Operation.ResearchOilGathering: Integer(30),
    Operation.ResearchAdvancedOilProcessing: Integer(30),
    Operation.ResearchCoalLiquefaction: Integer(30),
    Operation.ResearchSulfurProcessing: Integer(30),
    Operation.ResearchPlastics: Integer(30),
    Operation.ResearchModules: Integer(30),
    Operation.ResearchSpeedModule: Integer(30),
    Operation.ResearchSpeedModule2: Integer(30),
    Operation.ResearchSpeedModule3: Integer(60),
    Operation.ResearchProductivityModule: Integer(30),
    Operation.ResearchProductivityModule2: Integer(30),
    Operation.ResearchProductivityModule3: Integer(60),
    Operation.ResearchEfficiencyModule: Integer(30),
    Operation.ResearchEfficiencyModule2: Integer(30),
    Operation.ResearchEfficiencyModule3: Integer(60),
    Operation.ResearchDefender: Integer(30),
    Operation.ResearchDistractor: Integer(30),
    Operation.ResearchDestroyer: Integer(30),
    Operation.ResearchUraniumMining: Integer(30),
    Operation.ResearchNuclearPower: Integer(30),
    Operation.ResearchKovarexEnrichmentProcess: Integer(30),
    Operation.ResearchNuclearFuelReprocessing: Integer(30),
    Operation.ResearchMiningProductivity1: Integer(60),
    Operation.ResearchMiningProductivity2: Integer(60),
    Operation.ResearchMiningProductivity3: Integer(60),
    Operation.ResearchMiningProductivity4: Integer(60),
    Operation.ResearchArtillery: Integer(30),
    Operation.ResearchSpidertron: Integer(30),
    Operation.ResearchCircuitNetwork: Integer(15),
    Operation.ResearchAdvancedCombinators: Integer(30),
}
