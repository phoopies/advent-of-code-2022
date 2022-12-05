class Instruction:
    def __init__(self, amount: int, initial: int, to: int) -> None:
        self.amount = amount
        self.initial = initial
        self.to = to

    @classmethod
    def from_str(cls, instruction: str) -> 'Instruction':
        splitted = instruction.split(' ')
        digits = list(filter(str.isdigit, splitted))
        digits = map(int, digits)
        return cls(*digits)