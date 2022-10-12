from pico2d import *

open_canvas(1200,1000 )
# map1 = load_image('map1.png')
walking = load_image('walking_sheet.png')

dir = 0
dir2 = 0
move = False

x = 800 // 2
y = 600 // 2
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

running = True

while running:
     if move == True:
         clear_canvas()
         walking.clip_draw(frame * 40, 42 * way, 40, 42, x, y, 250, 250)
         update_canvas()
         handle_events()
         frame = (frame + 1) % 6
         x += dir * 5
         y += dir2 * 5
     else:
         clear_canvas()
         walking.clip_draw(frame * 40, 42 * way, 40, 42, x, y, 250, 250)
         update_canvas()
         handle_events()

     delay(0.1)

close_canvas()



