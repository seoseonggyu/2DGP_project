from pico2d import *
import server
import game_framework

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

class Map1:
    def __init__(self, ):
        self.image = load_image('map1.png')
        self.image_background = load_image('background.png')
        self.x, self.y = 1800, 1000
        self.map_crash = False



    def update(self):
        if self.map_crash == False:
            self.x += -server.hero.dir * RUN_SPEED_PPS * game_framework.frame_time
            self.y += -server.hero.dir2 * RUN_SPEED_PPS * game_framework.frame_time


    def draw(self):
        self.image_background.draw(1000, 600, 3000, 4000)
        self.image.draw(self.x, self.y, 3000, 2200)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 1420, self.y - 1030, self.x + 1420, self.y + 1130

    def map_handle_collision(self, other, group):
        if group == 'hero:stage1':
            self.map_crash = True


    def handle_collision(self, other, group):
        pass
