import random
from random import randint

import arcade


class Duck(arcade.Sprite):
    def __init__(self, speed, assets, texture_list: list[arcade.Texture], direction):
        super().__init__(texture_list[0])
        self.assets= assets
        self.direction = direction
        self.choose_x_y(self.direction)
        self.speed = speed
        self.alive = True
        self.scale = 80 / self.width
        self.textures = texture_list
        self.time_elapsed = 0
        self.current_texture_index = 0
        self.frame_count = 0

    def update(self, my_screen, player, delta_time: float = 1/ 60):
        self.frame_count += 1

        if not self.alive:
            return

        # Gérer l'animation du canard
        if self.frame_count % 15 == 0:
            self.current_texture_index = (self.current_texture_index + 1) % len(self.textures)
            self.set_texture(self.current_texture_index)

        # Gérer le déplacement du canard
        if self.direction == "L":
            self.center_x -= self.speed
        elif self.direction == "R":
            self.center_x += self.speed
        elif self.direction == "U":
            self.center_y += self.speed
        elif self.direction == "DL":
            self.center_x -= self.speed
            self.center_y += self.speed / 2
        elif self.direction == "DR":
            self.center_x += self.speed
            self.center_y += self.speed / 2

        # Gérer la fuite du canard
        if (
            self.center_x > my_screen.width or
            self.center_y > my_screen.height or
            self.center_x < 0 or
            self.center_y < 0
        ):
            self.alive = False
            player.chances -= 1


    # Vérification si le canard est touché
    def check_hit(self, x, y):
        if self.alive and self.collides_with_point((x, y)):
            self.alive = False
            return True
        return False

    # Gérer l'apparition du canard
    def choose_x_y(self, direction):
        if direction == "DL":
            self.center_x = random.randint(600, 900)
            self.center_y = random.randint(150, 200)
        elif direction == "DR":
            self.center_x = random.randint(100, 400)
            self.center_y = random.randint(150, 200)
        elif direction == "L":
            self.center_x = 900
            self.center_y = random.randint(300, 450)
        elif direction == "R":
            self.center_y = random.randint(300, 450)
        elif direction == "U":
            self.center_x = random.randint(200, 980)
            self.center_y = 150