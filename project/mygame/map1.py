from pico2d import *
from hero import character


class Map1:
    def __init__(self, ):
        self.image = load_image('map1.png')
        self.x, self.y = 350, 350


    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y, 1000, 1000)