from typing import List
from Instruction import Instruction, AddInstruction
from CPU import CPU
from CRT import CRT

filename = "./solutions/10/data.txt"


def get_data(filename: str) -> List[Instruction]:
    instructions = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            parts = line.split(' ')
            if parts[0] == 'noop':
                instructions.append(Instruction(1))
            else:
                instructions.append(AddInstruction(int(parts[1])))
    return instructions


def part1(instructions, cycles: List[int] = [20, 60, 100, 140, 180, 220]) -> int:
    cpu = CPU()
    signal_strengths = []
    next_cycles = cycles.copy()
    next_cycles.reverse()
    next_cycle = next_cycles.pop()
    for instruction in instructions:
        states = cpu.perform(instruction)
        for state in states:
            register, cycle = state
            if cycle == next_cycle:
                signal_strengths.append(register * cycle)
                if not next_cycles:
                    break
                next_cycle = next_cycles.pop()
    return sum(signal_strengths)


def part2(instructions) -> int:
    crt = CRT()
    crt.draw(instructions)


instructions = get_data(filename)

print(part1(instructions))
part2(instructions)
