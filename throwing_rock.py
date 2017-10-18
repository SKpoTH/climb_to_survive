import arcade

VELOCITY = 10
GRAVITY = 9.8

class Rock(arcade.Sprite):
    def setup(self, world, x, y, z):
        self.center_x = x
        self.center_y = y
        self.z = z
        self.run_time = 0

    def update(self, delta):
        self.run_time += delta
        self.center_x += VELOCITY*(self.z)
        self.center_y -= (VELOCITY*(self.run_time))+(0.5*9.8*((self.run_time)*(self.run_time)))