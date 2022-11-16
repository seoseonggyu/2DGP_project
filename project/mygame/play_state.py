from pico2d import *
import game_framework
import game_world

from hero import character
from life import Life
from enemy import Enemy1

from map1 import Map1
import title_state
import logo_state

hero = None
stage1 = None
gr = None
enemy1 = None
lifes = []

def handle_events():

    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_QUIT:
            game_framework.quit()
        if event.type == pico2d.SDL_MOUSEMOTION:
            hero.mouse_x, hero.mouse_y = event.x, 600 - 1 - event.y
        if (event.type, event.key) == (pico2d.SDL_KEYDOWN, pico2d.SDLK_ESCAPE):
            game_framework.quit()
        else:
            hero.handle_event(event)

# 초기화
def enter():
    global hero, lifes, stage1, enemy1
    hero = character()
    enemy1 = Enemy1()
    #stage1 = Map1()
    lifes.append(Life(50, 550))
    lifes.append(Life(100, 550))
    lifes.append(Life(150, 550))

    game_world.add_object(hero, 1)
    game_world.add_object(enemy1, 1)
    #game_world.add_object(stage1, 0)
    for i in lifes:
        game_world.add_object(i, 0)

# 종료
def exit():
    game_world.clear()

def update():
    hide_cursor()
    for game_object in game_world.all_objects():
        game_object.update()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass