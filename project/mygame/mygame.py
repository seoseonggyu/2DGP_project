import pico2d
import game_framework
import logo_state
import bullet

pico2d.open_canvas(1200, 800)
# game_framework.run(logo_state)
game_framework(bullet)
pico2d.close_canvas()