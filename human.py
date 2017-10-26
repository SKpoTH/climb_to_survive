import arcade

HUMAN_MOVE_LENGTH = 5
PILLAR_FARTHUR = 180 #the Range between a pillar to a pillar

VELOCITY = 10
GRAVITY = 9.8

class Human(arcade.Sprite):
    def setup(self, world, x, y):
        self.world = world
        self.center_x = x
        self.center_y = y     
        self.change_y = 0

        self.run_time = 0
        self.previous_pillar = PILLAR_FARTHUR

    def update(self, delta):
        self.center_y += self.change_y

        #Move to the left by gravity
        if self.world.is_pillar_move == -1:
            self.run_time += delta
            self.center_x -= VELOCITY
            self.previous_pillar -= VELOCITY
            self.center_y -= (VELOCITY*(self.run_time))+(0.5*9.8*((self.run_time)*(self.run_time)))
            if  self.previous_pillar == 0:
                self.world.is_pillar_move = 0
                self.previous_pillar = PILLAR_FARTHUR
                self.run_time = 0

        #Move to the right by gravity
        if self.world.is_pillar_move == 1:
            self.run_time += delta
            self.center_x += VELOCITY
            self.previous_pillar -= VELOCITY
            self.center_y -= (VELOCITY*(self.run_time))+(0.5*9.8*((self.run_time)*(self.run_time)))
            if  self.previous_pillar == 0:
                self.world.is_pillar_move = 0
                self.previous_pillar = PILLAR_FARTHUR
                self.run_time = 0

        #Player die and fall down
        if self.world.player_is_dead:
            self.run_time += delta
            self.center_y -= (2*VELOCITY*(self.run_time))+(0.5*9.8*((self.run_time)*(self.run_time)))
            if self.center_y <= -100:
                self.world.game_state = 2
                self.world.player_is_dead = False
                self.run_time = 0

        #Block player to not go outside playing area
        if self.center_y >= self.world.height or self.center_y <= 0:
            self.change_y = 0
        if self.center_x >= PILLAR_FARTHUR*6:
            self.center_x = PILLAR_FARTHUR*6
        elif self.center_x <= PILLAR_FARTHUR*1:
            self.center_x = PILLAR_FARTHUR*1
        
