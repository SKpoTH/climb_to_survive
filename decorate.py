import arcade
from random import randint

CLOUD_SPAWN = 1.2
CLOUD_LIMIT = 5

class Cloud(arcade.Sprite):
    def setup(self, decorate, x, y, move_speed):
        self.center_x = x
        self.center_y = y 
        self.move_speed = move_speed
    
    def update(self, delta):
        self.center_x += self.move_speed

class Decorate:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.cloud_list = []

        self.wait_time_cloud = 0

    def update(self, delta):
        self.wait_time_cloud += delta
        if self.wait_time_cloud >= CLOUD_SPAWN and len(self.cloud_list) <= CLOUD_LIMIT:
            self.cloud = Cloud('images/cloud.png', 0.2*randint(1,3))
            self.cloud.setup(self, 0-(self.cloud.width/2), randint(0,self.height), 0.5*randint(1,4))
            self.cloud_list.append(self.cloud)
            self.wait_time_cloud = 0

        for cloud in self.cloud_list:
            cloud.update(delta)
            if cloud.center_x >= self.width+cloud.width/2:
                self.cloud_list.remove(cloud)
