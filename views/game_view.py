import random
from random import choice

import arcade

from entities.player.player import Player
from managers.input_manager import InputManager
from entities.ennemies.duck import Duck
from managers.assets_manager import AssetsManager

class GameView(arcade.View):
    assets : AssetsManager()
    speed = 2

    def __init__(self):
        super().__init__()
        self.assets = AssetsManager()
        self.player = Player()

        # Instanciation du premier canard
        self.directions : list[str] = ["dl", "dr", "l", "r", "u"]
        self.duck = None
        self.duck = self.instance_new_duck()
        self.assets.sprite_list.append(self.duck)

        # Aficher la cible du joueur par dessus le reste
        self.window.set_mouse_visible(False)
        self.window.set_exclusive_mouse(True)

        self.sight = arcade.Sprite("assets/images/icons/cible.png", 0.1)
        self.sprite_list2 = arcade.SpriteList()
        self.sprite_list2.append(self.sight)
        self.sight_x = self.window.width // 2
        self.sight_y = self.window.height // 2
        self.sight.center_x = self.sight_x
        self.sight.center_y = self.sight_y
        self.window.set_mouse_visible(False)
        self.window.set_exclusive_mouse(True)

    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.color.BABY_BLUE)
        self.assets.sprite_list.draw()
        arcade.draw_text(f": {self.player.kills}", self.window.width - 70, self.window.height - 50, arcade.color.WHITE,
                         20, font_name="Karmatic Arcade")
        arcade.draw_text(f": {self.player.gold}", self.window.width - 70, self.window.height - 110, arcade.color.WHITE,
                         20, font_name="Karmatic Arcade")
        arcade.draw_text(f": {self.player.chances}", 70, self.window.height - 20, arcade.color.WHITE,
                         20, font_name="Karmatic Arcade")
        arcade.draw_texture_rect(
            self.assets.background,
            arcade.LBWH(0, 0, self.window.width, self.window.height),
        )
        self.sprite_list2.draw()

    def on_update(self, delta_time: float) -> None:
        from views.game_over_view import GameOverView
        self.duck.update(self.window, self.player)
        if not self.duck.alive:
            self.assets.sprite_list.remove(self.duck)
            if self.speed < 20:
                self.speed += 0.5
            self.duck = self.instance_new_duck()
            self.assets.sprite_list.extend([self.duck])
        if self.player.chances == 0:
            game_over_view= GameOverView(self.player)
            self.window.show_view(game_over_view)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        # print(f"{x}, {y}, {button}, {modifiers}")
        if self.duck.check_hit(self.sight_x, self.sight_y):
            print(f"{x} et {y} {button} {modifiers}")
            self.player.gold += 10
            self.player.kills += 1

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int) -> None:
        self.sight_x += dx
        self.sight_y += dy

        # Empêcher la sortie de l'écran
        self.sight_x = max(0, min(self.window.width, self.sight_x))
        self.sight_y = max(0, min(self.window.height, self.sight_y))

        self.sight.center_x = self.sight_x
        self.sight.center_y = self.sight_y

    def instance_new_duck(self):
        direction = random.choice(["dl", "dr", "l", "r", "u"])
        print(direction)
        if direction == "dl":
            duck = Duck(self.speed, self.assets, self.assets.texture_dl_list, direction)
        elif direction == "dr":
            duck = Duck(self.speed, self.assets, self.assets.texture_dr_list, direction)
        elif direction == "r":
            duck = Duck(self.speed, self.assets, self.assets.texture_r_list, direction)
        elif direction == "u":
            duck = Duck(self.speed, self.assets, self.assets.texture_u_list, direction)
        else:
            duck = Duck(self.speed, self.assets, self.assets.texture_l_list, direction)
        return duck