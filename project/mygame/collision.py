

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def map_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb2()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a < left_b: return True
    if right_a > right_b: return True
    if bottom_a < bottom_b: return True
    if top_a > top_b: return True

    return False