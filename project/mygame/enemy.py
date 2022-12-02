from pico2d import *
import game_framework
import game_world
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
import math
import random
import server
from bullet import Bullet
import play_state

enemy_size = 150

PIXEL_PER_METER = (10.0 / 0.01) # 10 pixel 30 cm
RUN_SPEED_KMPH = 3 # Km / Hour
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
    image_item = None

    def __init__(self):
        if Enemy1.image_idle == None:
            Enemy1.image_idle = load_image('enemy1_idle.png')
        if Enemy1.image_item == None:
            Enemy1.image_item = load_image('item.png')
        self.x, self.y = random.randint(2000, 3000), random.randint(100, 1200)
        self.hp = 100
        self.frame = 0
        self.font = load_font('ENCR10B.TTF', 16)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.x -= server.hero.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y -= server.hero.dir2 * RUN_SPEED_PPS * game_framework.frame_time

        if self.hp <= 0:
            server.hero.item_count += 1
            game_world.remove_object(self)

    def draw(self):
        self.image_idle.clip_draw(int(self.frame) * 40, 62, 40, 62, self.x, self.y, enemy_size, enemy_size)
        self.font.draw(self.x - 60, self.y + 50, '%7d' % self.hp, (0, 0, 255))
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 30, self.x + 70, self.y + 30

    def handle_collision(self, other, group):
        if group == 'shots:enemy1':
            self.hp -= 100





