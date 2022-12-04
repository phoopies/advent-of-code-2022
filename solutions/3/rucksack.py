from typing import List, Tuple
from functools import reduce

filename = "./solutions/3/data.txt"


def get_data(filename: str) -> List[Tuple[str, str]]:
    data: List[Tuple[str, str]] = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            l = line.strip()
            n = int(len(l) / 2)
            data.append((l[:n], l[n:]))
    return data


def priority(item: str) -> int:
    shift = ord("A") - 27 if item.isupper() else ord("a") - 1
    return ord(item) - shift


def priorities(items: list[str]) -> int:
    return reduce(lambda x, y: x + y, map(priority, items))

def part1(data: List[Tuple[str, str]]):
    duplicates = [[c for c in x if c in y] for (x, y) in data]
    duplicates = [c[0] for c in duplicates]
    return priorities(duplicates)


def part2(data: List[Tuple[str, str]], group_size = 3):
    if (len(data) % group_size != 0):
        raise ValueError("Cannot divide data into groups")

    group_badges: List[List[str]] = []
    for i, items in enumerate([x + y for (x, y) in data]):
        if i % group_size == 0:
            group_badges.append(items)
        else:
            group_badges[-1] = [item for item in items if item in group_badges[-1]]
    
    return priorities([badge[0] for badge in group_badges])




data = get_data(filename)

print(part1(data))
print(part2(data))
