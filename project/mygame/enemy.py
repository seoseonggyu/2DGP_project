from pico2d import *
import game_framework
import game_world

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
    image_idle = None
    image_attack = None

    def __init__(self):
        if Enemy1.image_idle == None:
            Enemy1.image_idle = load_image('enemy1_idle.png')
        if Enemy1.image_attack == None:
            self.image_attack = load_image('enemy1_attack.png')
        self.life = True
        self.frame = 0
        self.x, self.y = 600, 300


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

    def draw(self):
        self.image_idle.clip_draw(int(self.frame) * 40, 0, 40, 42, self.x, self.y, 120, 120)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def handle_collision(self, other, group):
        if group == 'shots:enemy1':
            if self.life == True:
                self.life = False
                game_world.remove_object(self)



