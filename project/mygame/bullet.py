import pico2d


class bullet:
    def __int__(self, mousex, mousey):
        # self.bullet_x, self.bullet_y = xpos, ypos
        self.bullet_x = mousex
        self.bullet_y = mousey
        self.shot = pico2d.load_image('bullet.png')
        self.speed = 2

    def update(self):
        pass
    def draw(self):
        self.shot.draw(self.bullet_x, self.bullet_y)


move = True
bulletXY = []
mouse_x, mouse_y = 600, 400 # 마우스

def handle_events():

    global move
    global mouse_x, mouse_y
    # global hero
    global bulletXY

    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_MOUSEMOTION: # 마우스
            mouse_x, mouse_y = event.x, 800 - 1 - event.y

        if event.type == pico2d.SDL_MOUSEBUTTONDOWN:
            if event.button == pico2d.SDL_BUTTON_LEFT:
                bulletXY.append(bullet(mouse_x, mouse_y))



# 초기화

# 종료


# 월드에 존재하는 객체들을 업데이트
def update():

    global bulletXY

    pico2d.hide_cursor()

    # bullet.hero_x, bullet.hero_y = hero.x, hero.y

    for bullets in bulletXY[:]:
        bullets.update()


# 월드를 그린다
def draw():
    pico2d.clear_canvas()
    for bullets in bulletXY[:]:
        bullets.draw()
    pico2d.update_canvas()

pico2d.open_canvas(1200, 800)
while True:

    pico2d.clear_canvas()
    for bullets in bulletXY[:]:
        bullets.draw()
    pico2d.update_canvas()
    handle_events()

pico2d.close_canvas()