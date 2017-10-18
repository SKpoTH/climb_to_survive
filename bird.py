import arcade

BIRD_MOVE = 3

VELOCITY_X = 2
VELOCITY_Y = 20
GRAVITY = 9.8

class Bird_Enemy(arcade.Sprite):
    def setup(self, world, x, y, get_position):
        self.center_x = x
        self.center_y = y
        self.world = world

        self.bird_dead = 0

        self.run_time = 0

        self.get_position = get_position
    
    def update(self, delta):
        if self.get_position == 0:
            self.center_x += self.world.bird_move
        elif self.get_position == 1:
            self.center_x -= self.world.bird_move

        if self.bird_dead == 1:
            if self.get_position == 0:
                self.run_time += delta
                self.center_x += VELOCITY_X
                self.center_y -= (VELOCITY_Y*(self.run_time))+(0.5*9.8*((self.run_time)*(self.run_time)))

            elif self.get_position == 1:
                self.run_time += delta
                self.center_x -= VELOCITY_X
                self.center_y -= (VELOCITY_Y*(self.run_time))+(0.5*9.8*((self.run_time)*(self.run_time)))