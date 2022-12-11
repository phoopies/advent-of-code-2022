class Instruction:
    def __init__(self, cycles: int) -> None:
        self.cycles = cycles

    def perform(self, cpu):
        cpu.current_cycle += self.cycles
        return self.cycles


class AddInstruction(Instruction):
    def __init__(self, count: int) -> None:
        self.count = count
        super().__init__(2)

    def perform(self, cpu):
        cpu.register += self.count
        return super().perform(cpu)
