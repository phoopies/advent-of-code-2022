from typing import List, Union
from Tile import Tile
from Point import Point


class TileMap:
    def __init__(
        self, tile_map: List[List[Tile]], source_point: Union[Point, None] = None
    ) -> None:
        self.tile_map = tile_map
        self.source_point = source_point if source_point else self._get_source_point()
        self.w = len(tile_map[0])
        self.h = len(self.tile_map)
        self.has_floor = False

    def __str__(self) -> str:
        return "\n".join(
            ["".join([tile.value for tile in row]) for row in self.tile_map]
        )

    def __getitem__(self, y: int) -> List[Tile]:
        return self.tile_map[y]

    def _get_source_point(self) -> Point:
        for y, row in enumerate(self.tile_map):
            for x, tile in enumerate(row):
                if tile == Tile.SAND_SOURCE:
                    return Point(x, y)
        return Point(-1, -1)

    def is_inside(self, point: Point) -> bool:
        return 0 <= point.x < self.w and 0 <= point.y < self.h

    def add_floor(self):
        self.tile_map.extend([[Tile.AIR] * self.w, [Tile.ROCK] * self.w])
        self.has_floor = True
        self.h += 2

    def make_wider(
        self, how_much = 1
    ):
        if how_much < 1:
            return
        for row in self.tile_map:
            row.insert(0, Tile.AIR)
            row.append(Tile.AIR)
        if self.has_floor:
            self.tile_map[-1][0] = Tile.ROCK
            self.tile_map[-1][-1] = Tile.ROCK
        self.w += 2
        self.source_point.x += 1
        if how_much > 0:
            self.make_wider(how_much-1)

    @staticmethod
    def from_data(
        rock_lines: List[List[Point]], source: Point = Point(500, 0)
    ) -> "TileMap":
        rock_points_x_w_source = [p.x for row in rock_lines for p in row] + [source.x]
        rock_points_y_w_source = [p.y for row in rock_lines for p in row] + [source.y]

        min_x, max_x = min(rock_points_x_w_source), max(rock_points_x_w_source)
        min_y, max_y = min(rock_points_y_w_source), max(rock_points_y_w_source)
        the_map = [
            [Tile.AIR for _x in range(max_x - min_x + 1)]
            for _y in range(max_y - min_y + 1)
        ]
        shifter = Point(min_x, min_y)
        actual_source_point = source - shifter
        shifted_rock_lines = [[p - shifter for p in rock] for rock in rock_lines]
        the_map[actual_source_point.y][actual_source_point.x] = Tile.SAND_SOURCE
        for rock in shifted_rock_lines:
            prev = rock[0]
            for p in rock[1:]:
                if prev.x == p.x:
                    r = sorted([prev.y, p.y])
                    for y in range(r[0], r[1] + 1):
                        the_map[y][p.x] = Tile.ROCK
                elif prev.y == p.y:
                    r = sorted([prev.x, p.x])
                    for x in range(r[0], r[1] + 1):
                        the_map[p.y][x] = Tile.ROCK
                prev = p
        return TileMap(the_map, actual_source_point)
