import random
from random import randint

import arcade

from managers.assets_manager import AssetsManager


class Duck(arcade.Sprite):
    def __init__(self, speed):
        super().__init__("assets/sprites/duck.png", scale=0.15)
        self.directions = ["diagonal_left", "diagonal_right", "left", "right", "up"]
        self.direction = random.choice(self.directions)
        self.choose_x_y(self.direction)
        self.speed = speed
        self.alive = True

    def update(self, my_screen, player):
        if not self.alive:
            return

        if self.direction == "left":
            self.center_x -= self.speed
        elif self.direction == "right":
            self.center_x += self.speed
        elif self.direction == "up":
            self.center_y += self.speed
        elif self.direction == "diagonal_left":
            self.center_x += self.speed
            self.center_y += self.speed / 2
        elif self.direction == "diagonal_right":
            self.center_x += self.speed / 2
            self.center_y -= self.speed

        if (
            self.center_x > my_screen.width or
            self.center_y > my_screen.height or
            self.center_x < 0 or
            self.center_y < 0
        ):
            self.alive = False
            player.chances -= 1


    def check_hit(self, x, y):
        if self.alive and self.collides_with_point((x, y)):
            self.alive = False
            return True
        return False

    def choose_x_y(self, direction):
        if direction == "diagonal_left":
            print("diagonal_left")
            self.center_x = 100
            self.center_y = random.randint(200, 250)
        elif direction == "diagonal_right":
            print("diagonal_right")
            self.center_x = 1120
            self.center_y = random.randint(200, 250)
        elif direction == "left":
            print("left")
            self.center_x = 1120
            self.center_y = random.randint(300, 450)
        elif direction == "right":
            print("right")
            self.center_x = 100
            self.center_y = random.randint(300, 450)
        elif direction == "up":
            print("up")
            self.center_x = random.randint(200, 980)
            self.center_y = 150