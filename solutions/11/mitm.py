from typing import Callable, List
from Monkey import Monkey
from functools import reduce
from math import floor
from copy import deepcopy

filename = "./solutions/11/data.txt"


def get_data(filename: str) -> List[Monkey]:
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    split_points = [i + 1 for i, s in enumerate(lines) if not s]
    monkeys = [
        Monkey.from_data(lines[i:j])
        for i, j in zip([0] + split_points, split_points + [len(lines)])
    ]
    return monkeys


def part1(
    monkeys: List[Monkey],
    rounds: int = 20,
    active_count: int = 2,
    worry: Callable[[int], int] = lambda x: floor(x / 3),
) -> int:
    copied_monkeys = deepcopy(monkeys)
    for _round in range(rounds):
        for monkey in copied_monkeys:
            monkey.play_round(copied_monkeys, worry)
    inspections = list(map(lambda m: m.inspections, copied_monkeys))
    active_ones = sorted(inspections)[-active_count:]
    return reduce(int.__mul__, active_ones, 1)

# Figure out other way to manage worry
# => lambda x: x yields same results for rounds 1 and 20
# Therefore we need to make sure that after managing the worry level the results are same as if not managing it
# => Take the modulo of a common factor of all test divisors
def part2(monkeys: List[Monkey]) -> int:
    common_factor = reduce(int.__mul__, [m.test_num for m in monkeys], 1)
    return part1(monkeys, rounds=10000, worry=lambda x: floor(x % common_factor))

monkeys = get_data(filename)

print(part1(monkeys))
print(part2(monkeys))
