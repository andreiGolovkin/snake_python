from pygame_tools.Geometry.Point import Point


class Cell(Point):
    def __init__(self, x: float = 0, y: float = 0):
        super().__init__(x, y)

    def get_key(self) -> str:
        return str(self.x) + "X" + str(self.y)

    def copy(self):
        return Cell(self.x, self.y)

    @classmethod
    def str2point(cls, key: str):
        _key = key.split("X")
        x = int(_key[0])
        y = int(_key[1])
        return cls(x, y)

    @classmethod
    def from_snake_segment(cls, segment: dict):
        vel_x = segment["x"]
        vel_y = segment["y"]

        return Point(vel_x, vel_y)
