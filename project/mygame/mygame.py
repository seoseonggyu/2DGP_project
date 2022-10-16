import pico2d
import game_framework
import character
# import bullet

pico2d.open_canvas(1200, 800)
game_framework.run(character)
pico2d.close_canvas()