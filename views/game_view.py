import arcade

from entities.player.player import Player
from managers.input_manager import InputManager
from entities.ennemies.duck import Duck
from managers.assets_manager import AssetsManager

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.assets = AssetsManager()
        self.player = Player()
        self.speed = 2
        self.input_manager = InputManager()
        arcade.set_background_color(arcade.color.BABY_BLUE)
        self.duck = Duck(self.speed)
        self.assets.sprite_list.append(self.duck)
        self.window.set_mouse_visible(False)

    def on_draw(self):
        self.clear()
        self.assets.sprite_list.draw()
        arcade.draw_text(f": {self.player.kills}", self.window.width - 70, self.window.height - 50, arcade.color.WHITE,
                         20)
        arcade.draw_text(f": {self.player.gold}", self.window.width - 70, self.window.height - 110, arcade.color.WHITE,
                         20)
        arcade.draw_text(f": {self.player.chances}", 70, self.window.height - 20, arcade.color.WHITE,
                         20)
        arcade.draw_texture_rect(
            self.assets.background,
            arcade.LBWH(0, 0, self.window.width, self.window.height),
        )

    def on_update(self, delta_time: float) -> None:
        from views.game_over_view import GameOverView
        self.duck.update(self.window, self.player)
        if not self.duck.alive:
            self.assets.sprite_list.remove(self.duck)
            if self.speed < 20:
                self.speed += 0.5
            self.duck = Duck(self.speed)
            self.assets.sprite_list.extend([self.duck])
        if self.player.chances == 0:
            game_over_view= GameOverView(self.player)
            self.window.show_view(game_over_view)

    def on_key_press(self, key, modifiers):
        self.input_manager.on_key_press(key)

    def on_key_release(self, key, modifiers):
        self.input_manager.on_key_release(key)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        # print(f"{x}, {y}, {button}, {modifiers}")
        if self.duck.check_hit(x, y):
            print(f"{x} et {y} {button} {modifiers}")
            self.player.gold += 10
            self.player.kills += 1

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int) -> None:
        self.assets.sight.center_x = x
        self.assets.sight.center_y = y