import arcade

PILLAR_FARTHUR = 180 #the Range between a pillar to a pillar

class Pillar(arcade.Sprite):
    def setup(self, world, x, y):
        self.center_x = x
        self.center_y = y
        
class Get_Hit(arcade.Sprite):
    def setup(self, would, x, y):
        self.center_x = x
        self.center_y = y
    
