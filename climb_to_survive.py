import arcade
import pyglet
from world import World

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1260

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
        self.world.pillar6.draw()

        self.world.human_main.draw()
        self.world.human_main_hit.draw()
        
        for spider in self.world.spider_list:
            spider.draw()

        for bird in self.world.bird_list:
            bird.draw()

        for rock in self.world.rock_list:
            rock.draw()

        show_score = 'Score: ' + str(self.world.score)
        arcade.draw_text(show_score, 10, SCREEN_HEIGHT-20, arcade.color.BLACK, 16)

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