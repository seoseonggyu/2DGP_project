import math
from server import map_w, map_h, hero

def MOUSE_ANGLE(a, b):
    mouse_angle = math.pi - math.atan2(a - map_w / 2, b - map_h / 2)

    if (math.degrees(mouse_angle)) >= math.degrees(1 / 6 * math.pi) and (
            math.degrees(mouse_angle) <= math.degrees(2 / 3 * math.pi)):
        return 0
    elif (math.degrees(mouse_angle)) > math.degrees(2 / 3 * math.pi) and math.degrees(
            mouse_angle) <= math.degrees(5 / 6 * math.pi):
        return 2
    elif (math.degrees(mouse_angle)) > math.degrees(5 / 6 * math.pi) and math.degrees(
            mouse_angle) <= math.degrees(7 / 6 * math.pi):
        return 3
    elif (math.degrees(mouse_angle)) > math.degrees(7 / 6 * math.pi) and math.degrees(
            mouse_angle) <= math.degrees(4 / 3 * math.pi):
        return 3
    elif (math.degrees(mouse_angle)) > math.degrees(4 / 3 * math.pi) and math.degrees(
            mouse_angle) <= math.degrees(2 * math.pi - 1 / 6 * math.pi):
        return 1
    elif (math.degrees(mouse_angle)) > math.degrees(2 * math.pi - 1 / 6 * math.pi) and math.degrees(
            mouse_angle) <= math.degrees(2 * math.pi):
        return 5
    elif (math.degrees(mouse_angle)) > math.degrees(0) and math.degrees(mouse_angle) <= math.degrees(
            1 / 6 * math.pi):
        return 5




def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True
