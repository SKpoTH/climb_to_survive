import arcade
from random import randint

HUMAN_MOVE_LENGTH = 5
PILLAR_FARTHUR = 150 #the Range between a pillar to a pillar
SPIDER_MOVE = 2

PILLAR_SCALE = 0.6
HUMAN_SCALE = 0.2
SPIDER_SCALE = 0.2

SPAWN_TIME = 1.0

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

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.wait = 0
        
        self.pillar1 = Pillar('images/pillar.png', PILLAR_SCALE)
        self.pillar1.setup(self, PILLAR_FARTHUR*1, 0)

        self.pillar2 = Pillar('images/pillar.png', PILLAR_SCALE)
        self.pillar2.setup(self, PILLAR_FARTHUR*2, 0)

        self.pillar3 = Pillar('images/pillar.png', PILLAR_SCALE)
        self.pillar3.setup(self, PILLAR_FARTHUR*3, 0)
        
        self.pillar4 = Pillar('images/pillar.png', PILLAR_SCALE)
        self.pillar4.setup(self, PILLAR_FARTHUR*4, 0)
        
        self.pillar5 = Pillar('images/pillar.png', PILLAR_SCALE)
        self.pillar5.setup(self, PILLAR_FARTHUR*5, 0)

        self.human_main = Human('images/human_climbing.png', HUMAN_SCALE)
        self.human_main.setup(self, PILLAR_FARTHUR*3, height/2)

        self.spider_list = []

    def update(self, delta):
        self.human_main.update(delta)
        
        self.wait += delta
        if self.wait >= SPAWN_TIME:
            self.spider = Spider_Enemy('images/spider_enemy.png', SPIDER_SCALE)
            self.spider.setup(self, PILLAR_FARTHUR*randint(1,5), self.height)
            self.spider_list.append(self.spider)
            self.wait -= SPAWN_TIME
        
        for spider in self.spider_list:
            spider.update(delta)
            if spider.center_y <= 0:
                self.spider_list.remove(spider)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.human_main.change_y = HUMAN_MOVE_LENGTH
            if self.human_main.center_y >= self.height:
                self.human_main.change_y = 0
            #If state below key I place for blocking player to spam key and player can go out

        if key == arcade.key.DOWN:
            self.human_main.change_y = -HUMAN_MOVE_LENGTH
            if self.human_main.center_y <= 0:
                self.human_main.change_y = 0

        if key == arcade.key.LEFT:
            self.human_main.center_x -= PILLAR_FARTHUR
            if self.human_main.center_x <= PILLAR_FARTHUR*1:
                self.human_main.center_x -= 0

        if key == arcade.key.RIGHT:
            self.human_main.center_x += PILLAR_FARTHUR
            if self.human_main.center_x >= PILLAR_FARTHUR*5:
                self.human_main.center_x += 0

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.human_main.change_y = 0
