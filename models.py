import arcade
import math

HUMAN_MOVE_LENGTH = 5
PILLAR_FARTHUR = 150 #the Range between a pillar to a pillar
SPIDER_MOVE = 2

VELOCITY = 10
GRAVITY = 9.8
ANGULAR_TRI = ((math.sqrt(2))/2)


class Human(arcade.Sprite):
    def setup(self, world, x, y):
        self.world = world
        self.center_x = x
        self.center_y = y     
        self.change_y = 0

    def update(self, delta):
        self.center_y += self.change_y

        #Block player to not go outside playing area
        if self.center_y >= self.world.height or self.center_y <= 0:
            self.change_y = 0
        if self.center_x >= PILLAR_FARTHUR*5:
            self.center_x = PILLAR_FARTHUR*5
        elif self.center_x <= PILLAR_FARTHUR*1:
            self.center_x = PILLAR_FARTHUR*1

class Pillar(arcade.Sprite):
    def setup(self, world, x, y):
        self.center_x = x
        self.center_y = y

class Spider_Enemy(arcade.Sprite):
    def setup(self, world, x, y):
        self.center_x = x
        self.center_y = y

    def update(self, delta): 
        self.center_y -= SPIDER_MOVE

class Rock(arcade.Sprite):
    def setup(self, world, x, y, z):
        self.center_x = x
        self.center_y = y
        self.z = z

    def update(self, delta):
        self.center_x += VELOCITY*(self.z)
        #self.center_y -= VELOCITY*ANGULAR_TRI


class Spider_Enemy_Hit(arcade.Sprite):
    def setup(self, would, x, y):
        self.center_x = x
        self.center_y = y
