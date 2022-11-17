from pico2d import *
import game_framework
import play_state
from bullet import Bullet
import server
import game_world
from enemy import Enemy1
import pygame

m_w = 1200
m_h = 1200



# Run Speed
PIXEL_PER_METER = (10.0 / 0.01) # 10 pixel 30 cm
RUN_SPEED_KMPH = 0.5 # Km / Hour
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
            self.fire_shot()

    def do(self):  # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6

        self.mouse_angle = math.pi - math.atan2(self.mouse_x - 600, self.mouse_y - 300)

        # print('mouse_angle: ',self.mouse_angle)

        if (self.mouse_angle <= 1.8) and (self.mouse_angle > 0.25):
            self.way = 0
        elif (self.mouse_angle <= 2.9) and (self.mouse_angle > 1.8):
            self.way = 2
        elif (self.mouse_angle <= 3.4) and (self.mouse_angle > 2.9):
            self.way = 4
        elif (self.mouse_angle <= 4.45) and (self.mouse_angle > 3.4):
            self.way = 3
        elif (self.mouse_angle <= 6.1) and (self.mouse_angle > 4.45):
            self.way = 1
        elif (self.mouse_angle <= 0.25) and (self.mouse_angle > 0):
            self.way = 5
        elif (self.mouse_angle <= 6.3) and (self.mouse_angle > 6.1):
            self.way = 5

        self.frame = self.face_dir
        self.mouse_angle = math.pi - math.atan2(self.mouse_x - 600, self.mouse_y - 300)


    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, 120, 120)

        self.weapon1.clip_composite_draw(0, 0, 27, 22,
                                       self.mouse_angle - 3.141592 / 2, '', self.x + 22, self.y - 5, 40, 40)

        self.cursor.draw(self.mouse_x, self.mouse_y)

class WEAPON_RUN:
    def enter(self, event):  # 상태에 들어갈 때 행하는 액션
        if event == DD:
            self.dir += 1

        elif event == AD:
            self.dir -= 1

        elif event == WD:
            self.dir2 += 1

        elif event == SD:
            self.dir2 -= 1

        if event == DU:
            if self.dir2 > 0:
                self.dir -= 1
            elif self.dir2 < 0:
                self.dir -= 1
            elif self.dir < 0:
                self.dir = -1

        elif event == AU:
            if self.dir2 > 0:
                self.dir += 1
            elif self.dir2 < 0:
                self.dir += 1
            elif self.dir > 0:
                self.dir = 1

        elif event == WU:
            if self.dir > 0:
                self.dir2 -= 1
            elif self.dir < 0:
                self.dir2 -= 1
            elif self.dir2 < 0:
                self.dir2 = -1

        elif event == SU:
            if self.dir > 0:
                self.dir2 += 1
            elif self.dir < 0:
                self.dir2 += 1
            elif self.dir2 > 0:
                self.dir2 = 1

    def exit(self, event):  # 상태를 나올 때 행하는 액션 , 고개 들기
        if event == AT:
            self.fire_shot()

    def do(self):  # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.mouse_angle = math.pi - math.atan2(self.mouse_x - 600, self.mouse_y - 300)

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.dir2 * RUN_SPEED_PPS * game_framework.frame_time

        self.x = pico2d.clamp(0, self.x, 1200)
        self.y = pico2d.clamp(0, self.y, 600)

        if (self.mouse_angle <= 1.8) and (self.mouse_angle > 0.25):
            self.way = 0
        elif (self.mouse_angle <= 2.9) and (self.mouse_angle > 1.8):
            self.way = 2
        elif (self.mouse_angle <= 3.4) and (self.mouse_angle > 2.9):
            self.way = 4
        elif (self.mouse_angle <= 4.45) and (self.mouse_angle > 3.4):
            self.way = 3
        elif (self.mouse_angle <= 6.1) and (self.mouse_angle > 4.45):
            self.way = 1
        elif (self.mouse_angle <= 0.25) and (self.mouse_angle > 0):
            self.way = 5
        elif (self.mouse_angle <= 6.3) and (self.mouse_angle > 6.1):
            self.way = 5

    def draw(self):
        self.cursor.draw(self.mouse_x, self.mouse_y)

        self.weapon1.clip_composite_draw(0, 0, 27, 22,
                                         self.mouse_angle - 3.141592 / 2, '', self.x + 28, self.y - 4, 42, 42)

        self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, 120, 120)

