import arcade
from arcade import load_texture

class AssetsManager:
    background: arcade.Texture
    gunIcon = arcade.Sprite
    goldIcon = arcade.Sprite

    def __init__(self, window):
        self.sprite_list = arcade.SpriteList()
        self.sprite_list2 = arcade.SpriteList()

        self.duck_dl_sheet = arcade.load_spritesheet("assets/sprites/duck-dl/spritesheet-dl.png")
        self.texture_dl_list = self.duck_dl_sheet.get_texture_grid(size=(1056, 1056), columns=4, count=4)

        self.duck_dr_sheet = arcade.load_spritesheet("assets/sprites/duck-dr/spritesheet-dr.png")
        self.texture_dr_list = self.duck_dr_sheet.get_texture_grid(size=(1056, 1056), columns=4, count=4)

        self.duck_r_sheet = arcade.load_spritesheet("assets/sprites/duck-r/spritesheet-r.png")
        self.texture_r_list = self.duck_r_sheet.get_texture_grid(size=(1088, 1088), columns=4, count=4)

        self.duck_l_sheet = arcade.load_spritesheet("assets/sprites/duck-l/spritesheet-l.png")
        self.texture_l_list = self.duck_l_sheet.get_texture_grid(size=(1088, 1088), columns=4, count=4)

        self.duck_u_sheet = arcade.load_spritesheet("assets/sprites/duck-u/spritesheet-u.png")
        self.texture_u_list = self.duck_u_sheet.get_texture_grid(size=(1056, 1056), columns=4, count=4)

        self.background = arcade.load_texture('assets/images/background/background-front.png')
        self.gunIcon = arcade.Sprite("assets/images/icons/gun.png", 0.1)
        self.gunIcon.center_x = 900
        self.gunIcon.center_y = 680
        self.sprite_list.append(self.gunIcon)
        self.goldIcon = arcade.Sprite("assets/images/icons/gold.png", 0.02)
        self.goldIcon.center_x = 910
        self.goldIcon.center_y = 620
        self.sprite_list.append(self.goldIcon)
        self.heartIcon = arcade.Sprite("assets/images/icons/heart.png", 0.1)
        self.heartIcon.center_x = 50
        self.heartIcon.center_y = 680
        self.sprite_list2.append(self.heartIcon)

        self.sight = arcade.Sprite("assets/images/icons/cible.png", 0.1)
        self.sprite_list2.append(self.sight)
        print(window.width, window.height)
        self.sight_x = window.width / 2
        self.sight_y = window.height / 2
        self.sight.center_x = self.sight_x
        self.sight.center_y = self.sight_y
