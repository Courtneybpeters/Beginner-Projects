# Magic 8 Ball program

import pyglet

def main():
    window = pyglet.window.Window()
    window.set_size(576, 432)

    background = pyglet.resource.image('magic8_blank.jpg')

    label = pyglet.text.Label('Hello, World',
                              font_name="Arial",
                              font_size=36,
                              x=window.width//2, y=window.height//2,
                              anchor_x='center', anchor_y='center')

    @window.event
    def on_draw():
        window.clear()
        background.blit(0, 0)

    # Displays all events to console - find event names/parameters
    # window.push_handlers(pyglet.window.event.WindowEventLogger())


    pyglet.app.run()

main()
