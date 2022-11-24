import math

from pico2d import *
import game_framework
import play_state
from bullet import Bullet
import server
import game_world
from enemy import Enemy1
import pygame

image_center_w = 1000
image_center_h = 600

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
            self.fire_shot()

    def do(self):  # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        self.mouse_angle = math.pi - math.atan2(self.mouse_x - image_center_w, self.mouse_y - image_center_h)

        # print('mouse_angle: ',math.degrees(math.pi - math.atan2(self.mouse_x - 600, self.mouse_y - 300)))
        # print('angle: ', math.degrees(5/6*math.pi))

        if (math.degrees(self.mouse_angle)) >= math.degrees(1/6 * math.pi) and (math.degrees(self.mouse_angle) <= math.degrees(2/3 * math.pi)):
            self.way = 0
        elif (math.degrees(self.mouse_angle)) > math.degrees(2/3 * math.pi) and math.degrees(self.mouse_angle) <= math.degrees(5/6 * math.pi):
            self.way = 2
        elif (math.degrees(self.mouse_angle)) > math.degrees(5/6 * math.pi) and math.degrees(self.mouse_angle) <= math.degrees(7/6 * math.pi):
            self.way = 4
        elif (math.degrees(self.mouse_angle)) > math.degrees(7/6 * math.pi) and math.degrees(self.mouse_angle) <= math.degrees(4/3 * math.pi):
            self.way = 3
        elif (math.degrees(self.mouse_angle)) > math.degrees(4/3 * math.pi) and math.degrees(self.mouse_angle) <= math.degrees(2 * math.pi - 1/6 * math.pi):
            self.way = 1
        elif (math.degrees(self.mouse_angle)) > math.degrees(2 * math.pi - 1/6 * math.pi) and math.degrees(self.mouse_angle) <= math.degrees(2 * math.pi):
            self.way = 5
        elif (math.degrees(self.mouse_angle)) > math.degrees(0) and math.degrees(self.mouse_angle) <= math.degrees(1/6 * math.pi):
            self.way = 5

        self.frame = self.face_dir
        self.x = pico2d.clamp(0, self.x, 2 * image_center_w - 50)
        self.y = pico2d.clamp(0, self.y, 2 * image_center_h - 50)


    def draw(self):
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
        if self.using_jump == False:
            if event == DD:
             self.dir += 1

        elif self.using_jump == True:
            pass

        # elif event == AD:
        #     self.dir -= 1
        #
        # elif event == WD:
        #     self.dir2 += 1
        #
        # elif event == SD:
        #     self.dir2 -= 1
        #
        # if event == DU:
        #     if self.dir2 > 0:
        #         self.dir -= 1
        #     elif self.dir2 < 0:
        #         self.dir -= 1
        #     elif self.dir < 0:
        #         self.dir = -1
        #
        # elif event == AU:
        #     if self.dir2 > 0:
        #         self.dir += 1
        #     elif self.dir2 < 0:
        #         self.dir += 1
        #     elif self.dir > 0:
        #         self.dir = 1
        #
        # elif event == WU:
        #     if self.dir > 0:
        #         self.dir2 -= 1
        #     elif self.dir < 0:
        #         self.dir2 -= 1
        #     elif self.dir2 < 0:
        #         self.dir2 = -1
        #
        # elif event == SU:
        #     if self.dir > 0:
        #         self.dir2 += 1
        #     elif self.dir < 0:
        #         self.dir2 += 1
        #     elif self.dir2 > 0:
        #         self.dir2 = 1

    def exit(self, event):  # 상태를 나올 때 행하는 액션 , 고개 들기
        if event == AT:
            self.fire_shot()

    def do(self):  # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.mouse_angle = math.pi - math.atan2(self.mouse_x - image_center_w, self.mouse_y - image_center_h)

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        # self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        # self.y += self.dir2 * RUN_SPEED_PPS * game_framework.frame_time

        self.x = pico2d.clamp(0, self.x, 2 * image_center_w - 50)
        self.y = pico2d.clamp(0, self.y, 2 * image_center_h - 50)

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

    def draw(self):
        self.cursor.clip_draw(0, 0, 22, 22, self.mouse_x, self.mouse_y, gun_image_size, gun_image_size)

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

        self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, character_image_size, character_image_size)

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
        self.mouse_angle = math.pi - math.atan2(self.mouse_x - image_center_w, self.mouse_y - image_center_h)

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


        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        # self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        # self.y += self.dir2 * RUN_SPEED_PPS * game_framework.frame_time

        self.x = pico2d.clamp(0, self.x, 2 * image_center_w - 50)
        self.y = pico2d.clamp(0, self.y, 2 * image_center_h - 50)

    @staticmethod
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

        self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, character_image_size, character_image_size)
        self.cursor.clip_draw(0, 0, 22, 22, self.mouse_x, self.mouse_y, gun_image_size, gun_image_size)


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
        # self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        # self.y += self.dir2 * RUN_SPEED_PPS * game_framework.frame_time

    # 외부에서 전달되는 self
    def draw(self):
        self.cursor.clip_draw(0, 0, 22, 22, self.mouse_x, self.mouse_y, gun_image_size, gun_image_size)
        self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, character_image_size, character_image_size)

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

        if self.map_crash == True:
            self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
            self.y += self.dir2 * RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, character_image_size, character_image_size)
        self.cursor.clip_draw(0, 0, 22, 22, self.mouse_x, self.mouse_y, gun_image_size, gun_image_size)

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
        self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, character_image_size, character_image_size)
        self.cursor.clip_draw(0, 0, 22, 22, self.mouse_x, self.mouse_y, gun_image_size, gun_image_size)


