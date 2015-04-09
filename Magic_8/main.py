# Magic 8 Ball program

import pyglet

def main():

    # Initialize window object and resize
    window = pyglet.window.Window()
    window.set_size(576, 432)

    # Images
    background = pyglet.resource.image('magic8_blank.jpg')
    ask = pyglet.resource.image('ask.png')
    clear = pyglet.resource.image('clear.png')
    quit = pyglet.resource.image('quit.png')

    # Image coordinates
    y = 30
    ask_x = 20
    clear_x = 140
    quit_x = 260


    # label = pyglet.text.Label('Hello, World',
    #                           font_name="Arial",
    #                           font_size=36,
    #                           x=window.width//2, y=window.height//2,
    #                           anchor_x='center', anchor_y='center')

    @window.event
    def on_draw():
        window.clear()
        background.blit(0, 0)
        ask.blit(ask_x, y)
        clear.blit(clear_x, y)
        quit.blit(quit_x, y)


    # Displays all events to console - find event names/parameters
    # window.push_handlers(pyglet.window.event.WindowEventLogger())


    pyglet.app.run()

main()
