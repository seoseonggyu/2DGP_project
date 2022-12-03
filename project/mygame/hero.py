import math

from pico2d import *
import game_framework
import play_state
from bullet import Bullet
import server
import time
import game_world
from server import map_w, map_h


image_center_w = map_w / 2
image_center_h = map_h / 2

character_image_size = 200
gun_image_size = 50

# Run Speed
PIXEL_PER_METER = (10.0 / 0.01) # 10 pixel 30 cm
RUN_SPEED_KMPH = 3 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Action Speed
TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6



#2 이벤트 정의
AT,DD, AD, WD, SD, DU, AU, WU, SU, QD, JP = range(11)


key_event_table = {
    (SDL_KEYDOWN, SDLK_d): DD,
    (SDL_KEYDOWN, SDLK_a): AD,
    (SDL_KEYDOWN, SDLK_w): WD,
    (SDL_KEYDOWN, SDLK_s): SD,
    (SDL_KEYDOWN, SDLK_q): QD,
    (SDL_KEYUP,   SDLK_d): DU,
    (SDL_KEYUP,   SDLK_a): AU,
    (SDL_KEYUP,   SDLK_w): WU,
    (SDL_KEYUP,   SDLK_s): SU,
    (SDL_MOUSEBUTTONDOWN,   SDL_BUTTON_LEFT): AT,
    (SDL_MOUSEBUTTONDOWN,   SDL_BUTTON_RIGHT): JP
}

class WEAPON_IDLE:
    def enter(self, event):  # 상태에 들어갈 때 행하는 액션
        print('enter idle')
        self.dir = 0
        self.dir2 = 0
        self.way = 0

    def exit(self, event):  # 상태를 나올 때 행하는 액션 , 고개 들기
        if event == AT:
            if self.attack_count != 5:
                self.fire_shot()
                self.attack_count += 1


    def do(self):  # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.mouse_angle = math.pi - math.atan2(self.mouse_x - image_center_w, self.mouse_y - image_center_h)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6

        if (math.degrees(self.mouse_angle)) >= math.degrees(1 / 6 * math.pi) and (
                math.degrees(self.mouse_angle) <= math.degrees(2 / 3 * math.pi)):
            self.way = 0
        elif (math.degrees(self.mouse_angle)) > math.degrees(2 / 3 * math.pi) and math.degrees(
                self.mouse_angle) <= math.degrees(5 / 6 * math.pi):
            self.way = 2
        elif (math.degrees(self.mouse_angle)) > math.degrees(5 / 6 * math.pi) and math.degrees(
                self.mouse_angle) <= math.degrees(7 / 6 * math.pi):
            self.way = 4
        elif (math.degrees(self.mouse_angle)) > math.degrees(7 / 6 * math.pi) and math.degrees(
                self.mouse_angle) <= math.degrees(4 / 3 * math.pi):
            self.way = 3
        elif (math.degrees(self.mouse_angle)) > math.degrees(4 / 3 * math.pi) and math.degrees(
                self.mouse_angle) <= math.degrees(2 * math.pi - 1 / 6 * math.pi):
            self.way = 1
        elif (math.degrees(self.mouse_angle)) > math.degrees(2 * math.pi - 1 / 6 * math.pi) and math.degrees(
                self.mouse_angle) <= math.degrees(2 * math.pi):
            self.way = 5
        elif (math.degrees(self.mouse_angle)) > math.degrees(0) and math.degrees(self.mouse_angle) <= math.degrees(
                1 / 6 * math.pi):
            self.way = 5

        if self.attack_count == 5:
            self.Reload()



    def draw(self):
        self.mouse_angle = math.pi - math.atan2(self.mouse_x - map_w / 2, self.mouse_y - map_h / 2)

        if (math.degrees(self.mouse_angle)) >= math.degrees(1/6 * math.pi) and (math.degrees(self.mouse_angle) <= math.degrees(2/3 * math.pi)):
            self.weapon1.clip_composite_draw(0, 0, 27, 22, self.mouse_angle - 3.141592 / 2, '', self.x + 50, self.y, 100, 100)

        elif (math.degrees(self.mouse_angle)) > math.degrees(2/3 * math.pi) and math.degrees(self.mouse_angle) <= math.degrees(5/6 * math.pi):
            self.weapon1.clip_composite_draw(0, 0, 27, 22, self.mouse_angle - 3.141592 / 2, '', self.x + 50, self.y + 20, 100, 100)

        elif (math.degrees(self.mouse_angle)) > math.degrees(5/6 * math.pi) and math.degrees(self.mouse_angle) <= math.degrees(7/6 * math.pi):
            self.weapon1.clip_composite_draw(0, 0, 27, 22, self.mouse_angle - 3.141592 / 2, '', self.x + 20, self.y + 20, 100, 100)

        elif (math.degrees(self.mouse_angle)) > math.degrees(7/6 * math.pi) and math.degrees(self.mouse_angle) <= math.degrees(4/3 * math.pi):
            self.weapon1.clip_composite_draw(0, 0, 27, 22, self.mouse_angle + 3.141592 / 2, 'h', self.x - 50, self.y + 20, 100, 100)

        elif (math.degrees(self.mouse_angle)) > math.degrees(4 / 3 * math.pi) and math.degrees(self.mouse_angle) <= math.degrees(2 * math.pi - 1 / 6 * math.pi):
            self.weapon1.clip_composite_draw(0, 0, 27, 22, self.mouse_angle + 3.141592 / 2, 'h', self.x - 50, self.y, 100, 100)

        elif (math.degrees(self.mouse_angle)) > math.degrees(2 * math.pi - 1 / 6 * math.pi) and math.degrees(self.mouse_angle) <= math.degrees(2 * math.pi):
            self.weapon1.clip_composite_draw(0, 0, 27, 22, self.mouse_angle + 3.141592 / 2, 'h', self.x - 20, self.y - 20, 100, 100)

        elif (math.degrees(self.mouse_angle)) > math.degrees(0) and math.degrees(self.mouse_angle) <= math.degrees(1 / 6 * math.pi):
            self.weapon1.clip_composite_draw(0, 0, 27, 22, self.mouse_angle - 3.141592 / 2, '', self.x + 20, self.y - 20, 100, 100)


        self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, character_image_size, character_image_size)
        self.cursor.clip_draw(0, 0, 22, 22, self.mouse_x, self.mouse_y, gun_image_size, gun_image_size)


