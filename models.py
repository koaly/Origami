import arcade.key

class Point:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.speed = 3
    
    def update(self, delta):
        self.y -= self.speed

class Plane:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.move = 0

    def get(self, other):
         return (abs(self.x - other.x) <= 30) and (abs(self.y - other.y) <= 30)
 
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

        self.life = 1
        self.score = 0
        self.leftPlane = Plane(self, 62, 100)
        self.rightPlane = Plane(self, 312, 100)
        self.point = Point(self, 62, 770)
 
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT:
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
        if key == arcade.key.RIGHT:
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
        self.point.update(delta)

        if self.point.y < 10:
            self.life -= 1
            if life == 0:
                self.point.y = 10
            else:
                self.point.y = 770
            self.point.speed = 0

        if self.leftPlane.get(self.point):
            #self.point.y = 770
            self.point.speed = 0
            self.score += 1
