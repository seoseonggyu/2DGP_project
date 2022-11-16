from pico2d import *

import bullet
import game_framework
import game_world

from hero import character
from life import Life
from enemy import Enemy1
from bullet import Bullet

from map1 import Map1
import title_state
import logo_state

hero = None
stage1 = None
gr = None
lifes = []
enemy = None

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

    lifes.append(Life(50, 550))
    lifes.append(Life(100, 550))
    lifes.append(Life(150, 550))

    game_world.add_object(hero, 1)
    game_world.add_object(enemy1, 1)

    # stage1 = Map1()
    #game_world.add_object(stage1, 0)

    for i in lifes:
        game_world.add_object(i, 0)

# 종료
def exit():
    for a, b, group  in game_world.all_collision_pairs():
        print('a:  b:  group:  ', a, b, group)
    game_world.clear()

def update():
    hide_cursor()
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('COLLISION ', group)
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

def collide(a, b):

    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True
