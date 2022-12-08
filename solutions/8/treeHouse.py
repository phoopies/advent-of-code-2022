from typing import List, Any
from functools import reduce

filename = "./solutions/8/data.txt"


def get_data(filename: str) -> List[List[int]]:
    with open(filename, "r") as f:
        lines = f.readlines()
        return [[int(c) for c in line] for line in map(str.strip, lines)]


def col(list_2d: List[List[Any]], i: int) -> List[Any]:
    return [x[i] for x in list_2d]


def visible(forest: List[List[int]], x: int, y: int) -> bool:
    if x == 0 or y == 0 or x == len(forest) - 1 or y == len(forest) - 1:
        return True
    tree = forest[y][x]
    treeCol = col(forest, x)
    competitors = [forest[y][:x], forest[y][x + 1 :], treeCol[:y], treeCol[y + 1 :]]
    return any([tree > max(competitor) for competitor in competitors])


def find(l, x) -> int:
    try:
        return l.index(x)
    except:
        return -1


# ugh :D
def scenic_score(forest: List[List[int]], x, y):
    if x == 0 or y == 0 or x == len(forest) - 1 or y == len(forest) - 1:
        return 0
    tree = forest[y][x]
    treeCol = col(forest, x)
    l, r, u, d = (
        forest[y][:x].copy(),
        forest[y][x + 1 :],
        treeCol[:y].copy(),
        treeCol[y + 1 :],
    )
    l.reverse(), u.reverse()
    comparisons = [[tree > other_tree for other_tree in d] for d in [l, r, u, d]]
    distances = [find(comparison, 0) + 1 for comparison in comparisons]
    points = [
        distance if distance != 0 else len([l, r, u, d][i])
        for i, distance in enumerate(distances)
    ]
    return reduce(lambda x, y: x * y, points, 1)


def part1(forest: List[List[int]]) -> int:
    return sum(
        [
            int(visible(forest, x, y))
            for y, row in enumerate(forest)
            for x, _ in enumerate(row)
        ]
    )


def part2(forest: List[List[int]]) -> int:
    return max(
        [
            scenic_score(forest, x, y)
            for y, row in enumerate(forest)
            for x, _ in enumerate(row)
        ]
    )


forest = get_data(filename)

print(part1(forest))
print(part2(forest))
