import arcade

MOVE_LENGTH = 5

class Human:
    def __init__(self, world, x, y):
        self.x = x
        self.y = y
        self.change_y = 0
        self.change_x = 0

    def update(self, delta):
        self.y += self.change_y
        self.x += self.change_x

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

        self.human_main = Human(self, 450, 200)

    def update(self, delta):
        self.human_main.update(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.human_main.change_y = MOVE_LENGTH
        if key == arcade.key.DOWN:
            self.human_main.change_y = -MOVE_LENGTH
        if key == arcade.key.LEFT:
            self.human_main.x -= 150
        if key == arcade.key.RIGHT:
            self.human_main.x += 150


    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.human_main.change_y = 0
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.human_main.change_x = 0
    