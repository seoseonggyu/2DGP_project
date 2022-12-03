from pico2d import *
import game_framework
import game_world
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
import math
import random
import server
import winsound
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

class TargetMarker:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        self.image = load_image('hand_arrow.png')
    def update(self):
        pass
    def draw(self):
        self.image.draw(self.x, self.y, 50, 50)


class Enemy1:
    image_idle = None
    image_attack = None
    image_item = None

    def __init__(self):
        if Enemy1.image_idle == None:
            Enemy1.image_idle = load_image('enemy1_idle.png')
        if Enemy1.image_item == None:
            Enemy1.image_item = load_image('item.png')
        # self.x, self.y = random.randint(2000, 3000), random.randint(100, 1200)
        self.x, self.y = 2500, 1000
        self.tx, self.ty = 2500, 1000
        self.dir = random.random() * 2 * math.pi
        self.speed = 0
        self.timer = 1.0
        self.build_behavior_tree()
        self.way = 0

        self.target_marker = TargetMarker(self.tx, self.ty)
        game_world.add_object(self.target_marker, 1)


        self.hp = 100
        self.frame = 0


        self.font = load_font('ENCR10B.TTF', 16)
        self.font2 = load_font('ENCR10B.TTF', 16)


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.x -= server.hero.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y -= server.hero.dir2 * RUN_SPEED_PPS * game_framework.frame_time
        self.bt.run()

        # if self.x - server.hero.x > 0:
        #     self.way = 0
        # else:
        #     self.way = 1

        if self.hp <= 0:
            game_world.remove_object(self)

    def draw(self):
        self.image_idle.clip_draw(int(self.frame) * 40, 62 * self.way, 40, 62, self.x, self.y, enemy_size, enemy_size)
        self.font.draw(self.x - 60, self.y + 50, '%7d' % self.hp, (0, 0, 255))
        self.font2.draw(self.x -60, self.y + 100, '%7d' % self.x, (255, 255, 255))

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 30, self.x + 70, self.y + 30

    def handle_collision(self, other, group):
        if group == 'shots:enemy1':
            self.hp -= 100

    def play_beep(self):
        winsound.Beep(440, 100)
        return BehaviorTree.SUCCESS


    def find_random_location(self):
        # x = 2500, y = 1000
        self.tx, self.ty = random.randint(1500, 3000), random.randint(0, 1200)
        self.target_marker.x, self.target_marker.y = self.tx, self.ty
        return BehaviorTree.SUCCESS

    def move_to(self, radius = 0.5):
        distance = (self.tx - self.x) ** 2 + (self.ty - self.y) ** 2
        self.dir = math.atan2(self.ty - self.y, self.tx - self.x)
        if distance < (PIXEL_PER_METER * radius) ** 2:
            self.speed = 0
            return BehaviorTree.SUCCESS
        else:
            self.speed = RUN_SPEED_PPS
            return BehaviorTree.RUNNING

    def build_behavior_tree(self):
        find_random_location_node = LeafNode('Find Random Location', self.find_random_location)
        move_to_node = LeafNode('Move To', self.move_to)
        play_beep_node = LeafNode('Play Beep', self.play_beep)

        wander_sequence = SequenceNode('Wander', find_random_location_node, move_to_node, play_beep_node)
        self.bt = BehaviorTree(wander_sequence)

        pass





