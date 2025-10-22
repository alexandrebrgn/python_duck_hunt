import arcade

class AssetsManager:
    background: arcade.Texture
    gunIcon = arcade.Sprite
    goldIcon = arcade.Sprite

    def __init__(self):
        self.sprite_list = arcade.SpriteList()
        self.background = arcade.load_texture('assets/images/background/background-front.png')
        self.gunIcon = arcade.Sprite("assets/images/icons/gun.png", 0.1)
        self.gunIcon.center_x = 900
        self.gunIcon.center_y = 680
        self.sprite_list.append(self.gunIcon)
        self.goldIcon = arcade.Sprite("assets/images/icons/gold.png", 0.02)
        self.goldIcon.center_x = 910
        self.goldIcon.center_y = 620
        self.sight = arcade.Sprite("assets/images/icons/cible.png", 0.1)
        self.sprite_list.append(self.goldIcon)
        self.sprite_list.append(self.sight)
