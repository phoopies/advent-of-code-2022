from typing import List, Any, Tuple

filename = "./solutions/9/data.txt"

Movement = Tuple[str, int]

def get_data(filename: str) -> List[Movement]:
    with open(filename, "r") as f:
        lines = f.readlines()
        return [(m[0], int(m[1])) for m in map(lambda x: x.strip().split(' '), lines)]


def col(list_2d: List[List[Any]], i: int) -> List[Any]:
    return [x[i] for x in list_2d]

def go(initial: Tuple[int, int], amount: Tuple[int, int]) -> Tuple[int, int]:
    return (initial[0] + amount[0], initial[1] + amount[1])

def move_step(initial: Tuple[int, int], step: int) -> Tuple[int, int]:
    move_map = {
        'L': (-1, 0),
        'U': (0, 1),
        'R': (1, 0),
        'D': (0, -1),
    }
    s = move_map[step]
    return go(initial, s)

def follow(initial, who):
    deltaX = who[0] - initial[0]
    deltaY = who[1] - initial[1]
    diag = abs(deltaX) + abs(deltaY) > 2
    mapper = lambda delta: int(diag) * min(max(delta, -1), 1) if -1 <= delta <= 1 else min(max(delta, -1), 1)
    return go(initial, (mapper(deltaX), mapper(deltaY)))
    

def part1(moves: List[Movement]) -> int:
    tail = (0, 0)
    head = (0, 0)
    tail_positions = [tail]
    for move in moves:
        for _ in range(move[1]):
            head = move_step(head, move[0])
            tail = follow(tail, head)
            if tail not in tail_positions:
                tail_positions.append(tail)
    return len(tail_positions)


def part2(moves: List[Movement], knot_count: int = 10) -> int:
    knots = [(0, 0) for _ in range(knot_count)]
    tail_positions = set([knots[-1]])
    for move in moves:
        for _ in range(move[1]):
            knots[0] = move_step(knots[0], move[0])
            for i in range(1, len(knots)):
                knots[i] = follow(knots[i], knots[i-1])
            tail_positions.add(knots[-1])
    return len(tail_positions)


moves = get_data(filename)

print(part1(moves))
print(part2(moves))
