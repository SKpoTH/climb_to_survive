import arcade

MOVE_LENGTH = 5
PILLAR_FARTHUR = 150 #the Range between a pillar to a pillar

class Human:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.change_y = 0

    def update(self, delta):
        self.y += self.change_y

        #Block player to not go outside playing area
        if self.y >= self.world.height or self.y <= 0:
            self.change_y = 0
        if self.x >= PILLAR_FARTHUR*5:
            self.x = PILLAR_FARTHUR*5
        elif self.x <= PILLAR_FARTHUR*1:
            self.x = PILLAR_FARTHUR*1

class Pillar:
    def __init__(self, world, x, y):
        self.x = x
        self.y = y

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.pillar1 = Pillar(self, PILLAR_FARTHUR*1, 0)
        self.pillar2 = Pillar(self, PILLAR_FARTHUR*2, 0)
        self.pillar3 = Pillar(self, PILLAR_FARTHUR*3, 0)
        self.pillar4 = Pillar(self, PILLAR_FARTHUR*4, 0)
        self.pillar5 = Pillar(self, PILLAR_FARTHUR*5, 0)

        self.human_main = Human(self, PILLAR_FARTHUR*3, height/2)

    def update(self, delta):
        self.human_main.update(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.human_main.change_y = MOVE_LENGTH
            if self.human_main.y >= self.height:
                self.human_main.change_y = 0
            #If state below key I place for blocking player to spam key and player can go out

        if key == arcade.key.DOWN:
            self.human_main.change_y = -MOVE_LENGTH
            if self.human_main.y <= 0:
                self.human_main.change_y = 0

        if key == arcade.key.LEFT:
            self.human_main.x -= PILLAR_FARTHUR
            if self.human_main.x <= PILLAR_FARTHUR*1:
                self.human_main.x -= 0

        if key == arcade.key.RIGHT:
            self.human_main.x += PILLAR_FARTHUR
            if self.human_main.x >= PILLAR_FARTHUR*5:
                self.human_main.x += 0


    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.human_main.change_y = 0
    