import arcade
from managers.input_manager import InputManager

class GameView(arcade.View):
    """Vue principale du jeu."""

    def __init__(self):
        super().__init__()
        self.input_manager = InputManager()

    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        self.clear()

    def on_key_press(self, key, modifiers):
        self.input_manager.on_key_press(key)

    def on_key_release(self, key, modifiers):
        self.input_manager.on_key_release(key)
