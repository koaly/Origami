import arcade.key
from random import randint

MAX_SPEED = 11
MAX_GAP = 0.3

class Object:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.speed = 3
    
    def update(self, delta):
        self.y -= self.speed

class Point(Object):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.cls = 0

class Death(Object):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.cls = 1

class Tmp(Object):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.cls = 2

class Fake(Object):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.cls = 3

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
                self.x += 9
            elif self.move == 2:
                self.x -= 9
        else:
            if self.move != 0:
                self.move = 0
    

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.time = 0
        self.speed = 3
        self.gap = 0.9
        print (self.speed)

        self.life = 1
        self.score = 0

        self.leftTrigger = False
        self.rightTrigger = False

        self.leftObject = []
        self.rightObject = []

        self.leftCheck = []
        self.rightCheck = []

        self.leftCreate = True
        self.rightCreate = True

        self.leftPlane = Plane(self, 62, 100)
        self.rightPlane = Plane(self, 312, 100)

        #self.point = Point(self, 62, 770)
        #self.death = Death(self, 312, 770)
 
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            if self.leftPlane.move == 0:
                if self.leftPlane.x == 62:
                    self.leftPlane.x += 9 
                    self.leftPlane.move = 1
                else:
                    self.leftPlane.x -= 9 
                    self.leftPlane.move = 2
            elif self.leftPlane.move == 1:
                self.leftPlane.move = 2
            else:
                self.leftPlane.move = 1
        if key == arcade.key.RIGHT:
            if self.rightPlane.move == 0:
                if self.rightPlane.x == 312:
                    self.rightPlane.x += 9 
                    self.rightPlane.move = 1
                else:
                    self.rightPlane.x -= 9 
                    self.rightPlane.move = 2
            elif self.rightPlane.move == 1:
                self.rightPlane.move = 2
            else:
                self.rightPlane.move = 1        

    def left_random(self):
        left_pos = randint(0,100)
        left_obj = randint(1,100)
        if left_pos >= 0 and left_pos <= 49:
            if left_obj >= 1 and left_obj <= 40:
                self.leftObject = [Point(self, 62, 800)] + self.leftObject
                self.leftCheck = [0] + self.leftCheck
            elif left_obj >= 41 and left_obj <= 90:
                self.leftObject = [Death(self, 62, 800)] + self.leftObject
                self.leftCheck = [1] + self.leftCheck
            else:
                self.leftObject = [Fake(self, 62, 800)] + self.leftObject
                self.leftCheck = [3] + self.leftCheck
        elif left_pos >= 50 and left_pos <= 99:
            if left_obj >= 1 and left_obj <= 40:
                self.leftObject = [Point(self, 188, 800)] + self.leftObject
                self.leftCheck = [0] + self.leftCheck
            elif left_obj >= 141 and left_obj <= 90:
                self.leftObject = [Death(self, 188, 800)] + self.leftObject
                self.leftCheck = [1] + self.leftCheck
            else:
                self.leftObject = [Fake(self, 188, 800)] + self.leftObject
                self.leftCheck = [3] + self.leftCheck
        else:
            self.leftObject = [Tmp(self, 62, 800)] + self.leftObject
            self.leftCheck = [2] + self.leftCheck
    
    def right_random(self):
        right_pos = randint(0,100)
        right_obj = randint(1,100)
        if right_pos >= 0 and right_pos <= 49:
            if right_obj >= 1 and right_obj <= 40:
                self.rightObject = [Point(self, 312, 800)] + self.rightObject
                self.rightCheck = [0] + self.rightCheck
            elif right_obj >= 41 and right_obj <= 90:
                self.rightObject = [Death(self, 312, 800)] + self.rightObject
                self.rightCheck = [1] + self.rightCheck
            else:
                self.rightObject = [Fake(self, 312, 800)] + self.rightObject
                self.rightCheck = [3] + self.rightCheck
        elif right_pos >= 50 and right_pos <= 99:
            if right_obj >= 1 and right_obj <= 40:
                self.rightObject = [Point(self, 438, 800)] + self.rightObject
                self.rightCheck = [0] + self.rightCheck
            elif right_obj >= 41 and right_obj <= 90:
                self.rightObject = [Death(self, 438, 800)] + self.rightObject
                self.rightCheck = [1] + self.rightCheck
            else:
                self.rightObject = [Fake(self, 438, 800)] + self.rightObject
                self.rightCheck = [3] + self.rightCheck
        else:
            self.rightObject = [Tmp(self, 312, 800)] + self.rightObject
            self.rightCheck = [2] + self.rightCheck

    def left_update(self, delta):
        for obj in self.leftObject:
            if obj.speed > 0 and obj.speed != self.speed:
                obj.speed = self.speed
            obj.update(delta)
            if self.leftPlane.get(obj):
                obj.y = 800
                obj.speed = 0
                if obj.cls == 0:
                    self.score += 1
                    if self.score % 50 == 0:
                        self.life += 1
                    if self.score % 15 == 0:
                        if self.speed <= MAX_SPEED:
                            self.speed += 0.5
                            print (self.speed)
                        if self.gap >= MAX_GAP:
                            self.gap -= 0.05
                elif obj.cls == 1:
                    if self.life > 0:  
                        self.life -= 1
                del obj
                #self.leftObject.pop()
                #self.leftCheck.pop()
            elif obj.y < 10:
                if obj.cls == 0:
                    if self.life > 0:  
                        self.life -= 1
                obj.y = 800
                obj.speed = 0
                del obj
                #self.leftObject.pop()
                #self.leftCheck.pop()
            elif obj.cls == 3:
                if obj.y <= 450:
                    self.leftObject = [Death(self, obj.x, obj.y)] + self.leftObject
                    self.leftCheck = [1] + self.leftCheck
                    self.leftTrigger = True
                    obj.y = 800
                    obj.speed = 0
                    del obj
    
    def right_update(self, delta):
        for obj in self.rightObject:
            if obj.speed > 0 and obj.speed != self.speed:
                obj.speed = self.speed
            obj.update(delta)
            if self.rightPlane.get(obj):
                obj.y = 800
                obj.speed = 0
                if obj.cls == 0:
                    self.score += 1
                    if self.score % 50 == 0:
                        self.life += 1
                    if self.score % 15 == 0:
                        if self.speed <= MAX_SPEED:
                            self.speed += 0.5
                            print (self.speed)
                        if self.gap >= MAX_GAP:
                            self.gap -= 0.05
                elif obj.cls == 1:
                    if self.life > 0:  
                        self.life -= 1
                del obj
                #self.leftObject.pop()
                #self.leftCheck.pop()
            elif obj.y < 10:
                if obj.cls == 0:    
                    if self.life > 0:  
                        self.life -= 1
                obj.y = 800
                obj.speed = 0
                del obj
            elif obj.cls == 3:
                if obj.y <= 450:
                    self.rightObject = [Death(self, obj.x, obj.y)] + self.rightObject
                    self.rightCheck = [1] + self.rightCheck
                    self.rightTrigger = True
                    obj.y = 800
                    obj.speed = 0
                    del obj

    def update(self, delta):
        self.time += delta
        if self.life > 0:
            self.leftPlane.update(delta)
            self.rightPlane.update(delta)
            #print (self.leftObject)
            #if len(self.leftCheck) > 11 or len(self.leftObject) > 11:
            #    self.leftObject.pop()
            #    self.leftCheck.pop()

            if self.time > self.gap:
                self.time = 0
                self.left_random()
                self.right_random()

            self.left_update(delta)
            self.right_update(delta)
        
        #self.point.update(delta)
        #self.death.update(delta)