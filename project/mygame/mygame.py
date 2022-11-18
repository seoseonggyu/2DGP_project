import pico2d
import game_framework
import play_state
import title_state

map_w = 2000
map_h = 1200
pico2d.open_canvas(map_w, map_h)
game_framework.run(title_state)
pico2d.close_canvas()