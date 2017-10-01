import arcade.key

class Plane:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.move = 0
 
    def update(self, delta):
        if self.x != 188 and self.x != 438 and self.x != 62 and self.x != 312:
            if self.move == 1:
                self.x += 6
            elif self.move == 2:
                self.x -= 6
        else:
            if self.move != 0:
                self.move = 0
 
 
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.leftPlane = Plane(self, 62, 100)
        self.rightPlane = Plane(self, 312, 100)
 
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.D:
            if self.leftPlane.move == 0:
                if self.leftPlane.x == 62:
                    self.leftPlane.x += 6 
                    self.leftPlane.move = 1
                else:
                    self.leftPlane.x -= 6 
                    self.leftPlane.move = 2
            elif self.leftPlane.move == 1:
                self.leftPlane.move = 2
            else:
                self.leftPlane.move = 1
        if key == arcade.key.J:
            if self.rightPlane.move == 0:
                if self.rightPlane.x == 312:
                    self.rightPlane.x += 6 
                    self.rightPlane.move = 1
                else:
                    self.rightPlane.x -= 6 
                    self.rightPlane.move = 2
            elif self.rightPlane.move == 1:
                self.rightPlane.move = 2
            else:
                self.rightPlane.move = 1        

    def update(self, delta):
        self.leftPlane.update(delta)
        self.rightPlane.update(delta)