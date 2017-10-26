import arcade
import pyglet

from world import World
from decorate import Decorate

SCREEN_HEIGHT = 760
SCREEN_WIDTH = 1260

PILLAR_SCALE = 0.6
HUMAN_SCALE = 0.2
SPIDER_SCALE = 0.2

class PillSurWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.decorate = Decorate(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.background = arcade.load_texture("images/background.png")
        
        self.game_title = arcade.load_texture("images/game_title.png")

        self.game_over = arcade.load_texture("images/game_over.png")

        self.tutorial = arcade.load_texture("images/tutorial_screen.png")

        #Get high score from text file
        self.get_score = open("high_score.txt","r")
        self.high_score = int(self.get_score.read())
        self.get_score.close()

        #Add sounds
        self.theme_song = arcade.sound.load_sound('sounds/Darude-Sandstorm.mp3')
        arcade.sound.play_sound(self.theme_song)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        self.world.pillar1.draw()
        self.world.pillar2.draw()
        self.world.pillar3.draw()
        self.world.pillar4.draw()
        self.world.pillar5.draw()
        self.world.pillar6.draw()
            
        #Play Screen
        if self.world.game_state == 1:
            self.world.human_main.draw()
            self.world.human_main_hit.draw()
        
            for spider in self.world.spider_list:
                spider.draw()

            for bird in self.world.bird_list:
                bird.draw()

            for rock in self.world.rock_list:
                rock.draw()

            show_score = 'Score: ' + str(self.world.score)
            arcade.draw_text(show_score, 10, SCREEN_HEIGHT-20, arcade.color.BLACK, 20)

        for cloud in self.decorate.cloud_list:
            cloud.draw()
        
        #Title Screen
        if self.world.game_state == 0:
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT-200,
                                      800, 150, self.game_title)
            arcade.draw_text('Press <SPACE> to continue', 630, 250, 
                            arcade.color.WHITE, 30, 
                            align="center", 
                            anchor_x="center", 
                            anchor_y="center",
                            bold=True, italic=True)

        #Tutorial Screen
        if self.world.game_state == 0.5:
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2)+30,
                                      800, 600, self.tutorial)
            arcade.draw_text('Press <ENTER> to start', 800, 200, 
                                arcade.color.WHITE, 30, 
                                align="center", 
                                anchor_x="center", 
                                anchor_y="center",
                                bold=True, italic=True)

        #Game over Screen
        if self.world.game_state == 2:

            for spider in self.world.spider_list:
                spider.draw()

            for bird in self.world.bird_list:
                bird.draw()

            for rock in self.world.rock_list:
                rock.draw()

            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2)+30,
                                      800, 600, self.game_over)
            
            if self.world.score > self.high_score:
                self.high_score = self.world.score
                self.get_score = open("high_score.txt","w")
                self.get_score.write(str(self.high_score))
                self.get_score.close()

            arcade.draw_text('"'+str(self.high_score)+'"', 420, 400, 
                            arcade.color.WHITE, 30, 
                            align="center", 
                            anchor_x="center", 
                            anchor_y="center",
                            italic=True,bold=False)

            arcade.draw_text(str(self.world.score), 830, 400, 
                            arcade.color.WHITE, 30, 
                            align="center", 
                            anchor_x="center", 
                            anchor_y="center",
                            italic=True,bold=False)

            arcade.draw_text('Press <SPACE> back to title', SCREEN_WIDTH // 2, 250, 
                            arcade.color.WHITE, 30, 
                            align="center", 
                            anchor_x="center", 
                            anchor_y="center",
                            bold=True, italic=True)

    def update(self, delta):
        self.world.update(delta)
        self.decorate.update(delta)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

        if key == arcade.key.SPACE and self.world.game_state == 0:
            self.world.game_state = 0.5

        if key == arcade.key.SPACE and self.world.game_state == 2:
            self.world.game_state = 0

        if key == arcade.key.ENTER and self.world.game_state == 0.5:
            self.decorate.cloud_list = []
            self.world.game_state = 1

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)

def main():
    window = PillSurWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()