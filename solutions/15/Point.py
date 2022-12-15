from typing import Union


class Point:
    def __init__(self, x: Union[int, str], y: Union[int, str]) -> None:
        self.x = int(x)
        self.y = int(y)
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, p: 'Point') -> 'Point':
        return Point(self.x + p.x, self.y + p.y)
    
    def __sub__(self, p: 'Point') -> 'Point':
        return Point(self.x - p.x, self.y - p.y)