from Directions import *
from Cell import Cell
from pygame_tools.Controls import *
from pygame_tools.Geometry.Point import Point
import Map


class Snake:
    def __init__(self, x, y):
        self.head = Cell(int(x), int(y))

        self.vel = Point(1, 0)

        self.last_tail = self.head.with_offset(-2, 0).get_key()
        self.body = {self.head.with_offset(-1, 0).get_key(): {"x": 1, "y": 0},
                     self.last_tail: {"x": 1, "y": 0}}

    def move(self):
        self.move_head()
        if not Map.food_eaten():
            self.move_tail()

    def move_head(self):
        self.add_body_piece()
        self.move_head_along_axis()
        self.head = self.check_borders(self.head)

    def move_tail(self):
        new_tail = self.get_new_tail()
        new_tail = self.check_borders(new_tail)
        self.set_tail(new_tail)

    def change_dir(self, direction) -> bool:
        valid_change = self.dir_change_is_valid(direction)
        if valid_change:
            self.set_dir(direction)
        return valid_change

    def dir_change_is_valid(self, direction: int) -> bool:
        current_dir = self.current_dir()
        return is_vertical(current_dir) == is_horizontal(direction)

    def add_body_piece(self):
        key = self.head.get_key()
        self.body[key] = {"x": self.vel.x, "y": self.vel.y}

    def move_head_along_axis(self):
        self.head.add_point(self.vel)

    def is_head(self, coord: Cell) -> bool:
        return coord == self.head

    def is_body(self, coord: Cell) -> bool:
        return coord.get_key() in self.body.keys()

    def bite_itself(self) -> bool:
        return self.is_body(self.head)

    def set_tail(self, new_tail: Cell):
        del self.body[self.last_tail]
        self.last_tail = new_tail.get_key()

    def set_dir(self, direction):
        if direction == RIGHT:
            self.set_dir_to_right()
        elif direction == LEFT:
            self.set_dir_to_left()
        elif direction == DOWN:
            self.set_dir_to_down()
        elif direction == UP:
            self.set_dir_to_up()

    def get_new_tail(self) -> Cell:
        new_tail = Cell.str2point(self.last_tail)

        new_tail.add(self.body[self.last_tail]['x'], self.body[self.last_tail]['y'])

        return new_tail

    def set_dir_to_down(self):
        self.vel.x = 0
        self.vel.y = 1

    def set_dir_to_up(self):
        self.vel.x = 0
        self.vel.y = -1

    def set_dir_to_right(self):
        self.vel.x = 1
        self.vel.y = 0

    def set_dir_to_left(self):
        self.vel.x = -1
        self.vel.y = 0

    def current_dir(self) -> int:
        return self.get_dir(self.vel)

    @classmethod
    def get_dir(cls, vel: Point) -> int:
        ans = 0
        if vel.x > 0:
            ans = RIGHT
        elif vel.x < 0:
            ans = LEFT
        elif vel.y > 0:
            ans = DOWN
        elif vel.y < 0:
            ans = UP
        return ans

    @classmethod
    def key2dir(cls, key: Key) -> int:
        ans = 0

        if key == D or key == RIGHT_ARROW:
            ans = RIGHT
        elif key == A or key == LEFT_ARROW:
            ans = LEFT
        elif key == W or key == UP_ARROW:
            ans = UP
        elif key == S or key == DOWN_ARROW:
            ans = DOWN

        return ans

    @classmethod
    def get_key(cls, coord: Cell) -> str:
        return str(coord.x) + "X" + str(coord.y)

    @classmethod
    def get_coord(cls, key) -> tuple:
        _key = key.split("X")
        x = int(_key[0])
        y = int(_key[1])
        return x, y

    @classmethod
    def check_borders(cls, point: Cell) -> Cell:
        new_point = point.copy()
        if point.x > Map.get_width() - 1:
            new_point.x = 0
        elif point.x < 0:
            new_point.x = Map.get_width() - 1

        if point.y > Map.get_height() - 1:
            new_point.y = 0
        elif point.y < 0:
            new_point.y = Map.get_height() - 1

        return new_point
