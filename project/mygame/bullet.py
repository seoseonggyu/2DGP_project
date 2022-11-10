from pico2d import *
import game_world

class bullet:
    image = None

    def __int__(self, mousex, mousey, velocity = 1):
        if bullet.image == None:
            bullet.image = load_image('bullet.png')
        self.x, self.y, self.velocity = mousex, mousey, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity
        self.y += self.velocity

        if self.x < 25 or self.x > 800 - 25 or self.y < 25 or self.y > 800 - 25:
            game_world.remove_object(self)

