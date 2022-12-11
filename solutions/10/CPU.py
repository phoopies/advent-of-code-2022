from Instruction import Instruction


class CPU:
    def __init__(self) -> None:
        self.register = 1
        self.current_cycle = 0

    @property
    def signal_strength(self):
        return self.current_cycle * self.register

    def perform(self, instruction: Instruction):
        register, cycle = self.register, self.current_cycle
        cycles = instruction.perform(self)
        return [(register, cycle + i + 1) for i in range(cycles)]
