import arcade

class Pillar:
    def __init__(self, world, x, y):
        self.x = x
        self.y = y

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.pillar1 = Pillar(self, 150, 0)
        self.pillar2 = Pillar(self, 300, 0)
        self.pillar3 = Pillar(self, 450, 0)
        self.pillar4 = Pillar(self, 600, 0)
        self.pillar5 = Pillar(self, 750, 0)