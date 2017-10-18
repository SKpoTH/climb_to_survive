import arcade

GRAVITY = 9.8
VELOCITY = 20

class Spider_Enemy(arcade.Sprite):
    def setup(self, world, x, y):
        self.center_x = x
        self.center_y = y
        self.world = world

        self.run_time = 0
        self.spider_dead = 0

    def update(self, delta): 
        if self.spider_dead == 1:
            self.run_time += delta
            self.center_y -= (VELOCITY*self.run_time)+(0.5*GRAVITY*self.run_time*self.run_time)

        else:
            self.center_y -= self.world.spider_move
