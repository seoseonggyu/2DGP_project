from pico2d import *

MAP1_WIDTH, MAP1_HEIGHT = 564, 818
open_canvas(500,500)
walking = load_image('walking_sheet.png')
map1 = load_image('map1.jpg')

dir = 0
dir2 = 0
move = False
running = True
x = 70
y = 818-90
frame = 0
way = 0


def handle_events():
    global running
    global dir
    global dir2
    global way
    global frame
    global move

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            move = True
            if event.key == SDLK_d:
                dir += 1
                way = 0
            if event.key == SDLK_a:
                dir -= 1
                way = 1
            if event.key == SDLK_w:
                dir2 += 1
                way = 4
            if event.key == SDLK_s:
                dir2 -= 1
                way = 5
            if dir > 0 and dir2 > 0:
                way = 2
            if dir < 0 and dir2 > 0:
                way = 3
            if dir < 0 and dir2 < 0:
                way = 1
            if dir > 0 and dir2 < 0:
                way = 0

            if event.key == SDLK_ESCAPE:
                running = False

        if event.type == SDL_KEYUP:
            if event.key == SDLK_d:
                if dir2 > 0:
                    dir -= 1
                    way = 4
                elif dir2 < 0:
                    way = 5
                    dir -= 1
                else:
                    way = 6
                    frame = -1
                    dir -= 1
                    move = False
            elif event.key == SDLK_w:
                if dir > 0:
                    dir2 -= 1
                    way = 0
                elif dir < 0:
                    dir2 -= 1
                    way = 1
                else:
                    way = 6
                    frame = 1
                    dir2 -= 1
                    move = False
            elif event.key == SDLK_a:
                if dir2 > 0:
                    dir += 1
                    way = 4
                elif dir2 < 0:
                    way = 5
                    dir += 1
                else:
                    way = 6
                    frame = 2
                    dir += 1
                    move = False
            elif event.key == SDLK_s:
                if dir > 0:
                    dir2 += 1
                    way = 0
                elif dir < 0:
                    dir2 += 1
                    way = 1
                else:
                    way = 6
                    frame = 0
                    dir2 += 1
                    move = False

def map_events():
    map1.draw(x, y)

if __name__ == "__main__":
    while running:
        if move == True:
            clear_canvas()
            map_events()
            walking.clip_draw(frame * 40, 42 * way, 40, 42, x, y, 50, 50)
            update_canvas()
            handle_events()
            frame = (frame + 1) % 6
            x += dir * 5
            y += dir2 * 5
        else:
            clear_canvas()
            map1.draw(MAP1_WIDTH // 2, MAP1_HEIGHT // 2)
            walking.clip_draw(frame * 40, 42 * way, 40, 42, x, y, 50, 50)
            update_canvas()
            handle_events()

        delay(0.03)

    close_canvas()