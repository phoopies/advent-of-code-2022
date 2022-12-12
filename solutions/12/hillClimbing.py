from typing import List
from Point import Point, PointType

filename = "./solutions/12/data.txt"


def can_move(from_point: Point, to_point: Point):
    return ord(to_point.elevation) - ord(from_point.elevation) <= 1


def set_paths(points: List[List[Point]]):
    for y, row in enumerate(points):
        for x, point in enumerate(row):
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dir in dirs:
                next_y = y + dir[1]
                if next_y < 0 or next_y >= len(points):
                    continue
                next_x = x + dir[0]
                if next_x < 0 or next_x >= len(row):
                    continue
                p2 = points[next_y][next_x]
                if can_move(point, p2):
                    point.possible_paths.append(p2)


def get_data(filename: str) -> List[List[Point]]:
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        max_steps_req = len(lines) * len(lines[0])
        points = [[Point(c, max_steps_req) for c in l] for l in lines]
    set_paths(points)
    return points


def part1(points: List[List[Point]] = None) -> int:
    points = points or get_data(filename)
    flat_points = [p for row in points for p in row]
    points_to_check = flat_points.copy()
    while points_to_check:
        changed_points = []
        for point in points_to_check:
            for possible_path in point.possible_paths:
                if point.min_steps + 1 < possible_path.min_steps:
                    changed_points.append(possible_path)
                    possible_path.min_steps_from = point
        points_to_check = changed_points.copy()
    for point in flat_points:
        if point.type == PointType.END:
            return point.min_steps


def part2() -> int:
    points = get_data(filename)
    shortest = 10e100
    case_num = 1
    total_cases = len([p for row in points for p in row if p.elevation == "a"])
    for case_num in range(total_cases):
        points = get_data(filename)
        for row in points:
            for point in row:
                if point.type == PointType.START:
                    point.type == PointType.REGULAR
                    break
        occ = 0
        for row in points:
            for point in row:
                if point.elevation == "a":
                    occ += 1
                    if occ != case_num + 1:
                        continue
                    point.type = PointType.START
                    maybe_shortest = part1(points)
                    shortest = min(shortest, maybe_shortest)
                    print(f"Case {case_num+1}\{total_cases}: length: {maybe_shortest} ({shortest})")
                    break
    return shortest


print(part1())
print(part2())
