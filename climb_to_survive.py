import arcade
from models import World

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900

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


class PillSurWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.WHITE)

        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.pillar_sprite1 = ModelSprite('images/pillar.png',model=self.world.pillar1)
        self.pillar_sprite2 = ModelSprite('images/pillar.png',model=self.world.pillar2)
        self.pillar_sprite3 = ModelSprite('images/pillar.png',model=self.world.pillar3)
        self.pillar_sprite4 = ModelSprite('images/pillar.png',model=self.world.pillar4)
        self.pillar_sprite5 = ModelSprite('images/pillar.png',model=self.world.pillar5)

    def on_draw(self):
        arcade.start_render()
        self.pillar_sprite1.draw()
        self.pillar_sprite2.draw()
        self.pillar_sprite3.draw()
        self.pillar_sprite4.draw()
        self.pillar_sprite5.draw()

def main():
    window = PillSurWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()