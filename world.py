import arcade
from random import randint, sample
from models import Human, Pillar, Spider_Enemy, Get_Hit, Rock, Bird_Enemy

'''
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900
'''
HUMAN_MOVE_LENGTH = 5
PILLAR_FARTHUR = 150 #the Range between a pillar to a pillar
SPIDER_MOVE = 2

PILLAR_SCALE = 0.6
HUMAN_SCALE = 0.3

SPIDER_SCALE = 0.3
HIT_SCALE = 0.3

ROCK_SCALE = 0.15

TIME_SCORE = 0.2

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.wait_bird_spawn = 0
        self.wait_spider_spawn = 0
        self.wait_time_score = 0
        
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
        self.human_main_hit = Get_Hit('images/spider_enemy_hitblock.png', HIT_SCALE)

        self.spider_list = []

        self.rock_list = []

        self.bird_list = []

        self.SPIDER_SPAWN_TIME = 1.0
        self.BIRD_SPAWN_TIME = 1.0

        self.score = 0

    def update(self, delta):
        self.human_main.update(delta)
        self.human_main_hit.setup(self, self.human_main.center_x, self.human_main.center_y)
     
        self.wait_spider_spawn += delta
        if self.wait_spider_spawn >= self.SPIDER_SPAWN_TIME:
            self.spider = Spider_Enemy('images/spider_enemy.png', SPIDER_SCALE)
            self.spider.setup(self, PILLAR_FARTHUR*randint(1,5), self.height)
            
            self.spider_list.append(self.spider)
            
            self.wait_spider_spawn -= self.SPIDER_SPAWN_TIME
            self.SPIDER_SPAWN_TIME = 0.5*randint(1,5)

        self.wait_bird_spawn += delta
        if self.wait_bird_spawn >= self.BIRD_SPAWN_TIME:
            self.bird = Bird_Enemy('images/spider_enemy.png', SPIDER_SCALE)
            self.bird.setup(self, 0, randint(0,self.height))
            
            self.bird_list.append(self.bird)
            
            self.wait_bird_spawn -= self.BIRD_SPAWN_TIME
            self.BIRD_SPAWN_TIME = 0.5*randint(1,5)

        
        self.wait_time_score += delta
        if self.wait_time_score >= TIME_SCORE:
            self.score += 1
            self.wait_time_score -= TIME_SCORE
            

        for rock in self.rock_list:
            rock.update(delta)

        for spider in self.spider_list:
            spider.update(delta)

            for rock in self.rock_list:
                if rock.center_x <= 0 or rock.center_y <= 0 or rock.center_x >= self.width or rock.center_y >= self.height:
                    self.rock_list.remove(rock)
                if arcade.geometry.check_for_collision(spider,rock):
                    self.rock_list.remove(rock)
                    self.spider_list.remove(spider)
                    self.score += 10

            if spider.center_y <= 0:
                self.spider_list.remove(spider)

            if arcade.geometry.check_for_collision(spider,self.human_main_hit):
                arcade.window_commands.close_window()

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