class WEAPON_RUN2:
    @staticmethod
    def enter(self, event):
        if event == DD:
            if self.dir2 > 0:
                self.dir += 1
            elif self.dir2 < 0:
                self.dir += 1
            else:
                self.dir = 1

        elif event == AD:
            if self.dir2 > 0:
                self.dir -= 1
            elif self.dir2 < 0:
                self.dir -= 1
            else:
                self.dir = -1

        elif event == WD:
            if self.dir > 0:
                self.dir2 += 1
            elif self.dir < 0:
                self.dir2 += 1
            else:
                self.dir2 = 1

        elif event == SD:
            if self.dir > 0:
                self.dir2 -= 1
            elif self.dir < 0:
                self.dir2 -= 1
            else:
                self.dir2 = -1

    @staticmethod
    def exit(self, event):
        if event == AT:
            self.fire_shot()

    @staticmethod
    def do(self):  # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기

        if (self.mouse_angle <= 1.8) and (self.mouse_angle > 0.25):
            self.way = 0
        elif (self.mouse_angle <= 2.9) and (self.mouse_angle > 1.8):
            self.way = 2
        elif (self.mouse_angle <= 3.4) and (self.mouse_angle > 2.9):
            self.way = 4
        elif (self.mouse_angle <= 4.45) and (self.mouse_angle > 3.4):
            self.way = 3
        elif (self.mouse_angle <= 6.1) and (self.mouse_angle > 4.45):
            self.way = 1
        elif (self.mouse_angle <= 0.25) and (self.mouse_angle > 0):
            self.way = 5
        elif (self.mouse_angle <= 6.3) and (self.mouse_angle > 6.1):
            self.way = 5

        self.mouse_angle = math.pi - math.atan2(self.mouse_x - 600, self.mouse_y - 300)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.dir2 * RUN_SPEED_PPS * game_framework.frame_time

        self.x = pico2d.clamp(0, self.x, 1200)
        self.y = pico2d.clamp(0, self.y, 600)

    @staticmethod
    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, 120, 120)
        self.cursor.draw(self.mouse_x, self.mouse_y)
        self.weapon1.clip_composite_draw(0, 0, 27, 22,
                                         self.mouse_angle - 3.141592 / 2, '', self.x + 28, self.y - 4, 42, 42)

class IDLE:
    def enter(self, event): # 상태에 들어갈 때 행하는 액션
        print('Enter Idle')
        self.dir = 0
        self.dir2 = 0

    def exit(self, event):
        print('eixt Idle')
        print('-------')

    def do(self):
            self.frame = self.face_dir
            self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
            self.y += self.dir2 * RUN_SPEED_PPS * game_framework.frame_time

    # 외부에서 전달되는 self
    def draw(self):
        self.cursor.draw(self.mouse_x, self.mouse_y)
        self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, 120, 120)

