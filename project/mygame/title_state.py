from pico2d import *

import game_framework
import character

image = None

def enter():
    global image
    image = load_image('title.png')
    pass

def exit():
    global image
    del image
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(character)
    pass

def draw():
    clear_canvas()
    image.draw(600,400)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass






