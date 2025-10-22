import arcade
from managers.input_manager import InputManager
from entities.ennemies.duck import Duck

class GameView(arcade.View):

    def __init__(self):
        super().__init__()
        self.input_manager = InputManager()
        arcade.set_background_color(arcade.color.AMAZON)
        self.duck = Duck(10, 200, 10)
        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(self.duck)

    def on_draw(self):
        self.clear()
        self.sprite_list.draw()
        self.duck.draw_hit_box(color=arcade.color.DARK_BLUE)

    def on_update(self, delta_time: float) ->  None:
        self.duck.update(self.window)
        if not self.duck.alive:
            self.sprite_list.remove(self.duck)
            self.duck = Duck(10, 200, 10)
            self.sprite_list.extend([self.duck])

    def on_key_press(self, key, modifiers):
        self.input_manager.on_key_press(key)


    def on_key_release(self, key, modifiers):
        self.input_manager.on_key_release(key)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        # print(f"{x}, {y}, {button}, {modifiers}")
        if self.duck.check_hit(x, y):
            print(f"{x} et {y} {button} {modifiers}")