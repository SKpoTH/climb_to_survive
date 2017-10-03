import arcade
from models import World

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900

PILLAR_SCALE = 0.6
HUMAN_SCALE = 0.2
'''
class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
 
    def draw(self):
        self.sync_with_model()
        super().draw()
'''

class Get_Sprite:
    def __init__(self, location, model, scale):
        self.model = model
        self.model_sprite = arcade.Sprite(location,scale)

    def draw(self):
        self.model_sprite.set_position(self.model.x, self.model.y)
        self.model_sprite.draw()

class PillSurWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.WHITE)

        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.pillar_sprite1 = Get_Sprite('images/pillar.png',self.world.pillar1,PILLAR_SCALE)
        self.pillar_sprite2 = Get_Sprite('images/pillar.png',self.world.pillar2,PILLAR_SCALE)
        self.pillar_sprite3 = Get_Sprite('images/pillar.png',self.world.pillar3,PILLAR_SCALE)
        self.pillar_sprite4 = Get_Sprite('images/pillar.png',self.world.pillar4,PILLAR_SCALE)
        self.pillar_sprite5 = Get_Sprite('images/pillar.png',self.world.pillar5,PILLAR_SCALE)

        self.human_sprite = Get_Sprite('images/human_climbing.png',self.world.human_main,HUMAN_SCALE)


    def on_draw(self):
        arcade.start_render()
        self.pillar_sprite1.draw()
        self.pillar_sprite2.draw()
        self.pillar_sprite3.draw()
        self.pillar_sprite4.draw()
        self.pillar_sprite5.draw()
        
        self.human_sprite.draw()

    def update(self, delta):
        self.world.update(delta)
    
    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
    
    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)

def main():
    window = PillSurWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()