class WEAPON_RUN:
    def enter(self, event):  # 상태에 들어갈 때 행하는 액션
        if event == DD:
            self.dir += 1
        elif event == DU:
            self.dir -= 1
        if event == AD:
            self.dir -= 1
        elif event == AU:
            self.dir += 1

        if event == WD:
            self.dir2 += 1
        elif event == WU:
            self.dir2 -= 1
        if event == SD:
            self.dir2 -= 1
        elif event == SU:
            self.dir2 += 1

    def exit(self, event):  # 상태를 나올 때 행하는 액션 , 고개 들기
        if event == AT:
            if self.attack_count != 5:
                self.fire_shot()
                self.attack_count += 1

    def do(self):  # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기\
        self.mouse_angle = math.pi - math.atan2(self.mouse_x - image_center_w, self.mouse_y - image_center_h)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6

        if (math.degrees(self.mouse_angle)) >= math.degrees(1 / 6 * math.pi) and (
                math.degrees(self.mouse_angle) <= math.degrees(2 / 3 * math.pi)):
            self.way = 0
        elif (math.degrees(self.mouse_angle)) > math.degrees(2 / 3 * math.pi) and math.degrees(
                self.mouse_angle) <= math.degrees(5 / 6 * math.pi):
            self.way = 2
        elif (math.degrees(self.mouse_angle)) > math.degrees(5 / 6 * math.pi) and math.degrees(
                self.mouse_angle) <= math.degrees(7 / 6 * math.pi):
            self.way = 4
        elif (math.degrees(self.mouse_angle)) > math.degrees(7 / 6 * math.pi) and math.degrees(
                self.mouse_angle) <= math.degrees(4 / 3 * math.pi):
            self.way = 3
        elif (math.degrees(self.mouse_angle)) > math.degrees(4 / 3 * math.pi) and math.degrees(
                self.mouse_angle) <= math.degrees(2 * math.pi - 1 / 6 * math.pi):
            self.way = 1
        elif (math.degrees(self.mouse_angle)) > math.degrees(2 * math.pi - 1 / 6 * math.pi) and math.degrees(
                self.mouse_angle) <= math.degrees(2 * math.pi):
            self.way = 5
        elif (math.degrees(self.mouse_angle)) > math.degrees(0) and math.degrees(self.mouse_angle) <= math.degrees(
                1 / 6 * math.pi):
            self.way = 5

        if self.attack_count == 5:
            self.Reload()

    def draw(self):

        if (math.degrees(self.mouse_angle)) >= math.degrees(1 / 6 * math.pi) and (
                math.degrees(self.mouse_angle) <= math.degrees(2 / 3 * math.pi)):
            self.weapon1.clip_composite_draw(0, 0, 27, 22, self.mouse_angle - 3.141592 / 2, '', self.x + 50, self.y,
                                             100, 100)

        elif (math.degrees(self.mouse_angle)) > math.degrees(2 / 3 * math.pi) and math.degrees(
                self.mouse_angle) <= math.degrees(5 / 6 * math.pi):
            self.weapon1.clip_composite_draw(0, 0, 27, 22, self.mouse_angle - 3.141592 / 2, '', self.x + 50,
                                             self.y + 20, 100, 100)

        elif (math.degrees(self.mouse_angle)) > math.degrees(5 / 6 * math.pi) and math.degrees(
                self.mouse_angle) <= math.degrees(7 / 6 * math.pi):
            self.weapon1.clip_composite_draw(0, 0, 27, 22, self.mouse_angle - 3.141592 / 2, '', self.x + 20,
                                             self.y + 20, 100, 100)

        elif (math.degrees(self.mouse_angle)) > math.degrees(7 / 6 * math.pi) and math.degrees(
                self.mouse_angle) <= math.degrees(4 / 3 * math.pi):
            self.weapon1.clip_composite_draw(0, 0, 27, 22, self.mouse_angle + 3.141592 / 2, 'h', self.x - 50,
                                             self.y + 20, 100, 100)

        elif (math.degrees(self.mouse_angle)) > math.degrees(4 / 3 * math.pi) and math.degrees(
                self.mouse_angle) <= math.degrees(2 * math.pi - 1 / 6 * math.pi):
            self.weapon1.clip_composite_draw(0, 0, 27, 22, self.mouse_angle + 3.141592 / 2, 'h', self.x - 50, self.y,
                                             100, 100)

        elif (math.degrees(self.mouse_angle)) > math.degrees(2 * math.pi - 1 / 6 * math.pi) and math.degrees(
                self.mouse_angle) <= math.degrees(2 * math.pi):
            self.weapon1.clip_composite_draw(0, 0, 27, 22, self.mouse_angle + 3.141592 / 2, 'h', self.x - 20,
                                             self.y - 20, 100, 100)

        elif (math.degrees(self.mouse_angle)) > math.degrees(0) and math.degrees(self.mouse_angle) <= math.degrees(
                1 / 6 * math.pi):
            self.weapon1.clip_composite_draw(0, 0, 27, 22, self.mouse_angle - 3.141592 / 2, '', self.x + 20,
                                             self.y - 20, 100, 100)


        self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, character_image_size,
                             character_image_size)

        self.cursor.clip_draw(0, 0, 22, 22, self.mouse_x, self.mouse_y, gun_image_size, gun_image_size)
        self.item.draw(45, 1200 - 120, character_image_size - 100, character_image_size - 100)
        self.font.draw(50, 1200 - 120, '%7d' % self.item_count, (255, 255, 255))


