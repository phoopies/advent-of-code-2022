from typing import List, Tuple
from Instruction import Instruction

filename = "./solutions/5/data.txt"


def get_data(filename: str) -> Tuple[List[List[str]], List[Instruction]]:
    crates: List[List[str]] = []
    instructions: List[Instruction] = []

    with open(filename, "r") as f:
        lines = [line.replace("\n", "") for line in f.readlines()]
        split = lines.index("")
        crate_count = int(lines[split - 1][-2])
        crates = [[] for _ in range(crate_count)]

        # Handle crates
        for line in lines[: split - 1]:
            crate_row = line[
                1::4
            ]  # Get every fourth element starting from the second element
            for i, crate in enumerate(crate_row):
                if crate != " ":
                    crates[i].insert(0, crate)

        # Handle instructions
        for line in lines[split + 1 :]:
            instructions.append(Instruction.from_str(line))
    return (crates, instructions)


def part1(crates: List[List[str]], instructions: List[Instruction]) -> str:
    movable_crates = [crate.copy() for crate in crates]
    for instruction in instructions:
        for _ in range(instruction.amount):
            movable_crates[instruction.to - 1].append(
                movable_crates[instruction.initial - 1].pop()
            )
    return "".join([stack[-1] for stack in movable_crates])


def part2(crates: List[List[str]], instructions: List[Instruction]):
    movable_crates = [crate.copy() for crate in crates]
    for instruction in instructions:
        movable_crates[instruction.to - 1] = movable_crates[instruction.to - 1] + (
            movable_crates[instruction.initial - 1][-instruction.amount:]
        )
        movable_crates[instruction.initial - 1] = movable_crates[
            instruction.initial - 1
        ][:-instruction.amount]
    return "".join([stack[-1] for stack in movable_crates])


crates, instructions = get_data(filename)

print(part1(crates, instructions))
print(part2(crates, instructions))
