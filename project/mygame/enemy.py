from pico2d import *
import game_framework

PIXEL_PER_METER = (10.0 / 0.01) # 10 pixel 30 cm
RUN_SPEED_KMPH = 0.5 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Action Speed
TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6

class Enemy1:
    def __init__(self):
        self.image_idle = load_image('enemy1_idle.png')
        self.image_attack = load_image('enemy1_attack.png')
        self.frame = 0
        self.x, self.y = 600, 300
        self.found = True


    def update(self):
        if self.found == False:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        elif self.found == True:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11

    def draw(self):
        if self.found == False:
            self.image_idle.clip_draw(int(self.frame) * 40, 0, 40, 42, self.x, self.y, 120, 120)
        elif self.found == True:
            self.image_attack.clip_draw(int(self.frame) * 45, 0, 45, 47, self.x, self.y, 120, 120)