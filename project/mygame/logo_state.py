from pico2d import *
import game_framework
import play_state
import title_state

# running = True
image_enter = None
image_background = None
logo_time = 0.0

def enter():
    global image_enter, image_background
    image_enter = load_image('logo_enter.png')
    image_background = load_image('logo_background.png')
    pass

def exit():
    global image
    del image
    pass

def update():
    # logo time을 계산하고, 그 결과에 따라 1초가 넘으면 running = False
    global logo_time
    delay(0.01)
    logo_time += 0.01
    if logo_time >= 0.5:
        logo_time = 0
        # running = False
        game_framework.change_state(title_state)
    pass

def draw():
    clear_canvas()
    image.draw(600,400)
    update_canvas()
    pass

def handle_events():
    events = get_events()