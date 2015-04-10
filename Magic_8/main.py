# Magic 8 Ball program

import pyglet
import random
import rectangle

def main():

    # Initialize window object and set size
    window = pyglet.window.Window()
    window.set_size(576, 432)

    # Images
    background = pyglet.resource.image('magic8_blank.jpg')
    ask_img = pyglet.resource.image('ask.png')
    clear_img = pyglet.resource.image('clear.png')
    quit_img = pyglet.resource.image('quit.png')

    # Button rectangles
    ask = rectangle.Rectangle(20, 30, 100, 30)
    clear = rectangle.Rectangle(140, 30, 100, 30)
    quit = rectangle.Rectangle(260, 30, 100, 30)


    # Replies
    replies = ['Definitely!', 'Possibly.', 'It\'s in the stars.', 'Nope.',
               'Sorry.', 'No way.', 'No.', 'Yes', 'Try again.', 'Not this time.'
               'Hmmm.', 'Of course.', 'Ha. ..Ha. Ha.', 'Oh yeah. Big time.',
               'Can\'t say', 'Totally!', 'Yep.', 'Naturally, yes.', 'Ohh yeah.']

    # 8 Ball Result
    answer = pyglet.text.Label('',
                              font_name="Arial",
                              font_size=36,
                              x=window.width//2, y=window.height//2,
                              anchor_x='center', anchor_y='center')

    # Drawing event handler
    @window.event
    def on_draw():
        window.clear()
        background.blit(0, 0)
        ask_img.blit(ask.x, ask.y)
        clear_img.blit(clear.x, clear.y)
        quit_img.blit(quit.x, quit.y)
        answer.draw()

    # Button Press event handler
    @window.event
    def on_mouse_press(x, y, button, modifiers):
        within_ask = ask.in_rect(x, y)
        within_clear = clear.in_rect(x, y)
        within_quit = quit.in_rect(x, y)

        if within_ask:
            answer.text = replies[random.randrange(len(replies))]
        if within_clear:
            answer.text = ''
        if within_quit:
            pyglet.app.exit()

    # Displays all events to console - find event names/parameters - debugging
    # window.push_handlers(pyglet.window.event.WindowEventLogger())

    pyglet.app.run()

main()
