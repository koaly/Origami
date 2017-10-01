import arcade
 
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 750
 
class TwinWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.BLACK)
 
        self.leftPlane_sprite = arcade.Sprite('images/plane.png')
        self.leftPlane_sprite.set_position(62,100)

        self.rightPlane_sprite = arcade.Sprite('images/plane.png')
        self.rightPlane_sprite.set_position(438,100)

    def on_draw(self):
        arcade.start_render()
 
        self.leftPlane_sprite.draw()
        self.rightPlane_sprite.draw()
 
def main():
    window = TwinWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()
