from pico2d import *
import game_framework
import game_world

from hero import character
from life import Life
from enemy import Enemy1
from map1 import Map1

import server
from function import collide

import title_state
import logo_state

map_h = 1200


def handle_events():

    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_QUIT:
            game_framework.quit()
        if event.type == pico2d.SDL_MOUSEMOTION:
            server.hero.mouse_x, server.hero.mouse_y = event.x, map_h - 1 - event.y
        if (event.type, event.key) == (pico2d.SDL_KEYDOWN, pico2d.SDLK_ESCAPE):
            game_framework.quit()
        else:
            server.hero.handle_event(event)

# 초기화
def enter():
    server.stage1 = Map1()
    game_world.add_object(server.stage1, 0)

    server.hero = character()
    game_world.add_object(server.hero, 1)

    server.enemy1_list = [Enemy1() for i in range(10)]
    game_world.add_objects(server.enemy1_list, 1)

    server.lifes.append(Life(50, map_h - 50))
    server.lifes.append(Life(110, map_h - 50))
    server.lifes.append(Life(170, map_h - 50))

    game_world.add_collision_pairs(None, server.enemy1_list, 'shots:enemy1')

    for i in server.lifes:
        game_world.add_object(i, 0)

# 종료
def exit():
    for a, b, group in game_world.all_collision_pairs():
        print('a:  b:  group:  ', a, b, group)
    game_world.clear()

def update():
    hide_cursor()
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            a.handle_collision(b, group)
            b.handle_collision(a, group)

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
