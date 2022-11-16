from pico2d import *
import game_world
import math
import play_state

class Bullet:
    image = None

    def __init__(self, mousex, mousey, posx, posy):
        if Bullet.image == None:
            Bullet.image = load_image('bullet.png')
        self.x = posx
        self.y = posy
        self.dir = (mousex - posx, mousey- posy)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0] / length, self.dir[1] / length)

        self.speed = 1

    def draw(self):
        self.image.draw(self.x, self.y, 30, 30)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x = self.x + self.dir[0] * self.speed
        self.y = self.y + self.dir[1] * self.speed

        if self.x  < 25 or self.x > 1200 - 100 or self.y < 25 or self.y > 600 - 25:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        if play_state.enemy1.life == True:
            if group == 'shots:enemy1':
                game_world.remove_object(self)


