from typing import List, Union
from Tile import Tile
from Point import Point
from TileMap import TileMap
from copy import deepcopy

filename = "./solutions/14/data.txt"


def get_data(filename: str) -> List[List[Tile]]:
    points: List[List[Point]] = []
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        points = [
            [Point(*pair.split(",")) for pair in row.split("->")] for row in lines
        ]
    return TileMap.from_data(points)


def next_point(tile_map: TileMap, sand_point: Point) -> Union[Point, None]:
    moves_to_check = [Point(0, 1), Point(-1, 1), Point(1, 1)]
    for move in moves_to_check:
        move_to_point = sand_point + move
        if not tile_map.is_inside(move_to_point):
            if not tile_map.has_floor:
                return Point(-1, -1)  # Abyss
            tile_map.make_wider()
            return next_point(tile_map, tile_map.source_point)
        next_tile = tile_map[move_to_point.y][move_to_point.x]
        if next_tile == Tile.AIR or next_tile == Tile.SAND_SOURCE:
            return move_to_point
    return None


def part1(tile_map: TileMap) -> int:
    tile_map_c = deepcopy(tile_map)
    sand_units = 0
    while True:
        sand_point = Point(tile_map_c.source_point.x, tile_map_c.source_point.y)
        prev = None
        while sand_point:
            if sand_point.y == -1:
                return sand_units
            prev = sand_point
            sand_point = next_point(tile_map_c, sand_point)
        sand_units += 1
        tile_map_c[prev.y][prev.x] = Tile.SAND


def part2(tile_map: TileMap) -> int:
    tile_map_c = deepcopy(tile_map)
    tile_map_c.add_floor()
    sand_units = 0
    while True:
        sand_units += 1
        start = Point(tile_map_c.source_point.x, tile_map_c.source_point.y)
        sand_point = next_point(tile_map_c, start)
        if not sand_point:
            return sand_units
        prev = None
        while sand_point:
            prev = sand_point
            sand_point = next_point(tile_map_c, sand_point)
        tile_map_c[prev.y][prev.x] = Tile.SAND


tile_map = get_data(filename)

print(part1(tile_map))
print(part2(tile_map))
