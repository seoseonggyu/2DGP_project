from pico2d import *


class bullet:
    def __init__(self):
        self.sx, self.sy = 600, 400
        self.x, self.y = 0, 0
        self.ax, self.ay = 0, 0
        self.t = 0
        self.bullet = pico2d.load_image('bullet.png')


    def update(self):
        self.t += 0.002
        self.x = (1 - self.t) * self.sx + self.t * self.ax
        self.y = (1 - self.t) * self.sy + self.t * self.ay

    def draw(self):
        self.cursor.draw(self.x, self.y)



def handle_events():
    global running
    global ax, ay
    global x, y
    global deil
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_MOUSEMOTION:
             x, y = event.x, 800 - 1 - event.y
             if event.button == pico2d.SDL_BUTTON_LEFT:
                 deil = bullet()
                 ax = event.x
                 ay = event.y



open_canvas(1200, 800)

cursor = pico2d.load_image('gun_cursor.png')

deil = None
running = True

sx, sy = 400, 300
x, y = 400, 300
ax, ay = x, y
hide_cursor()
t = 0

def reset_world():
    global ax, ay
    global t
    global sx, sy
    global x, y
    t = 0
    sx, sy = x, y


def update_world():
    global x, y
    global t
    t += 0.002
    x = (1-t)*sx + t*ax
    y = (1-t)*sy + t*ay

    if t >= 1.0:
        reset_world()

reset_world()

while running:
    clear_canvas()
    cursor.draw(x,y)

    update_canvas()

    handle_events()

close_canvas()