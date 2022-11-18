from pico2d import *
import game_framework
import play_state

image_enter = None
image_background = None

map_w = 2000
map_h = 1200

def enter():
    global image_enter, image_background
    image_enter = load_image('logo_enter.png')
    image_background = load_image('background.png')

def exit():
    global image_enter, image_background
    del image_enter, image_background

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if (event.type, event.key) == (pico2d.SDL_KEYDOWN, pico2d.SDLK_ESCAPE):
            game_framework.quit()
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(play_state)
    pass

def draw():
    clear_canvas()
    image_background.draw(1000, 600, 3000, 4000)
    image_enter.clip_draw(0, 0, 436, 139, map_w / 2, map_h / 2, 1000, 300)


    update_canvas()

    # self.image_idle.clip_draw(int(self.frame) * 40, 62, 40, 62, self.x, self.y, 120, 120)

def update():
    pass

def pause():
    pass

def resume():
    pass






