import arcade
 
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 950
 
class TwinWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.BLACK)
 
        self.plane1_sprite = arcade.Sprite('images/plane.jpg')
        self.plane1_sprite.set_position(100,100)

    def on_draw(self):
        arcade.start_render()
 
        self.plane1_sprite.draw()
 
def main():
    window = TwinWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()
