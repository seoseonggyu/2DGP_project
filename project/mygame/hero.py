from pico2d import *
import game_framework
import game_world


# Run Speed
PIXEL_PER_METER = (10.0 / 0.01) # 10 pixel 30 cm
RUN_SPEED_KMPH = 1 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Action Speed
TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6


#2 이벤트 정의
Mouse_Down, DD, AD, WD, SD, DU, AU, WU, SU = range(9)


key_event_table = {
    (SDL_KEYDOWN, SDLK_d): DD,
    (SDL_KEYDOWN, SDLK_a): AD,
    (SDL_KEYDOWN, SDLK_w): WD,
    (SDL_KEYDOWN, SDLK_s): SD,
    (SDL_KEYUP,   SDLK_d): DU,
    (SDL_KEYUP,   SDLK_a): AU,
    (SDL_KEYUP,   SDLK_w): WU,
    (SDL_KEYUP,   SDLK_s): SU
}

class IDLE:
    def enter(self, event): # 상태에 들어갈 때 행하는 액션
        print('enter idle')
        self.dir = 0
        self.dir2 = 0
        pass
    def exit(self): # 상태를 나올 때 행하는 액션 , 고개 들기
        print('exit idle')
        pass
    def do(self): # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = self.face_dir
        pass

    # 외부에서 전달되는 self
    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, 120, 120)
        self.cursor.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, 120, 120)


class RUN:
    @staticmethod
    def enter(self, event):
        print('enter RUN')
        if event == DD:
            self.way = 0
            self.dir += 1

        elif event == AD:
            self.way = 1
            self.dir -= 1

        elif event == WD:
            self.way = 4
            self.dir2 += 1

        elif event == SD:
            self.way = 5
            self.dir2 -= 1

        if event == DU:
            if self.dir2 > 0:
                self.way = 4
                self.dir -= 1
            elif self.dir2 < 0:
                self.way = 5
                self.dir -= 1
            elif self.dir < 0:
                self.way = 1
                self.dir = -1

        elif event == AU:
            if self.dir2 > 0:
                self.way = 4
                self.dir += 1
            elif self.dir2 < 0:
                self.way = 5
                self.dir += 1
            elif self.dir > 0:
                self.way = 0
                self.dir = 1

        elif event == WU:
            if self.dir > 0:
                self.way = 0
                self.dir2 -= 1
            elif self.dir < 0:
                self.way = 1
                self.dir2 -= 1
            elif self.dir2 < 0:
                self.way = 5
                self.dir2 = -1

        elif event == SU:
            if self.dir > 0:
                self.way = 0
                self.dir2 += 1
            elif self.dir < 0:
                self.way = 1
                self.dir2 += 1
            elif self.dir2 > 0:
                self.way = 4
                self.dir2 = 1

    @staticmethod
    def exit(self):
        print('exit RUN')
        self.face_dir = self.way
        pass

    @staticmethod
    def do(self): # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.dir2 * RUN_SPEED_PPS * game_framework.frame_time


        self.x = pico2d.clamp(0, self.x, 800)
        self.y = pico2d.clamp(0, self.y, 600)

    @staticmethod
    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, 120, 120)
        self.cursor.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, 120, 120)

class RUN2:
    @staticmethod
    def enter(self, event):
        print('enter RUN2')
        if event == DD:
            if self.dir2 > 0:
                self.way = 2
                self.dir += 1
            elif self.dir2 < 0:
                self.way = 0
                self.dir += 1
            else:
                self.dir = 1
                self.way = 0

        elif event == AD:
            if self.dir2 > 0:
                self.way = 3
                self.dir -= 1
            elif self.dir2 < 0:
                self.way = 1
                self.dir -= 1
            else:
                self.dir = -1
                self.way = 1

        elif event == WD:
            if self.dir > 0:
                self.way = 2
                self.dir2 += 1
            elif self.dir < 0:
                self.way = 3
                self.dir2 += 1
            else:
                self.dir2 = 1
                self.way = 4

        elif event == SD:
            if self.dir > 0:
                self.way = 0
                self.dir2 -= 1
            elif self.dir < 0:
                self.way = 1
                self.dir2 -= 1
            else:
                self.dir2 = -1
                self.way = 5

    @staticmethod
    def exit(self):
        print('exit RUN2')
        pass

    @staticmethod
    def do(self): # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.dir2 * RUN_SPEED_PPS * game_framework.frame_time

        self.x = pico2d.clamp(0, self.x, 800)
        self.y = pico2d.clamp(0, self.y, 600)

    @staticmethod
    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, 120, 120)
        self.cursor.clip_draw(int(self.frame) * 40, 42 * self.way, 40, 42, self.x, self.y, 120, 120)

next_stage = {
    IDLE:  {DD: RUN,  AD: RUN,  WD: RUN,  SD: RUN,  DU: IDLE,  AU: IDLE,  WU: IDLE,  SU: IDLE, Mouse_Down: IDLE},
    RUN:   {DD: RUN2, AD: RUN2, WD: RUN2, SD: RUN2, DU: IDLE,  AU: IDLE,  WU: IDLE,  SU: IDLE, Mouse_Down: IDLE},
    RUN2:  {DD: IDLE, AD: IDLE, WD: IDLE, SD: IDLE, DU: RUN,   AU: RUN,   WU: RUN,   SU: RUN, Mouse_Down: IDLE}
}

class character:

    def __init__(self):
        self.x, self.y = 100, 100 # 캐릭터 좌표
        # self.mouse_x, self.mouse_y = 600, 400 # 마우스 좌표
        self.frame = 0
        self.way = 0
        self.dir, self.dir2 = 0, 0
        self.face_dir = 0

        self.image = pico2d.load_image('character_sheet.png')
        self.cursor = pico2d.load_image('gun_cursor.png')
        # self.life = pico2d.load_image('life.png')

        self.q = []  # 이벤트 큐 초기화
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.q:
            event = self.q.pop()
            self.cur_state.exit(self) # 현재 상태를 나가야되고,
            self.cur_state = next_stage[self.cur_state][event] # 다음 상태를 구한다
            self.cur_state.enter(self, event)

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        # if event.type == pico2d.SDL_MOUSEMOTION: # 마우스
        #     mouse_x, mouse_y = event.x, 800 - 1 - event.y

        # if event.type == pico2d.SDL_MOUSEBUTTONDOWN:
        #     if event.button == pico2d.SDL_BUTTON_LEFT:
        #         mouse_x, mouse_y = event.x, 800 - 1 - event.y
        #         bulletXY.append(bullet(mouse_x, mouse_y, hero.x, hero.y))

    def draw(self):
        self.cur_state.draw(self)
        # self.cursor.draw(self.mouse_x, self.mouse_y)