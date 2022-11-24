from pico2d import *
import game_world
import math
import game_framework
import server

PIXEL_PER_METER = (10.0 / 0.01) # 10 pixel 30 cm
RUN_SPEED_KMPH = 3 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6


class Bullet:
    image = None

    def __init__(self, mousex, mousey, posx, posy, speed):
        if Bullet.image == None:
            Bullet.image = load_image('bullet.png')
        self.x, self.y = 1000, 600
        self.dir = math.atan2(mousey - posy, mousex - posx)

        self.speed = speed

    def draw(self):
        self.image.draw(self.x, self.y, 30, 30)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time -server.hero.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time -server.hero.dir2 * RUN_SPEED_PPS * game_framework.frame_time

        if self.x < 50 or self.x > 1950 or self.y < 50 or self.y > 1150:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        if group == 'shots:enemy1':
            game_world.remove_object(self)





