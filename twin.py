import arcade
from models import *
 
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 750
 
class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
 
    def draw(self):
        self.sync_with_model()
        super().draw()

class TwinWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.BLACK)
        
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.background = arcade.Sprite('images/bg.png')
        self.background.set_position(250,375)
 
        self.leftPlane_sprite = ModelSprite('images/plane.png',model=self.world.leftPlane)
        self.rightPlane_sprite = ModelSprite('images/plane.png',model=self.world.rightPlane)
        self.point_sprite = ModelSprite('images/cookie.png',model=self.world.point)
        self.death_sprite = ModelSprite('images/water.png',model=self.world.death)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def update(self, delta):
        self.world.update(delta)

    def on_draw(self):
        arcade.start_render()

        self.background.draw()
 
        self.leftPlane_sprite.draw()
        self.rightPlane_sprite.draw()
        self.point_sprite.draw()
        self.death_sprite.draw()

        if self.world.score >= 100:
            arcade.draw_text(str(self.world.score), self.width - 50, self.height - 30, arcade.color.WHITE, 20)
        elif self.world.score >= 10:
            arcade.draw_text(str(self.world.score), self.width - 33, self.height - 30, arcade.color.WHITE, 20)
        else:
            arcade.draw_text(str(self.world.score), self.width - 20, self.height - 30, arcade.color.WHITE, 20)
        arcade.draw_text(str(self.world.life), 8, self.height - 30, arcade.color.WHITE, 20)

 
def main():
    window = TwinWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()
