import arcade

from views.game_view import GameView

class GameOverView(arcade.View):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.window.set_mouse_visible(False)
        self.window.set_exclusive_mouse(True)

    def on_draw(self):
        self.clear()
        arcade.draw_text("GAME OVER", self.window.width / 2, self.window.height / 2 + 50, arcade.color.WHITE, 40,
                         anchor_x="center", font_name="Karmatic Arcade")
        arcade.draw_text(f"Score : {self.player.kills} abattus.", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, 20, anchor_x="center", font_name="Karmatic Arcade")
        arcade.draw_text("Appuyez sur ESPACE pour commencer.", self.window.width / 2, self.window.height / 2 - 50,
                         arcade.color.WHITE, 20, anchor_x="center", font_name="Karmatic Arcade")
        arcade.draw_text("Appuyez sur ALT + F4 pour quitter.", self.window.width / 2, self.window.height / 2 - 100,
                         arcade.color.WHITE, 20, anchor_x="center", font_name="Karmatic Arcade")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            game_view = GameView()
            self.window.show_view(game_view)