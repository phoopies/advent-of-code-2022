from Point import Point


class Sensor:
    def __init__(self, location: Point, beacon_location: Point) -> None:
        self.location = location
        self.beacon = beacon_location
