from typing import List, Tuple

filename = "./solutions/4/data.txt"


def get_data(filename: str) -> List[Tuple[Tuple[int, int]]]:
    data: List[Tuple[str, str]] = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            l = line.strip()
            data.append(tuple([tuple(map(int, d.split("-"))) for d in l.split(",")]))
    return data


def contains(p1: Tuple[int, int], p2: Tuple[int, int]) -> bool:
    """p1 contains p2"""
    return (p1[0] <= p2[0]) and (p1[1] >= p2[1])


def overlaps(p1: Tuple[int, int], p2: Tuple[int, int]) -> bool:
    """p1 overlaps p2"""
    return (p2[0] <= p1[0] <= p2[1]) or (p2[0] <= p1[1] <= p2[1])


def part1(data: List[Tuple[Tuple[int, int]]]):
    l = list(
        filter(lambda tup: contains(tup[0], tup[1]) or contains(tup[1], tup[0]), data)
    )
    return len(l)


def part2(data: List[Tuple[Tuple[int, int]]]):
    l = list(
        filter(lambda tup: overlaps(tup[0], tup[1]) or overlaps(tup[1], tup[0]), data)
    )
    return len(l)


data = get_data(filename)

print(part1(data))
print(part2(data))
