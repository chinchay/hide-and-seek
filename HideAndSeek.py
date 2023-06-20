from typing import Optional, Tuple
import arcade
# import pyglet

# SCREEN_WIDTH = 400
# SCREEN_HEIGHT = 400
# SCREEN_TITLE = "Hide and seek"

# customized from https://github.com/pythonarcade/template/blob/master/source_code/main.py

class HideAndSeek( arcade.Window ):
    # def __init__(self, width: int = 800, height: int = 600, title: str | None = 'Arcade Window', fullscreen: bool = False, resizable: bool = False, update_rate: float | None = 1 / 60, antialiasing: bool = True, gl_version: Tuple[int, int] = ..., screen: XlibScreen = None, style: str | None = pyglet.window.Window.WINDOW_STYLE_DEFAULT, visible: bool = True, vsync: bool = False, gc_mode: str = "context_gc", center_window: bool = False, samples: int = 4, enable_polling: bool = True):
    #     super().__init__(width, height, title, fullscreen, resizable, update_rate, antialiasing, gl_version, screen, style, visible, vsync, gc_mode, center_window, samples, enable_polling)

    def __init__(self) -> None:
        super().__init__(width=400, height=400, title="Hide and seek!")
        
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        # arcade.set_background_color( (0, 0, 0, 0) )


        pass

    def setup(self):
        img = "images/pacman.png"
        scaling = 1
        self.player_sprite = arcade.Sprite(img, scaling)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100

        self.player_list = arcade.SpriteList()
        self.player_list.append( self.player_sprite )
        pass

    def on_draw(self):
        # this will allow to color the screen and render in general
        arcade.start_render() 

        # other stuff

        self.player_list.draw()

        # finish rendering
        # arcade.finish_render()


        ### return super().on_draw()

        pass



def main():
    game = HideAndSeek()
    game.setup()
    arcade.run()
    pass

if __name__ == "__main__":
    main()
    # arcade.open_window(600, 600, 'Coin Game')
    # arcade.set_background_color(arcade.color.WHEAT)
    # arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
    # arcade.run()