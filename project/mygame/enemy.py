from pico2d import *
import game_framework
import game_world
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
import math
import random
import server
from bullet import Bullet

PIXEL_PER_METER = (10.0 / 0.01) # 10 pixel 30 cm
RUN_SPEED_KMPH = 0.5 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

class Enemy1:
    image_idle = None
    image_attack = None

    def load_images(self):
        if Enemy1.image_idle == None:
            Enemy1.image_idle = load_image('enemy1_idle.png')
        if Enemy1.image_attack == None:
            self.image_attack = load_image('enemy1_attack.png')

    def __init__(self):
        self.prepare_patrol_points()
        self.patrol_order = 1
        self.x, self.y = self.patrol_positions[0]
        self.load_images()
        self.life = True
        self.frame = 0
        self.speed = 0
        self.dir = 0
        self.timer = 1.0  # change direction every 1 sec when wandering
        self.wait_timer = 2.0
        self.build_behavior_tree()
        self.attack = False
        self.attack_count = 0

    def wander(self):
        self.speed = RUN_SPEED_PPS
        self.timer -= game_framework.frame_time
        if self.timer <= 0:
            self.timer = 1.0
            self.dir = random.random() * 2 * math.pi
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING

    def wait(self):
        self.speed = 0
        self.wait_timer -= game_framework.frame_time
        if self.wait_timer <= 0:
            self.wait_timer = 2.0
            return BehaviorTree.SUCCESS

        return BehaviorTree.RUNNING


    def find_player(self):
        distance = (server.hero.x - self.x) ** 2 + (server.hero.y - self.y) ** 2
        if distance < (PIXEL_PER_METER * 10) ** 2:
            return BehaviorTree.SUCCESS
        else:
            self.speed = 0
        return BehaviorTree.FAIL

    # def move_to_player(self):
    #     self.speed = RUN_SPEED_PPS
    #     self.dir = math.atan2(server.hero.y - self.y, server.hero.x - self.x)
    #     return BehaviorTree.SUCCESS

    def attack_to_player(self):
        self.speed = 0
        self.attack = True
        if self.attack_count == 0:
            enemy_shot = Bullet(server.hero.x, server.hero.y, self.x, self.y)
            game_world.add_object(enemy_shot, 1)
            self.attack_count += 1
            print('self.frame == ',self.frame)
        if self.frame >= 10.9:
            self.attack_count = 0

        return BehaviorTree.SUCCESS


    def get_next_position(self):
        self.target_x, self.target_y = self.patrol_positions[self.patrol_order % len(self.patrol_positions)]
        self.patrol_order += 1
        self.dir = math.atan2(self.target_y - self.y, self.target_x - self.x)
        return BehaviorTree.SUCCESS

    def move_to_target(self):
        self.speed = RUN_SPEED_PPS
        distance = (self.target_x - self.x) ** 2 + (self.target_y - self.y) ** 2

        if distance < PIXEL_PER_METER ** 2:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING

    def prepare_patrol_points(self):
        # positions for origin at top, left
        positions = [(43, 750), (1118, 750), (1050, 530), (575, 220), (235, 33), (575, 220), (1050, 530), (1118, 750)]
        self.patrol_positions = []
        for p in positions:
                self.patrol_positions.append((p[0], 1024 - p[1]))  # convert for origin at bottom, left

    def build_behavior_tree(self):

        wander_node = LeafNode("Wander", self.wander)
        find_player_node = LeafNode("Find Player", self.find_player)
        attack_to_player_node = LeafNode("attack to Player", self.attack_to_player)
        chase_node = SequenceNode("Chase")
        chase_node.add_children(find_player_node, attack_to_player_node)
        wander_chase_node = SelectorNode("WanderChase")
        wander_chase_node.add_children(chase_node, wander_node)
        self.bt = BehaviorTree(wander_chase_node)

    def update(self):
        self.bt.run()
        if self.attack == False:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        elif self.attack == True:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11

        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(50, self.x, 1200 - 50)
        self.y = clamp(50, self.y, 600 - 50)

    def draw(self):
        if self.attack == False:
            self.image_idle.clip_draw(int(self.frame) * 40, 62, 40, 62, self.x, self.y, 120, 120)
        elif self.attack == True:
            self.image_attack.clip_draw(int(self.frame) * 45, 67, 45, 67, self.x, self.y, 120, 120)

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        if self.attack == True:
            return self.x - 10, self.y - 30, self.x + 60, self.y + 30
        elif self.attack == False:
            return self.x - 5, self.y - 30, self.x + 65, self.y + 30
    def handle_collision(self, other, group):
        if group == 'shots:enemy1':
            if self.life == True:
                self.life = False
                game_world.remove_object(self)