class RUN:
    @staticmethod
    def enter(self, event):
        print('Enter run')
        if event == DD:
            self.way = 0
            self.dir += 1

        elif event == AD:
            self.way = 1
            self.dir -= 1

        elif event == WD:
            self.way = 4
            self.dir2 += 1

        elif event == SD:
            self.way = 5
            self.dir2 -= 1

        if event == DU:
            if self.dir2 > 0:
                self.way = 4
                self.dir -= 1
            elif self.dir2 < 0:
                self.way = 5
                self.dir -= 1
            elif self.dir < 0:
                self.way = 1
                self.dir = -1

        elif event == AU:
            if self.dir2 > 0:
                self.way = 4
                self.dir += 1
            elif self.dir2 < 0:
                self.way = 5
                self.dir += 1
            elif self.dir > 0:
                self.way = 0
                self.dir = 1

        elif event == WU:
            if self.dir > 0:
                self.way = 0
                self.dir2 -= 1
            elif self.dir < 0:
                self.way = 1
                self.dir2 -= 1
            elif self.dir2 < 0:
                self.way = 5
                self.dir2 = -1

        elif event == SU:
            if self.dir > 0:
                self.way = 0
                self.dir2 += 1
            elif self.dir < 0:
                self.way = 1
                self.dir2 += 1
            elif self.dir2 > 0:
                self.way = 4
                self.dir2 = 1

    @staticmethod
    def exit(self, event):
        print('exit run')
        print('-------')
        self.face_dir = self.way

    @staticmethod
    def do(self): # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        # self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        # self.y += self.dir2 * RUN_SPEED_PPS * game_framework.frame_time


        self.x = pico2d.clamp(0, self.x, 1200)
        self.y = pico2d.clamp(0, self.y, 600)

    @staticmethod
    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, 120, 120)
        self.cursor.draw(self.mouse_x, self.mouse_y)

class RUN2:
    @staticmethod
    def enter(self, event):
        print('Enter RUN2')
        if event == DD:
            if self.dir2 > 0:
                self.way = 2
                self.dir += 1
            elif self.dir2 < 0:
                self.way = 0
                self.dir += 1
            else:
                self.dir = 1
                self.way = 0

        elif event == AD:
            if self.dir2 > 0:
                self.way = 3
                self.dir -= 1
            elif self.dir2 < 0:
                self.way = 1
                self.dir -= 1
            else:
                self.dir = -1
                self.way = 1

        elif event == WD:
            if self.dir > 0:
                self.way = 2
                self.dir2 += 1
            elif self.dir < 0:
                self.way = 3
                self.dir2 += 1
            else:
                self.dir2 = 1
                self.way = 4

        elif event == SD:
            if self.dir > 0:
                self.way = 0
                self.dir2 -= 1
            elif self.dir < 0:
                self.way = 1
                self.dir2 -= 1
            else:
                self.dir2 = -1
                self.way = 5

    @staticmethod
    def exit(self, event):
        print('exit RUN2')
        print('-------')

    @staticmethod
    def do(self): # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        # self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        # self.y += self.dir2 * RUN_SPEED_PPS * game_framework.frame_time

        self.x = pico2d.clamp(0, self.x, 1200)
        self.y = pico2d.clamp(0, self.y, 600)

    @staticmethod
    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, 120, 120)
        self.cursor.draw(self.mouse_x, self.mouse_y)

# class JUMP:
#     def enter(self, event): # 상태에 들어갈 때 행하는 액션
#         print('enter jump')
#         self.jump_check = False
#         if self.dir > 0 and self.dir2 < 0:
#             self.way = 0
#         elif self.dir < 0 and self.dir2 < 0:
#             self.way = 1
#         elif self.dir < 0:
#             self.way = 1
#         elif self.dir > 0 and self.dir2 > 0:
#             self.way = 2
#         elif self.dir < 0 and self.dir2 > 0:
#             self.way = 3
#         elif self.dir2 < 0:
#             self.way = 4
#         elif self.dir2 > 0:
#             self.way = 5
#
#     def exit(self, event):
#         print('jump exit')
#         print('-------')
#
#     def do(self):
#         self.x = pico2d.clamp(0, self.x, 1000)
#         self.y = pico2d.clamp(0, self.y, 600)
#         #print('frame: ', self.frame)
#         if int(self.frame) >= 8.0:
#             self.jump_check = True
#             if self.dir > 0:
#                 self.dir -= 1
#             if self.dir < 0:
#                 self.dir += 1
#             if self.dir2 > 0:
#                 self.dir2 -= 1
#             if self.dir2 < 0:
#                 self.dir2 += 1
#             print('jump frmae:', self.frame)
#
#
#         if self.jump_check == False:
#             self.frame = (self.frame + JUMP_FRAMES_PER_ACTION * JUMP_ACTION_PER_TIME * game_framework.frame_time) % 9
#             self.x += self.dir * JUMP_RUN_SPEED_PPS * game_framework.frame_time
#             self.y += self.dir2 * JUMP_RUN_SPEED_PPS * game_framework.frame_time
#
#
#         if self.jump_check == True:
#             self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
#
#     def draw(self):
#         self.cursor.draw(self.mouse_x, self.mouse_y)
#
#         if self.jump_check == False:
#             self.jump.clip_draw(int(self.frame) * 42, 62 * self.way, 42, 62, self.x, self.y, 120, 200)
#
#         elif self.jump_check == True:
#             self.image.clip_draw(int(self.frame), 42 * self.way, 40, 42, self.x, self.y, 120, 120)


