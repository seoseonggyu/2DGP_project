import pico2d
import game_framework
import play_state
# import bullet

map_w = 1200
map_h = 600
pico2d.open_canvas(map_w, map_h)
game_framework.run(play_state)
pico2d.close_canvas()