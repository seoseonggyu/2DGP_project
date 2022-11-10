from pico2d import *
import game_framework
import game_world

from hero import character
from grass import Grass

import title_state
import logo_state

hero = None
grass =None

# class bullet:
#     def __init__(self, mousex, mousey, posx, posy):
#         self.bullet_x, self.bullet_y = mousex, mousey
#         self.shot = pico2d.load_image('bullet.png')
#         self.speed = 0
#         self.hero_x, self.hero_y = posx, posy  # 캐릭터 위치
#
#         self.x, self.y = 0, 0
#
#     def update(self):
#         self.speed += 0.002
#         self.x = (1 - self.speed) * self.hero_x + self.speed * self.bullet_x
#         self.y = (1 - self.speed) * self.hero_y + self.speed * self.bullet_y
#
#
#     def draw(self):
#         self.shot.clip_draw(0, 0, 40, 42, self.x, self.y)

# class Life:
#     def __init__(self, posx, posy):
#         self.life = pico2d.load_image('life.png')
#         self.x = posx
#         self.y = posy
#
#     def update(self):
#         pass
#
#     def draw(self):
#         self.life.draw(self.x, self.y, 50, 50)

# class Stage1:
#     def __init__(self):
#         self.stage1_image = pico2d.load_image('stage1.png')
#     def draw(self):
#         self.stage1_image.draw(600, 400, 1200, 800)



# 캐릭터 관련
dir = 0
dir2 = 0
way = 0
frame = 0
move = True
mouse_x, mouse_y = 600, 400 # 마우스

# 총알 관련
bulletXY = []

# 생명 관련
life = []



def handle_events():

    # global mouse_x, mouse_y
    # global bulletXY

    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_QUIT:
            game_framework.quit()
        if (event.type, event.key) == (pico2d.SDL_KEYDOWN, pico2d.SDLK_ESCAPE):
            game_framework.quit()
        else:
            hero.handle_event(event)


# stage1 = None
# life = None

# 초기화
def enter():
    global hero, grass #stage1, life
    hero = character()
    grass = Grass()
    game_world.add_object(grass, 0)
    game_world.add_object(hero, 1)

    #life = [Life(50, 750), Life(100, 750), Life(150, 750)]
    #stage1 = Stage1()

# 종료
def exit():
    game_world.clear()

# 월드에 존재하는 객체들을 업데이트
def update():
    for game_object in game_world.all_objects():
        game_object.update()
    # global bulletXY
    # global mouse_x, mouse_x


    # pico2d.hide_cursor()
    # hero.dir = dir
    # hero.dir2 = dir2
    # hero.way = way
    # hero.mouse_x = mouse_x
    # hero.mouse_y = mouse_y

    # if move == True:

    # elif move == False:
    #     hero.frame = frame
    #     hero.update2()
    #
    # for bullets in bulletXY[:]:
    #     bullets.update()
    #
    # if len(bulletXY) != 0:
    #     for i, bxy in enumerate(bulletXY):
    #         if bxy.x <= 50 or bxy.x >= 1150 or bxy.y <= 50 or bxy.y >= 750:
    #             bulletXY.remove(bxy)


def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()


# 월드를 그린다


def draw():
    clear_canvas()
    draw_world()
    update_canvas()

    # global bulletXY
    # stage1.draw() # 스테이지1


    # 생명 카운트
    # for i in life:
    #     i.draw()

    # 총알
    # for bullets in bulletXY[:]:
    #     bullets.draw()
    # pico2d.update_canvas()

def pause():
    pass

def resume():
    pass