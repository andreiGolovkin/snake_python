import pygame
import sys
import Map
from Snake import Snake
from timer import Timer
from pygame_tools.Drawing_tools import set_win_size, background, screen_width, screen_height, update_display
from pygame_tools.Controls import Key, SPACE
from pygame_tools.Geometry.Point import Point
from Directions import dir_is_valid


class Game:
    def __init__(self):
        self.game_over = False
        self.dir_is_changed = False

        self.t = Timer(0.5)

        self.snake = Snake(Map.get_width() / 2, Map.get_height() / 2)

        pygame.init()
        set_win_size(800, 600)
        Map.set_snake(self.snake)
        Map.place_food()

    def iterate(self):
        self.check_events()
        self.setup_timer()
        if not self.game_over and (self.t.is_finished() or self.dir_is_changed):
            self.update()
            self.draw()

        if self.dir_is_changed:
            self.t.restart()
            self.dir_is_changed = False

    def update(self):
        self.snake.move()
        if Map.food_eaten():
            Map.place_food()
        self.check_game_state()

    def setup_timer(self):
        if SPACE.pressed:
            self.t.interval = 0.05
        else:
            self.t.interval = 0.5

    def check_game_state(self):
        self.game_over = self.snake.bite_itself()

    def draw(self):
        if not self.game_over:
            background(0, 0, 0)

            center_point = Point(screen_width() / 2, screen_height() / 2)
            Map.draw(center_point)

            update_display()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.handle_on_press_control(event.key)
            elif event.type == pygame.KEYUP:
                self.handle_on_release_control(event.key)
            elif event.type == pygame.QUIT:
                sys.exit()

    def handle_on_press_control(self, code: int):
        key = Key(code)
        direction = self.snake.key2dir(key)
        if dir_is_valid(direction):
            self.dir_is_changed = self.snake.change_dir(direction)
        elif key == SPACE:
            SPACE.press()

    @classmethod
    def handle_on_release_control(cls, code: int):
        key = Key(code)
        if key == SPACE:
            SPACE.release()


def run():
    game = Game()
    while True:
        game.iterate()


'''
game_over = False
dir_is_changed = False

t = Timer(0.5)

snake = None


def run():
    init()
    while True:
        iterate()


def init():
    pygame.init()
    set_win_size(800, 600)
    create_snake()
    Map.place_food()


def iterate():
    global game_over
    global dir_is_changed
    global t

    check_events()

    if not game_over and (t.is_finished() or dir_is_changed):
        update()
        draw()

    if dir_is_changed:
        t.restart()
        dir_is_changed = False


def update():
    global snake

    snake.move_head(Map.get_width(), Map.get_height())
    if not Map.food_eaten():
        snake.move_tail(Map.get_width(), Map.get_height())
    else:
        Map.place_food()
    check_game_state()


def check_game_state():
    global game_over
    global snake

    game_over = snake.bite_itself()


def draw():
    global game_over

    if not game_over:
        background(0, 0, 0)

        Map.draw(screen_width() / 2, screen_height() / 2)

        update_display()


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            handle_control(event.key)
        elif event.type == pygame.QUIT:
            sys.exit()


def handle_control(key):
    global snake
    global dir_is_changed

    direction = snake.key2dir(key)
    if dir_is_valid(direction):
        dir_is_changed = snake.change_dir(direction)


def create_snake():
    global snake

    snake = Snake(Map.get_width() / 2, Map.get_height() / 2)
    Map.set_snake(snake)
'''