next_stage = {
    IDLE:   {DD: RUN,    AD: RUN,    WD: RUN,    SD: RUN,    DU: IDLE, AU: IDLE, WU: IDLE, SU: IDLE, QD: WEAPON_IDLE,
             AT: IDLE, JP: IDLE},
    RUN:    {DD: RUN2,   AD: RUN2,   WD: RUN2,   SD: RUN2,   DU: IDLE, AU: IDLE, WU: IDLE, SU: IDLE, QD: WEAPON_IDLE,
             AT: RUN,  JP: RUN},
    RUN2:   {DD: RUN2,   AD: RUN2,   WD: RUN2,   SD: RUN2,   DU: RUN,  AU: RUN,  WU: RUN,  SU: RUN,  QD: WEAPON_IDLE,
             AT: RUN2, JP: RUN2},
    WEAPON_IDLE: {DD: WEAPON_RUN,  AD: WEAPON_RUN,  WD: WEAPON_RUN,  SD: WEAPON_RUN,  DU: WEAPON_IDLE, AU: WEAPON_IDLE,
                  WU: WEAPON_IDLE, SU: WEAPON_IDLE, AT: WEAPON_IDLE, QD: IDLE, JP: WEAPON_IDLE},
    WEAPON_RUN:  {DD: WEAPON_RUN2, AD: WEAPON_RUN2, WD: WEAPON_RUN2, SD: WEAPON_RUN2, DU: WEAPON_IDLE, AU: WEAPON_IDLE,
                  WU: WEAPON_IDLE, SU: WEAPON_IDLE, AT: WEAPON_RUN,  JP: WEAPON_RUN},
    WEAPON_RUN2: {DD: WEAPON_IDLE, AD: WEAPON_IDLE, WD: WEAPON_IDLE, SD: WEAPON_RUN2, DU: WEAPON_RUN,  AU: WEAPON_RUN,
                  WU: WEAPON_RUN,  SU: WEAPON_RUN,  AT: WEAPON_RUN2, JP: WEAPON_RUN2}
}

class character:
    def __init__(self):

        self.mouse_angle = 0
        self.x, self.y = 600, 300 # 캐릭터 좌표
        self.mouse_x, self.mouse_y = 0, 0 # 마우스 좌표
        self.frame = 0
        self.way = 0
        self.dir, self.dir2 = 0, 0
        self.face_dir = 0
        self.jump_check = False

        self.image = load_image('character_sheet.png')
        self.cursor = load_image('gun_cursor.png')
        self.jump = load_image('jump_sheet.png')
        self.weapon1 = load_image('weapon1.png')
        self.rotation_image = None

        self.q = []  # 이벤트 큐 초기화
        self.cur_state = IDLE
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

    def fire_shot(self):
        shots = Bullet(self.mouse_x, self.mouse_y, self.x, self.y)
        game_world.add_object(shots, 1)
        game_world.add_collision_pairs(shots, server.enemy1, 'shots:enemy1')

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 35

