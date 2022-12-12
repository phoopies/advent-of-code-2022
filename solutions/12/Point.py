from enum import Enum
from typing import List


class PointType(Enum):
    START = 1
    REGULAR = 2
    END = 3


class Point:
    def __init__(self, elevation: str, max_steps: int) -> None:
        self.type = PointType.REGULAR
        self.elevation = elevation
        if elevation == "S":
            self.elevation = "a"
            self.type = PointType.START
        if elevation == "E":
            self.elevation = "z"
            self.type = PointType.END

        self.max_steps = max_steps
        self.possible_paths: List["Point"] = []
        self.min_steps_from: "Point" = None

    @property
    def min_steps(self):
        if self.type == PointType.START:
            return 0
        return (
            self.min_steps_from.min_steps + 1 if self.min_steps_from else self.max_steps
        )
