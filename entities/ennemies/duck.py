import random
import arcade

class Duck(arcade.Sprite):
    def __init__(self, x, y, speed):
        super().__init__("assets/sprites/duck.png", scale=0.5)
        self.center_x = x
        self.center_y = y
        self.speed = speed
        self.alive = True
        self.directions = ["diagonal", "left", "right", "up"]
        self.direction = random.choice(self.directions)

    def update(self, my_screen):
        if not self.alive:
            return

        if self.direction == "left":
            self.center_x -= self.speed
        elif self.direction == "right":
            self.center_x += self.speed
        elif self.direction == "up":
            self.center_y += self.speed
        elif self.direction == "diagonal":
            self.center_x += self.speed
            self.center_y += self.speed / 2

        if (
            self.center_x > my_screen.width or
            self.center_y > my_screen.height or
            self.center_x < 0 or
            self.center_y < 0
        ):
            self.alive = False

    def check_hit(self, x, y):
        if self.alive and self.collides_with_point((x, y)):
            self.alive = False
            return True
        return False
