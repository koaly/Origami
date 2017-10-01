class Plane:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.move = 0
 
    def update(self, delta):
        if self.x != 188 or self.x != 438 or self.x != 62 or self.x != 312:
            if self.move == 1:
                self.x += 7
            elif self.move == 2:
                self.x -= 7
        else:
            self.move = 0
 
 
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.leftPlane = Plane(self, 62, 100)
        self.rightPlane = Plane(self, 312, 100)
 
 
    def update(self, delta):
        self.leftPlane.update(delta)
        self.rightPlane.update(delta)