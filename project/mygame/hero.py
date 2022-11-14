from pico2d import *
import game_framework
from bullet import Bullet
import game_world
import pygame


# Run Speed
PIXEL_PER_METER = (10.0 / 0.01) # 10 pixel 30 cm
RUN_SPEED_KMPH = 1 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Action Speed
TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6


#2 이벤트 정의
AT,DD, AD, WD, SD, DU, AU, WU, SU, QD = range(10)


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

        print('mouse_angle: ',self.mouse_angle)

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
        self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, 120, 120)

        # self.image.clip_composite_draw(int(self.frame) * 40, 42 * self.way, 40, 42,
        #                                self.mouse_angle, '', self.x, self.y, 120, 120)
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
        self.mouse_angle = math.pi - math.atan2(self.mouse_x - 600, self.mouse_y - 300)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.dir2 * RUN_SPEED_PPS * game_framework.frame_time

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

        self.x = pico2d.clamp(0, self.x, 1200)
        self.y = pico2d.clamp(0, self.y, 600)

    @staticmethod
    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, 120, 120)
        self.cursor.draw(self.mouse_x, self.mouse_y)


class IDLE:
    def enter(self, event): # 상태에 들어갈 때 행하는 액션
        print('enter idle')
        self.dir = 0
        self.dir2 = 0

    def exit(self, event): # 상태를 나올 때 행하는 액션 , 고개 들기
        pass

    def do(self): # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = self.face_dir


    # 외부에서 전달되는 self
    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, 120, 120)
        self.cursor.draw(self.mouse_x, self.mouse_y)

class RUN:
    @staticmethod
    def enter(self, event):
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
        print('exit RUN')
        self.face_dir = self.way
        pass

    @staticmethod
    def do(self): # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.dir2 * RUN_SPEED_PPS * game_framework.frame_time


        self.x = pico2d.clamp(0, self.x, 1200)
        self.y = pico2d.clamp(0, self.y, 600)

    @staticmethod
    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, 120, 120)
        self.cursor.draw(self.mouse_x, self.mouse_y)

class RUN2:
    @staticmethod
    def enter(self, event):
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

    @staticmethod
    def do(self): # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.dir2 * RUN_SPEED_PPS * game_framework.frame_time

        self.x = pico2d.clamp(0, self.x, 1200)
        self.y = pico2d.clamp(0, self.y, 600)

    @staticmethod
    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, 120, 120)
        self.cursor.draw(self.mouse_x, self.mouse_y)

next_stage = {
    IDLE:   {DD: RUN,    AD: RUN,    WD: RUN,    SD: RUN,    DU: IDLE,          AU: IDLE,          WU: IDLE,          SU: IDLE, QD: WEAPON_IDLE},
    RUN:    {DD: RUN2,   AD: RUN2,   WD: RUN2,   SD: RUN2,   DU: IDLE,          AU: IDLE,          WU: IDLE,          SU: IDLE},
    RUN2:   {DD: IDLE,   AD: IDLE,   WD: IDLE,   SD: IDLE,   DU: RUN,           AU: RUN,           WU: RUN,           SU: RUN},
    WEAPON_IDLE: {DD: WEAPON_RUN, AD: WEAPON_RUN, WD: WEAPON_RUN, SD: WEAPON_RUN, DU: WEAPON_IDLE,   AU: WEAPON_IDLE,   WU: WEAPON_IDLE, SU: WEAPON_IDLE, AT: WEAPON_IDLE, QD: IDLE},
    WEAPON_RUN: {DD: WEAPON_RUN2, AD: WEAPON_RUN2, WD: WEAPON_RUN2, SD: WEAPON_RUN2, DU: WEAPON_IDLE,   AU: WEAPON_IDLE,   WU: WEAPON_IDLE, SU: WEAPON_IDLE, AT: WEAPON_RUN},
    WEAPON_RUN2: {DD: WEAPON_IDLE, AD: WEAPON_IDLE, WD: WEAPON_IDLE, SD: WEAPON_RUN2, DU: WEAPON_RUN,   AU: WEAPON_RUN,   WU: WEAPON_RUN, SU: WEAPON_RUN, AT: WEAPON_RUN2}
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

        self.image = load_image('character_sheet.png')
        self.cursor = load_image('gun_cursor.png')
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

    def fire_shot(self):
        shots = Bullet(self.mouse_x, self.mouse_y, self.x, self.y)
        game_world.add_object(shots, 1)