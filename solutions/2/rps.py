from typing import List, Tuple
from functools import reduce

filename = "./solutions/2/data.txt"


def get_data(filename: str) -> List[Tuple[str, str]]:
    data: List[Tuple[str, str]] = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            data.append((tuple(line.strip().split(" "))))
    return data


def rock_paper_scissors(p1: str, p2: str) -> Tuple[int, int]:
    """
    Returns the amount of points players get
    from this game of rock paper scissors
    """
    p1int = ord(p1) - ord("A") + 1
    p2int = ord(p2) - ord("X") + 1
    dif = p2int - p1int
    p = (3, 3)
    if dif == 1 or dif == -2:
        p = (0, 6)
    elif dif == 2 or dif == -1:
        p = (6, 0)
    return (p[0] + p1int, p[1] + p2int)


def end_rock_paper_scissors(p1: str, p2_ending: str) -> int:
    p1int = ord(p1) - ord("A") + 1
    if p2_ending == "Y":  # draw
        return 3 + p1int
    if p2_ending == "X":  # lose
        return 0 + (p1int - 1 or 3)
    if p2_ending == "Z":  # win
        return 6 + (p1int % 3) + 1


def part1(data):
    results = list(map(lambda p: rock_paper_scissors(*p), data))
    total_score = reduce(lambda prev, p: prev + p[1], results, 0)
    return total_score


def part2(data):
    p2_scores = list(map(lambda p: end_rock_paper_scissors(*p), data))
    print(p2_scores)
    total_score = reduce(lambda prev, p: prev + p, p2_scores)
    return total_score


data = get_data(filename)
print(part1(data))
print(part2(data))
