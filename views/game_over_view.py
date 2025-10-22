import arcade

from views.game_view import GameView

class GameOverView(arcade.View):
    def __init__(self, player):
        super().__init__()
        self.player = player

    def on_draw(self):
        self.clear()
        arcade.draw_text("GAME OVER", self.window.width / 2, self.window.height / 2 + 50, arcade.color.WHITE, 40,
                         anchor_x="center")
        arcade.draw_text(f"Score : {self.player.kills} abatus", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Appuyez sur ESPACE pour commencer", self.window.width / 2, self.window.height / 2 - 50,
                         arcade.color.WHITE, 20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            game_view = GameView()
            self.window.show_view(game_view)