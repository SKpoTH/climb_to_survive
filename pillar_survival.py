import arcade

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900

class PillSurWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.WHITE)
    
    def on_draw(self):
        arcade.start_render()

def main():
    window = PillSurWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()