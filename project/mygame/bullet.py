from pico2d import *
import game_world
import pygame
import math

class Bullet:
    image = None

    def __init__(self, mousex, mousey, posx, posy):
        if Bullet.image == None:
            Bullet.image = load_image('bullet.png')
        self.pos = (posx, posy)
        self.dir = (mousex - posx, mousey- posy)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0] / length, self.dir[1] / length)

        self.speed = 2.5

    def draw(self):
        self.image.draw(self.pos[0], self.pos[1], 30, 30)

    def update(self):
        self.pos = (self.pos[0] + self.dir[0] * self.speed,
                    self.pos[1] + self.dir[1] * self.speed)

        if self.pos[0] < 25 or self.pos[0] > 1200 - 25 or self.pos[1] < 25 or self.pos[1] > 600 - 25:
            game_world.remove_object(self)

