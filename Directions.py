LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4


def dir_is_valid(direction) -> bool:
    return 5 > direction > 0


def is_horizontal(direction) -> bool:
    return direction == LEFT or direction == RIGHT


def is_vertical(direction) -> bool:
    return direction == UP or direction == DOWN


def dir2str(direction):
    ans = ""
    if direction == RIGHT:
        ans = "RIGHT"
    elif direction == LEFT:
        ans = "LEFT"
    elif direction == DOWN:
        ans = "DOWN"
    elif direction == UP:
        ans = "UP"
    return ans
