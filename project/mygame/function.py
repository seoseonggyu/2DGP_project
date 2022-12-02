import math
from server import map_w, map_h, hero





def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

# 만들고 쓰지 않는 것
# class IDLE:
#     def enter(self, event): # 상태에 들어갈 때 행하는 액션
#         print('Enter Idle')
#         self.dir = 0
#         self.dir2 = 0
#
#     def exit(self, event):
#         print('eixt Idle')
#         print('-------')
#
#     def do(self):
#         self.frame = self.face_dir
#         # self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
#         # self.y += self.dir2 * RUN_SPEED_PPS * game_framework.frame_time
#
#     # 외부에서 전달되는 self
#     def draw(self):
#         self.cursor.clip_draw(0, 0, 22, 22, self.mouse_x, self.mouse_y, gun_image_size, gun_image_size)
#         self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, character_image_size, character_image_size)
#
# class RUN:
#     @staticmethod
#     def enter(self, event):
#         print('Enter run')
#         if event == DD:
#             self.way = 0
#             self.dir += 1
#
#         elif event == AD:
#             self.way = 1
#             self.dir -= 1
#
#         elif event == WD:
#             self.way = 4
#             self.dir2 += 1
#
#         elif event == SD:
#             self.way = 5
#             self.dir2 -= 1
#
#         if event == DU:
#             if self.dir2 > 0:
#                 self.way = 4
#                 self.dir -= 1
#             elif self.dir2 < 0:
#                 self.way = 5
#                 self.dir -= 1
#             elif self.dir < 0:
#                 self.way = 1
#                 self.dir = -1
#
#         elif event == AU:
#             if self.dir2 > 0:
#                 self.way = 4
#                 self.dir += 1
#             elif self.dir2 < 0:
#                 self.way = 5
#                 self.dir += 1
#             elif self.dir > 0:
#                 self.way = 0
#                 self.dir = 1
#
#         elif event == WU:
#             if self.dir > 0:
#                 self.way = 0
#                 self.dir2 -= 1
#             elif self.dir < 0:
#                 self.way = 1
#                 self.dir2 -= 1
#             elif self.dir2 < 0:
#                 self.way = 5
#                 self.dir2 = -1
#
#         elif event == SU:
#             if self.dir > 0:
#                 self.way = 0
#                 self.dir2 += 1
#             elif self.dir < 0:
#                 self.way = 1
#                 self.dir2 += 1
#             elif self.dir2 > 0:
#                 self.way = 4
#                 self.dir2 = 1
#
#     @staticmethod
#     def exit(self, event):
#         print('exit run')
#         print('-------')
#         self.face_dir = self.way
#
#     @staticmethod
#     def do(self): # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
#         self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
#
#         if self.map_crash == True:
#             self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
#             self.y += self.dir2 * RUN_SPEED_PPS * game_framework.frame_time
#
#     @staticmethod
#     def draw(self):
#         self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, character_image_size, character_image_size)
#         self.cursor.clip_draw(0, 0, 22, 22, self.mouse_x, self.mouse_y, gun_image_size, gun_image_size)
#
# class RUN2:
#     @staticmethod
#     def enter(self, event):
#         print('Enter RUN2')
#         if event == DD:
#             if self.dir2 > 0:
#                 self.way = 2
#                 self.dir += 1
#             elif self.dir2 < 0:
#                 self.way = 0
#                 self.dir += 1
#             else:
#                 self.dir = 1
#                 self.way = 0
#
#         elif event == AD:
#             if self.dir2 > 0:
#                 self.way = 3
#                 self.dir -= 1
#             elif self.dir2 < 0:
#                 self.way = 1
#                 self.dir -= 1
#             else:
#                 self.dir = -1
#                 self.way = 1
#
#         elif event == WD:
#             if self.dir > 0:
#                 self.way = 2
#                 self.dir2 += 1
#             elif self.dir < 0:
#                 self.way = 3
#                 self.dir2 += 1
#             else:
#                 self.dir2 = 1
#                 self.way = 4
#
#         elif event == SD:
#             if self.dir > 0:
#                 self.way = 0
#                 self.dir2 -= 1
#             elif self.dir < 0:
#                 self.way = 1
#                 self.dir2 -= 1
#             else:
#                 self.dir2 = -1
#                 self.way = 5
#
#     @staticmethod
#     def exit(self, event):
#         print('exit RUN2')
#         print('-------')
#
#     @staticmethod
#     def do(self): # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
#         self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
#         # self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
#         # self.y += self.dir2 * RUN_SPEED_PPS * game_framework.frame_time
#
#         self.x = pico2d.clamp(0, self.x, 1200)
#         self.y = pico2d.clamp(0, self.y, 600)
#
#     @staticmethod
#     def draw(self):
#         self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, character_image_size, character_image_size)
#         self.cursor.clip_draw(0, 0, 22, 22, self.mouse_x, self.mouse_y, gun_image_size, gun_image_size)