# 42 , 41
# class JUMP:
#     def enter(self, event): # 상태에 들어갈 때 행하는 액션
#         print('enter jump')
#
#         if self.dir > 0:
#             self.way = 0
#             pass
#
#     def exit(self, event):
#         print('jump exit')
#         print('-------')
#         self.finish_jump = False
#         self.using_jump = True
#
#     def do(self):
#         if self.finish_jump == False:
#             self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10
#         elif self.finish_jump == True:
#             self.frame = 0
#
#         if self.frame >= 9:
#             self.finish_jump = True
#             self.using_jump = False
#             self.dir -= 1
#
#     def draw(self):
#         self.cursor.clip_draw(0, 0, 22, 22, self.mouse_x, self.mouse_y, gun_image_size, gun_image_size)
#
#         if self.finish_jump == False:
#             self.jump.clip_draw(int(self.frame) * 42, 41 * self.way, 42, 41, self.x, self.y - 41, character_image_size, character_image_size)
#         elif self.finish_jump == True:
#             self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, character_image_size, character_image_size)

next_stage = {
    # WEAPON_IDLE: {DD: WEAPON_RUN,  AD: WEAPON_RUN,  WD: WEAPON_RUN,  SD: WEAPON_RUN,  DU: WEAPON_IDLE, AU: WEAPON_IDLE,
    #               WU: WEAPON_IDLE, SU: WEAPON_IDLE, AT: WEAPON_IDLE},
    WEAPON_RUN:  {DD: WEAPON_RUN, AD: WEAPON_RUN, WD: WEAPON_RUN, SD: WEAPON_RUN, DU: WEAPON_RUN, AU: WEAPON_RUN,
                  WU: WEAPON_RUN, SU: WEAPON_RUN, AT: WEAPON_RUN},
}

