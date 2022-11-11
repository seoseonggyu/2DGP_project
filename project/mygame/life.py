from pico2d import *

class Life:
    image = None

    def __init__(self, posx, posy):
        if Life.image == None:
            Life.image = load_image('life.png')
        self.x, self.y = posx, posy

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y, 50, 50)