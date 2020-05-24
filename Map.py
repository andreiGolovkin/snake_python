from pygame_tools.Drawing_tools import color, rect
from Snake import *
from Cell import Cell
from Directions import UP, DOWN, LEFT, RIGHT, is_horizontal, is_vertical


food = Cell()

width = 30
height = 25

side = 20
gap = 1

snake = None


def draw(center: Point):
    global width
    global height

    start = find_start_offset(center)

    for x in range(width):
        for y in range(height):
            map_coord = Cell(x, y)
            draw_cell(start, map_coord)


def draw_cell(offset: Point, map_coord: Cell):
    global side
    global gap

    cell_coord, cell_width, cell_height = get_cell_param(map_coord)

    choose_color(map_coord)
    rect(offset.x + cell_coord.x, offset.y + cell_coord.y, cell_width, cell_height)


def choose_color(coord: Cell):
    global snake

    if is_food(coord):
        color(0, 200, 0)
    elif snake.is_head(coord):
        color(255, 0, 0)
    elif snake.is_body(coord):
        color(255, 255, 255)
    else:
        color(50, 50, 50)


def get_cell_param(coord: Point) -> tuple:
    global snake

    if not snake.is_body(coord):
        cell_coord, cell_width, cell_height = get_standard_cell_param(coord)
    else:
        cell_coord, cell_width, cell_height = get_expanded_cell_param(coord)

    return cell_coord, cell_width, cell_height


def get_standard_cell_param(coord: Point) -> tuple:
    global side
    global gap

    cell_coord = Point(coord.x * (side + gap), coord.y * (side + gap))

    cell_width = side
    cell_height = side

    return cell_coord, cell_width, cell_height


def get_expanded_cell_param(coord: Cell) -> tuple:
    global side
    global gap

    global snake

    cell_coord, cell_width, cell_height = get_standard_cell_param(coord)

    key = coord.get_key()
    segment = snake.body[key]
    vel = Cell.from_snake_segment(segment)

    direction = snake.get_dir(vel)
    if direction == RIGHT and not on_right_edge(coord):
        cell_coord, cell_width, cell_height = expand_to_right(cell_coord, cell_width, cell_height)
    elif direction == LEFT and not on_left_edge(coord):
        cell_coord, cell_width, cell_height = expand_to_left(cell_coord, cell_width, cell_height)
    elif direction == UP and not on_up_edge(coord):
        cell_coord, cell_width, cell_height = expand_to_up(cell_coord, cell_width, cell_height)
    elif direction == DOWN and not on_down_edge(coord):
        cell_coord, cell_width, cell_height = expand_to_down(cell_coord, cell_width, cell_height)

    return cell_coord, cell_width, cell_height


def expand_to_right(cell_coord: Point, cell_width: int, cell_height: int) -> tuple:
    global gap
    return cell_coord, cell_width + gap, cell_height


def expand_to_left(cell_coord: Point, cell_width: int, cell_height: int) -> tuple:
    global gap
    return cell_coord.with_offset(-gap, 0), cell_width + gap, cell_height


def expand_to_up(cell_coord: Point, cell_width: int, cell_height: int) -> tuple:
    global gap
    return cell_coord.with_offset(0, -gap), cell_width, cell_height + gap


def expand_to_down(cell_coord: Point, cell_width: int, cell_height: int) -> tuple:
    global gap
    return cell_coord, cell_width, cell_height + gap


def on_right_edge(coord: Cell) -> bool:
    global width

    return coord.x == width - 1


def on_left_edge(coord: Cell) -> bool:
    return coord.x == 0


def on_up_edge(coord: Cell) -> bool:
    return coord.y == 0


def on_down_edge(coord: Cell) -> bool:
    global height

    return coord.y == height - 1


def find_start_offset(center: Point) -> Point:
    global width
    global height
    global side

    start = Point(center.x - width*(side+1)/2, center.y - height*(side+1)/2)

    return start


def food_eaten() -> bool:
    global snake

    global food

    return snake.is_head(food)


def is_food(coord: Cell) -> bool:
    global food
    return food == coord


def place_food():
    global food

    global width
    global height

    global snake

    new_food = Cell.random(width, height)
    while snake.is_head(new_food) or snake.is_body(new_food):
        new_food = Cell.random(width, height)
    food = new_food


def set_snake(_snake: Snake):
    global snake
    snake = _snake


def get_width() -> int:
    global width
    return width


def get_height() -> int:
    global height
    return height
