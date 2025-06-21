from core.enums.assembling_machine import AssemblingMachine

mining_drill_allowed: set[AssemblingMachine] = {
    AssemblingMachine.ElectricMiningDrill,
    AssemblingMachine.BurnerMiningDrill,
    AssemblingMachine.Pumpjack,
}
