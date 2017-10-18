import arcade
import sys
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
        self.leftObject_sprite = []
        self.rightObject_sprite = []

        self.left_len = 0
        self.right_len = 0

        self.scoreboard = arcade.Sprite('images/score.png')
        self.scoreboard.set_position(250,height//2)

        self.scoreCheck = False
        #self.point_sprite = ModelSprite('images/cookie.png',model=self.world.point)
        #self.death_sprite = ModelSprite('images/water.png',model=self.world.death)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def update(self, delta):
        #print (self.leftObject_sprite)
        if len(self.leftObject_sprite) > 11:
           self.leftObject_sprite.pop()

        if len(self.rightObject_sprite) > 11:
            self.rightObject_sprite.pop()
        
        if self.world.leftTrigger:
            if self.world.leftCheck[0] == 1:
                self.leftObject_sprite = [ModelSprite('images/water.png',model=self.world.leftObject[0])] + self.leftObject_sprite
            self.world.leftTrigger = False
        
        if self.world.rightTrigger:
            if self.world.rightCheck[0] == 1:
                self.rightObject_sprite = [ModelSprite('images/water.png',model=self.world.rightObject[0])] + self.rightObject_sprite
            self.world.rightTrigger = False

        if self.world.time == 0:
            if len(self.world.leftCheck) != 0 and len(self.world.leftObject) != 0 and self.left_len != len(self.world.leftObject):
                self.left_len = len(self.world.leftObject)
                if self.world.leftCheck[0] == 0 or self.world.leftCheck[0] == 3:
                    #self.leftObject_sprite.append(ModelSprite('images/cookie.png',model=self.world.leftObject[0]))
                    self.leftObject_sprite = [ModelSprite('images/cookie.png',model=self.world.leftObject[0])] + self.leftObject_sprite
                elif self.world.leftCheck[0] == 1:
                    #self.leftObject_sprite.append(ModelSprite('images/water.png',model=self.world.leftObject[0]))
                    self.leftObject_sprite = [ModelSprite('images/water.png',model=self.world.leftObject[0])] + self.leftObject_sprite
                else:
                    self.leftObject_sprite = [ModelSprite('images/tmp.png',model=self.world.leftObject[0])] + self.leftObject_sprite
       
            if len(self.world.rightCheck) != 0 and len(self.world.rightObject) != 0 and self.right_len != len(self.world.rightObject):
                self.right_len = len(self.world.rightObject)
                if self.world.rightCheck[0] == 0 or self.world.rightCheck[0] == 3:
                    #self.leftObject_sprite.append(ModelSprite('images/cookie.png',model=self.world.leftObject[0]))
                    self.rightObject_sprite = [ModelSprite('images/cookie.png',model=self.world.rightObject[0])] + self.rightObject_sprite
                elif self.world.rightCheck[0] == 1:
                    #self.leftObject_sprite.append(ModelSprite('images/water.png',model=self.world.leftObject[0]))
                    self.rightObject_sprite = [ModelSprite('images/water.png',model=self.world.rightObject[0])] + self.rightObject_sprite
                else:
                    self.rightObject_sprite = [ModelSprite('images/tmp.png',model=self.world.rightObject[0])] + self.rightObject_sprite
                

        self.world.update(delta)

    def on_draw(self):
        arcade.start_render()

        self.background.draw()
 
        self.leftPlane_sprite.draw()
        self.rightPlane_sprite.draw()

        for i in range(0, len(self.leftObject_sprite)):
            if i > 10:
                break
            self.leftObject_sprite[i].draw()

        for i in range(0, len(self.rightObject_sprite)):
            if i > 10:
                break
            self.rightObject_sprite[i].draw()

        #for leftDrop in self.leftObject_sprite:
        #    leftDrop.draw()
        #self.point_sprite.draw()
        #self.death_sprite.draw()

        if self.world.score >= 100:
            arcade.draw_text(str(self.world.score), self.width - 50, self.height - 30, arcade.color.WHITE, 20)
        elif self.world.score >= 10:
            arcade.draw_text(str(self.world.score), self.width - 33, self.height - 30, arcade.color.WHITE, 20)
        else:
            arcade.draw_text(str(self.world.score), self.width - 20, self.height - 30, arcade.color.WHITE, 20)
        arcade.draw_text(str(self.world.life), 8, self.height - 30, arcade.color.WHITE, 20)

        if self.world.life == 0:
            self.scoreboard.draw()
            f = open('highscore.log', 'r')
            highscore = f.readline()
            if self.world.score > int(highscore) or self.scoreCheck:
                self.scoreCheck = True
                arcade.draw_text('New Highscore!', self.width//2-85, self.height//2-75, arcade.color.WHITE, 20)
                f = open('highscore.log', 'w')
                f.write(str(self.world.score))
            else:
                arcade.draw_text('Highscore: ' + highscore, self.width//2-100, self.height//2-75, arcade.color.WHITE, 20)
            if self.world.score >= 100:
                arcade.draw_text(str(self.world.score), self.width//2-80, self.height//2-10, arcade.color.WHITE, 80)
            elif self.world.score >= 10:
                arcade.draw_text(str(self.world.score), self.width//2-55, self.height//2-10, arcade.color.WHITE, 80)
            else:
                arcade.draw_text(str(self.world.score), self.width//2-25, self.height//2-10, arcade.color.WHITE, 80)
 
def main():
    window = TwinWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()
