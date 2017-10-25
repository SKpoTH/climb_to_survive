import arcade
from random import randint

from human import Human
from spider import Spider_Enemy
from bird import Bird_Enemy
from throwing_rock import Rock
from models import Pillar, Get_Hit

HUMAN_MOVE_LENGTH = 5
PILLAR_FARTHUR = 180 #the Range between a pillar to a pillar
SPIDER_MOVE = 2

PILLAR_SCALE = 0.7
HUMAN_SCALE = 0.35

SPIDER_SCALE = 0.3
HIT_SCALE = 0.3

ROCK_SCALE = 0.1

TIME_SCORE = 0.2

MOVE_RATE = 0.5

SPAWN_RATE = 0.1

NEXT_LEVEL_MULTI = 1.2

class World:
    def __init__(self, width, height):
        #SCREEN SIZE
        self.width = width
        self.height = height
        
        #CHECK Move to another pillar
        self.is_pillar_move = 0

        #Delay of monster spawning
        self.wait_bird_spawn = 0
        self.wait_spider_spawn = 0
        
        self.bird_spawn_time = 1.0
        self.spider_spawn_time = 1.0

        self.spawn_rate = 1.0

        #Monster movement speed
        self.spider_move = 2
        self.bird_move = 1.5
        
        #Count Score
        self.wait_time_score = 0
        self.score = 0

        #Level
        self.level_speed_up = 100
        self.level_spawn_up = 50

        self.speed_score = 0
        self.spawn_score = 0

        #Game State
        self.game_state = 0
        
        #Setup All Pillar
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

        self.pillar6 = Pillar('images/pillar.png', PILLAR_SCALE)
        self.pillar6.setup(self, PILLAR_FARTHUR*6, 0)

        #Setup main charractor and hit block 
        self.human_main = Human('images/human_model.png', HUMAN_SCALE)
        self.human_main.setup(self, PILLAR_FARTHUR*3, self.height/2)
        self.human_main_hit = Get_Hit('images/spider_enemy_hitblock.png', HIT_SCALE)

        #Set monster in group for append or remove
        self.spider_list = []
        self.bird_list = []
        
        self.rock_list = []

    def update(self, delta):
        
        if self.game_state == 0.5:
            self.spider_list = []
            self.bird_list = []

            self.speed_score = 0
            self.spawn_score = 0
            self.score = 0

            self.level_speed_up = 100
            self.level_spawn_up = 50

            self.spider_move = 2
            self.bird_move = 1.5

            self.human_main.setup(self, PILLAR_FARTHUR*3, self.height/2)

        if self.game_state == 1:
            self.human_main.update(delta)
            self.human_main_hit.setup(self, self.human_main.center_x, self.human_main.center_y)

            #Spider spawning
            self.wait_spider_spawn += delta
            if self.wait_spider_spawn >= self.spider_spawn_time:
                self.spider = Spider_Enemy('images/spider_enemy.png', SPIDER_SCALE)
                self.spider.setup(self, PILLAR_FARTHUR*randint(1,6), self.height)
            
                self.spider_list.append(self.spider)
            
                self.wait_spider_spawn -= self.spider_spawn_time
                self.spider_spawn_time = self.spawn_rate*randint(1,5)

            #Bird spawning
            self.wait_bird_spawn += delta
            if self.wait_bird_spawn >= self.bird_spawn_time:
                self.bird_position = randint(0,1)
            
                if self.bird_position == 0:
                    self.bird = Bird_Enemy('images/bird_model_right.png', SPIDER_SCALE)
                elif self.bird_position == 1:
                    self.bird = Bird_Enemy('images/bird_model_left.png', SPIDER_SCALE)

                self.bird.setup(self, self.width*self.bird_position, randint(50,self.height-50), self.bird_position)
            
                self.bird_list.append(self.bird)

                self.wait_bird_spawn -= self.bird_spawn_time
                self.bird_spawn_time = self.spawn_rate*randint(1,8)

            #Score counting
            self.wait_time_score += delta
            if self.wait_time_score >= TIME_SCORE:
                self.score += 1
                self.speed_score += 1
                self.spawn_score += 1
                self.wait_time_score -= TIME_SCORE
        
            if self.speed_score >= self.level_speed_up:
                self.speed_score -= self.level_speed_up
                self.level_speed_up = self.level_speed_up*NEXT_LEVEL_MULTI
                self.spider_move += MOVE_RATE
                self.bird_move += MOVE_RATE

            if self.spawn_score >= self.level_spawn_up:
                self.spawn_score -= self.level_spawn_up
                self.level_spawn_up = self.level_spawn_up*NEXT_LEVEL_MULTI
                self.spawn_rate -= SPAWN_RATE

            #============Make everything go on===================
            #Rock action
            for rock in self.rock_list:
                rock.update(delta)
                if rock.center_x <= 0 or rock.center_y <= 0 or rock.center_x >= self.width or rock.center_y >= self.height:
                    self.rock_list.remove(rock)
            
            #Bird Action
            for bird in self.bird_list:
                bird.update(delta)

                for rock in self.rock_list:
                    if arcade.geometry.check_for_collision(bird,rock):
                        self.rock_list.remove(rock)
                        bird.bird_dead = 1
                        self.score += 10
                        self.speed_score += 10
                        self.spawn_score += 10

                if bird.get_position == 0 and bird.center_x >= self.width:
                    self.bird_list.remove(bird)
                elif bird.get_position == 1 and bird.center_x == 0:
                    self.bird_list.remove(bird)
            
                elif bird.center_y <= 0:
                    self.bird_list.remove(bird)

                if arcade.geometry.check_for_collision(bird, self.human_main_hit):
                    self.game_state = 2

            #Spider Action
            for spider in self.spider_list:
                spider.update(delta)

                for rock in self.rock_list:
                    if arcade.geometry.check_for_collision(spider,rock):
                        self.rock_list.remove(rock)
                        spider.spider_dead = 1
                        self.score += 5
                        self.speed_score += 5
                        self.spawn_score += 5

                if spider.center_y <= 0:
                    self.spider_list.remove(spider)

                if arcade.geometry.check_for_collision(spider,self.human_main_hit):
                    self.game_state = 2

        elif self.game_state == 2:

            #Rock Continue move
            for rock in self.rock_list:
                rock.update(delta)
                if rock.center_x <= 0 or rock.center_y <= 0 or rock.center_x >= self.width or rock.center_y >= self.height:
                    self.rock_list.remove(rock)

            #Spider Continue move
            for spider in self.spider_list:
                spider.update(delta)

                if spider.center_y <= 0:
                    self.spider_list.remove(spider)

            #Bird Continue move
            for bird in self.bird_list:
                bird.update(delta)

                if bird.get_position == 0 and bird.center_x >= self.width:
                    self.bird_list.remove(bird)
                elif bird.get_position == 1 and bird.center_x == 0:
                    self.bird_list.remove(bird)

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
            self.is_pillar_move = -1
            if self.human_main.center_x <= PILLAR_FARTHUR*1:
                self.human_main.center_x -= 0

        if key == arcade.key.RIGHT:
            self.is_pillar_move = 1
            if self.human_main.center_x >= PILLAR_FARTHUR*5:
                self.human_main.center_x += 0

        #Throw Rock
        if key == arcade.key.Z and len(self.rock_list) <= 2:
            self.rock = Rock('images/rock_model.png', ROCK_SCALE)
            self.rock.setup(self, self.human_main.center_x, self.human_main.center_y, -1)
            self.rock_list.append(self.rock)

        if key == arcade.key.X and len(self.rock_list) <= 2:
            self.rock = Rock('images/rock_model.png', ROCK_SCALE)
            self.rock.setup(self, self.human_main.center_x, self.human_main.center_y, 1)
            self.rock_list.append(self.rock)

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.human_main.change_y = 0