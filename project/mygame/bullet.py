import pico2d
import game_framework



class bullet:
    def __init__(self):
        self.sx, self.sy = 600, 400
        self.x, self.y = 0, 0
        self.ax, self.ay = 0, 0
        self.cursor = pico2d.load_image('bullet.png')

    def update(self):


    def draw(self):
        self.cursor.draw(self.x, self.y)


def handle_events():
    global x,y
    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_QUIT:
            game_framework.quit()
        elif event.type == pico2d.SDL_MOUSEMOTION:
            x, y = event.x, 800 - 1 - event.y
            if event.button == pico2d.SDL_BUTTON_LEFT:



deil = None

def enter():
    global deil
    deil = bullet()

def exit():
    global deil
    del deil

def update():
    global x, y
    pico2d.hide_cursor()
    deil.x = x
    deil.y = y

def draw():
    pico2d.clear_canvas()
    deil.draw()
    pico2d.update_canvas()