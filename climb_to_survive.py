import arcade
from models import World

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900

PILLAR_SCALE = 0.6
HUMAN_SCALE = 0.2
SPIDER_SCALE = 0.2

class PillSurWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.WHITE)
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_draw(self):
        arcade.start_render()
        self.world.pillar1.draw()
        self.world.pillar2.draw()
        self.world.pillar3.draw()
        self.world.pillar4.draw()
        self.world.pillar5.draw()
        
        self.world.human_main.draw()
        
        for spider in self.world.spider_list:
            spider.draw()

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