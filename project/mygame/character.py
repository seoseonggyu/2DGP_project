import pico2d
import game_framework
import time
import title_state
import logo_state


class character:
    def __init__(self):
        self.x, self.y = 600, 400 # 캐릭터 좌표
        self.mouse_x, self.mouse_y = 600, 400 # 마우스 좌표
        self.frame = 0
        self.way = 0
        self.dir = 0
        self.dir2 = 0
        self.image = pico2d.load_image('character_sheet.png')
        self.cursor = pico2d.load_image('gun_cursor.png')

    def update(self):
        self.frame = (self.frame + 1) % 6
        self.x += self.dir * 5
        self.y += self.dir2 * 5
        pico2d.delay(0.01)

    def update2(self):
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 40, 42 * self.way, 40, 42, self.x, self.y, 120, 120)
        self.cursor.draw(self.mouse_x, self.mouse_y)

class bullet:
    def __init__(self, mousex, mousey, posx, posy):
        self.bullet_x, self.bullet_y = mousex, mousey
        self.shot = pico2d.load_image('bullet.png')
        self.speed = 0
        self.hero_x, self.hero_y = posx, posy  # 캐릭터 위치

        self.x, self.y = 0, 0

    def update(self):
        self.speed += 0.002
        self.x = (1 - self.speed) * self.hero_x + self.speed * self.bullet_x
        self.y = (1 - self.speed) * self.hero_y + self.speed * self.bullet_y


    def draw(self):
        self.shot.clip_draw(0, 0, 40, 42, self.x, self.y)

dir = 0
dir2 = 0
way = 0
frame = 0
move = True

bulletXY = []
mouse_x, mouse_y = 600, 400 # 마우스

def handle_events():
    global dir
    global dir2
    global way
    global frame
    global move
    global mouse_x, mouse_y
    global bulletXY

    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_QUIT:
            game_framework.quit()
        if event.type == pico2d.SDL_MOUSEMOTION: # 마우스
            mouse_x, mouse_y = event.x, 800 - 1 - event.y

        if event.type == pico2d.SDL_MOUSEBUTTONDOWN:
            if event.button == pico2d.SDL_BUTTON_LEFT:
                mouse_x, mouse_y = event.x, 800 - 1 - event.y
                bulletXY.append(bullet(mouse_x, mouse_y, hero.x, hero.y))

        if event.type == pico2d.SDL_KEYDOWN: # 캐릭터 이동
            move = True
            if event.key == pico2d.SDLK_ESCAPE:
                game_framework.quit()
            if event.key == pico2d.SDLK_d:
                dir += 1
                way = 0
            if event.key == pico2d.SDLK_a:
                dir -= 1
                way = 1
            if event.key == pico2d.SDLK_w:
                dir2 += 1
                way = 4
            if event.key == pico2d.SDLK_s:
                dir2 -= 1
                way = 5

            if dir > 0 and dir2 > 0:
                way = 2
            if dir < 0 and dir2 > 0:
                way = 3
            if dir < 0 and dir2 < 0:
                way = 1
            if dir > 0 and dir2 < 0:
                way = 0

        if event.type == pico2d.SDL_KEYUP:
            if event.key == pico2d.SDLK_d:
                if dir2 > 0:
                    dir -= 1
                    way = 4
                elif dir2 < 0:
                    way = 5
                    dir -= 1
                else:
                    way = 6
                    frame = 0
                    dir -= 1
                    move = False
            elif event.key == pico2d.SDLK_w:
                if dir > 0:
                    dir2 -= 1
                    way = 0
                elif dir < 0:
                    dir2 -= 1
                    way = 1
                else:
                    way = 6
                    frame = 2
                    dir2 -= 1
                    move = False
            elif event.key == pico2d.SDLK_a:
                if dir2 > 0:
                    dir += 1
                    way = 4
                elif dir2 < 0:
                    way = 5
                    dir += 1
                else:
                    way = 6
                    frame = 3
                    dir += 1
                    move = False
            elif event.key == pico2d.SDLK_s:
                if dir > 0:
                    dir2 += 1
                    way = 0
                elif dir < 0:
                    dir2 += 1
                    way = 1
                else:
                    way = 6
                    frame = 1
                    dir2 += 1
                    move = False


hero = None

# 초기화
def enter():
    global hero
    hero = character()

# 종료
def exit():
    global hero
    del hero

# 월드에 존재하는 객체들을 업데이트
def update():
    global dir
    global dir2
    global way
    global move
    global frame
    global bulletXY
    global mouse_x, mouse_x


    pico2d.hide_cursor()
    hero.dir = dir
    hero.dir2 = dir2
    hero.way = way
    hero.mouse_x = mouse_x
    hero.mouse_y = mouse_y

    # bullet.hero_x, bullet.hero_y = hero.x, hero.y
    if move == True:
        hero.update()

    elif move == False:
        hero.frame = frame
        hero.update2()

    for bullets in bulletXY[:]:
        bullets.update()



# 월드를 그린다
def draw():
    global bulletXY
    pico2d.clear_canvas()
    hero.draw()
    for bullets in bulletXY[:]:
        bullets.draw()
    pico2d.update_canvas()