# 42 , 41
class JUMP:
    def enter(self, event): # 상태에 들어갈 때 행하는 액션
        print('enter jump')

        if self.dir > 0:
            self.way = 0
            pass

    def exit(self, event):
        print('jump exit')
        print('-------')
        self.finish_jump = False
        self.using_jump = True

    def do(self):
        if self.finish_jump == False:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10
        elif self.finish_jump == True:
            self.frame = 0

        if self.frame >= 9:
            self.finish_jump = True
            self.using_jump = False
            self.dir -= 1

    def draw(self):
        self.cursor.clip_draw(0, 0, 22, 22, self.mouse_x, self.mouse_y, gun_image_size, gun_image_size)

        if self.finish_jump == False:
            self.jump.clip_draw(int(self.frame) * 42, 41 * self.way, 42, 41, self.x, self.y - 41, character_image_size, character_image_size)
        elif self.finish_jump == True:
            self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, character_image_size, character_image_size)

next_stage = {
    IDLE:   {DD: RUN,    AD: RUN,    WD: RUN,    SD: RUN,    DU: IDLE, AU: IDLE, WU: IDLE, SU: IDLE, QD: WEAPON_IDLE,
             AT: IDLE, JP: JUMP},
    RUN:    {DD: RUN2,   AD: RUN2,   WD: RUN2,   SD: RUN2,   DU: IDLE, AU: IDLE, WU: IDLE, SU: IDLE, QD: WEAPON_IDLE,
             AT: RUN,  JP: JUMP},
    RUN2:   {DD: RUN2,   AD: RUN2,   WD: RUN2,   SD: RUN2,   DU: RUN,  AU: RUN,  WU: RUN,  SU: RUN,  QD: WEAPON_IDLE,
             AT: RUN2, JP: JUMP},
    WEAPON_IDLE: {DD: WEAPON_RUN,  AD: WEAPON_RUN,  WD: WEAPON_RUN,  SD: WEAPON_RUN,  DU: WEAPON_IDLE, AU: WEAPON_IDLE,
                  WU: WEAPON_IDLE, SU: WEAPON_IDLE, AT: WEAPON_IDLE, QD: IDLE, JP: WEAPON_IDLE},
    WEAPON_RUN:  {DD: WEAPON_RUN2, AD: WEAPON_RUN2, WD: WEAPON_RUN2, SD: WEAPON_RUN2, DU: WEAPON_IDLE, AU: WEAPON_IDLE,
                  WU: WEAPON_IDLE, SU: WEAPON_IDLE, AT: WEAPON_RUN,  JP: JUMP},
    WEAPON_RUN2: {DD: WEAPON_IDLE, AD: WEAPON_IDLE, WD: WEAPON_IDLE, SD: WEAPON_RUN2, DU: WEAPON_RUN,  AU: WEAPON_RUN,
                  WU: WEAPON_RUN,  SU: WEAPON_RUN,  AT: WEAPON_RUN2, JP: JUMP},
    JUMP: {DD: WEAPON_RUN, AD: WEAPON_RUN, WD: WEAPON_RUN, SD: WEAPON_RUN, DU: JUMP,  AU: JUMP,
                  WU: JUMP,  SU: JUMP}

}

class character:
    def __init__(self):

        self.mouse_angle = 0
        self.x, self.y = image_center_w, image_center_h # 캐릭터 좌표
        self.mouse_x, self.mouse_y = 0, 0 # 마우스 좌표
        self.frame = 0
        self.way = 0
        self.dir, self.dir2 = 0, 0
        self.face_dir = 0

        self.finish_jump = False
        self.using_jump = False

        self.map_crash = False

        self.image = load_image('character_sheet.png')
        self.cursor = load_image('gun_cursor.png')
        self.jump = load_image('jump_sheet.png')
        self.weapon1 = load_image('weapon1.png')

        self.q = []  # 이벤트 큐 초기화
        self.cur_state = WEAPON_IDLE
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
        draw_rectangle(*self.get_bb2())

    def fire_shot(self):
        shots = Bullet(self.mouse_x, self.mouse_y, self.x, self.y, 2 * RUN_SPEED_PPS)
        game_world.add_object(shots, 1)
        game_world.add_collision_pairs(shots, None, 'shots:enemy1')

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 35

    def get_bb2(self):
        return self.x - 520, self.y - 530, self.x + 520, self.y + 530

    def map_handle_collision(self, other, group):
        if group == 'hero:stage1':
            self.map_crash = True

    def handle_collision(self, other, group):
        pass


