import arcade
from random import randint
from models import Human, Pillar, Spider_Enemy, Spider_Enemy_Hit, Rock

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900

HUMAN_MOVE_LENGTH = 5
PILLAR_FARTHUR = 150 #the Range between a pillar to a pillar
SPIDER_MOVE = 2

PILLAR_SCALE = 0.6
HUMAN_SCALE = 0.3

SPIDER_SCALE = 0.3
SPIDER_HIT_SCALE = 0.2

SPAWN_TIME = 1.0

ROCK_SCALE = 0.1

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
        self.spider_hit_list = []

        self.rock_list = []

    def update(self, delta):
        self.human_main.update(delta)
     
        self.wait += delta
        if self.wait >= SPAWN_TIME:
            self.spider = Spider_Enemy('images/spider_enemy.png', SPIDER_SCALE)
            self.spider.setup(self, PILLAR_FARTHUR*randint(1,5), self.height)
            
            self.spider_list.append(self.spider)

            self.spider_hit = Spider_Enemy_Hit('images/spider_enemy_hitblock.png', SPIDER_HIT_SCALE)
            self.spider_hit.setup(self, self.spider.center_x, self.spider.center_y)

            self.spider_hit_list.append(self.spider_hit)
            
            self.wait -= SPAWN_TIME
        
        for spider_hit in self.spider_hit_list:
            spider_hit.center_y -= SPIDER_MOVE

            for rock in self.rock_list:
                rock.update(delta)
                if rock.center_x <= 0 or rock.center_y <= 0 or rock.center_x >= self.width or rock.center_y >= self.height:
                    self.rock_list.remove(rock)
                if arcade.geometry.check_for_collision(spider_hit,rock):
                    self.rock_list.remove(rock)
                    self.spider_hit_list.remove(spider_hit)

            if spider_hit.center_y <= 0:
                self.spider_hit_list.remove(spider_hit)

            if arcade.geometry.check_for_collision(spider_hit,self.human_main):
                arcade.window_commands.close_window()

        for spider in self.spider_list:
            spider.update(delta)
            if spider.center_y <= 0:
                self.spider_list.remove(spider)

        for rock in self.rock_list:
            rock.update(delta)
            if rock.center_x <= 0 or rock.center_y <= 0 or rock.center_x >= self.width or rock.center_y >= self.height:
                self.rock_list.remove(rock)
                

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

            #Throw Rock
        if key == arcade.key.Z:
            self.rock = Rock('images/spider_enemy_hitblock.png', ROCK_SCALE)
            self.rock.setup(self, self.human_main.center_x, self.human_main.center_y, -1)
            self.rock_list.append(self.rock)

        if key == arcade.key.X:
            self.rock = Rock('images/spider_enemy_hitblock.png', ROCK_SCALE)
            self.rock.setup(self, self.human_main.center_x, self.human_main.center_y, 1)
            self.rock_list.append(self.rock)

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.human_main.change_y = 0