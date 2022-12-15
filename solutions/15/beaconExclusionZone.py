from Range import Range
from typing import List, Set
from Sensor import Sensor
from Point import Point


use_test_data = False
filename = "./solutions/15/" + ("test-data.txt" if use_test_data else "data.txt")

TUNING_MULTIPLIER = 4000000

def get_data(filename: str) -> List[Sensor]:
    n = lambda s: int(s.split('=')[1].replace(':', '').replace(",", ""))
    with open(filename, "r") as f:
        lines = [line.strip().split(' ') for line in f.readlines()]
        return [Sensor(Point(n(line[2]), n(line[3])), Point(n(line[8]), n(line[9]))) for line in lines]

def longer_distance(p1: Point, p2: Point) -> int:
    dist = p1 - p2
    delta = max(abs(dist.x), abs(dist.y))
    return delta

def overlaps(sensor: Sensor, y: int) -> bool:
    longer = longer_distance(sensor.location, sensor.beacon)
    return sensor.location.y - longer < y < sensor.location.y + longer

def length_to_beacon(sensor: Sensor) -> int:
    return abs(sensor.location.x - sensor.beacon.x) + abs(sensor.location.y - sensor.beacon.y)

def part1(sensors: List[Sensor], y = 10) -> int:
    overlapping_sensors = [sensor for sensor in sensors if overlaps(sensor, y)]
    cannot_have_beacon_xs: Set[int] = set()
    for sensor in overlapping_sensors:
        dist_to_y = abs(sensor.location.y - y)
        l_beacon = length_to_beacon(sensor)
        move = l_beacon - dist_to_y
        too_close_xs =  [x for x in range(sensor.location.x - move, sensor.location.x + move)]
        cannot_have_beacon_xs = cannot_have_beacon_xs.union(set(too_close_xs))
    return len(cannot_have_beacon_xs)


def part2(sensors: List[Sensor], max_coordinate = 2000000) -> int:
    gaps: List[List[Range]] = [[Range(0, max_coordinate)] for _ in range(max_coordinate + 1)]
    for i, sensor in enumerate(sensors):
        print(f"Checking sensor {i+1} / {len(sensors)}")
        l_beacon = length_to_beacon(sensor)
        for x in range(l_beacon + 1):
            y = sensor.location.y
            min_x = sensor.location.x - l_beacon + x
            max_x = sensor.location.x + l_beacon - x
            all_gaps: List[List[Range]]  = []
            if x == 0:
                all_gaps.append(gaps[y])
            else:
                if y - x >= 0:
                    all_gaps.append(gaps[y - x])
                if y + x <= max_coordinate:
                    all_gaps.append(gaps[y + x])
            for agap in all_gaps:
                for j in range(len(agap)):
                    gap = agap[j]
                    if not gap:
                        continue
                    if min_x <= gap.start and max_x >= gap.end:
                        agap[j] = None
                    elif min_x <= gap.start:
                        if max_x >= gap.start:
                            agap[j].start = max_x + 1
                    elif max_x >= gap.end:
                        if min_x <= gap.end:
                            agap[j].end = min_x - 1
                    else: # in between
                        agap.insert(j, (Range(gap.start, min_x - 1)))
                        agap[j+1].start = max_x+1
    result = 0
    for y, gap in enumerate(gaps):
        for r in gap:
            if r:
                if result:
                    print("OOPs found multiple solutions!")
                result = r.start * TUNING_MULTIPLIER + y
    return result


sensors = get_data(filename)

print(part1(sensors, 10 if use_test_data else 2000000))
print(part2(sensors, 20 if use_test_data else 4000000))