class character:
    def __init__(self):
        self.font = load_font('ENCR10B.TTF', 16)
        self.mouse_angle = 0
        self.x, self.y = image_center_w, image_center_h # 캐릭터 좌표

        self.mouse_x, self.mouse_y = 0, 0 # 마우스 좌표
        self.frame = 0
        self.way = 0
        self.attack_count = 0
        self.timer = 50
        self.dir, self.dir2 = 0, 0
        self.face_dir = 0

        self.font = load_font('ENCR10B.TTF', 16)
        self.font2 = load_font('ENCR10B.TTF', 16)
        self.item_count = 0

        self.finish_jump = False
        self.using_jump = False
        self.font = load_font('ENCR10B.TTF', 16)

        self.image = load_image('character_sheet.png')
        self.cursor = load_image('gun_cursor.png')
        self.jump = load_image('jump_sheet.png')
        self.weapon1 = load_image('weapon1.png')
        self.item = load_image('item.png')

        self.q = []  # 이벤트 큐 초기화
        self.cur_state = WEAPON_RUN
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.q:
            event = self.q.pop()
            self.cur_state.exit(self, event) # 현재 상태를 나가야되고,
            self.cur_state = next_stage[self.cur_state][event] # 다음 상태를 구한다
            self.cur_state.enter(self, event)

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        if (event.type, event.button) in key_event_table:
            key_event = key_event_table[(event.type, event.button)]
            self.add_event(key_event)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

        self.font.draw(self.x - 40, self.y + 80, 'counter: %d' % (self.attack_count), (255, 255, 0))
        self.font2.draw(self.x - 40, self.y + 120, '%d' % self.x, (255, 255, 255))


    def fire_shot(self):
        shots = Bullet(self.mouse_x, self.mouse_y, self.x, self.y, 2 * RUN_SPEED_PPS)
        game_world.add_object(shots, 1)
        game_world.add_collision_pairs(shots, None, 'shots:enemy1')

    def Reload(self):
        self.timer -= 1
        if self.timer == 0:
            self.attack_count = 0
            self.timer = 50

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 35


    def handle_collision(self, other, group):
        pass


