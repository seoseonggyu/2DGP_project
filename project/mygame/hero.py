import pico2d

#2 이벤트 정의
RD, LD, RU, LU = range(4)

key_event_table = {
    (pico2d.SDL_KEYDOWN, pico2d.SDLK_d): RD,
    (pico2d.SDL_KEYDOWN, pico2d.SDLK_a): LD,
    (pico2d.SDL_KEYUP, pico2d.SDLK_d): RU,
    (pico2d.SDL_KEYUP, pico2d.SDLK_a): LU
}

class IDLE:
    def enter(self, event): # 상태에 들어갈 때 행하는 액션
        print('enter idle')
        self.dir = 0
        pass
    def exit(self): # 상태를 나올 때 행하는 액션 , 고개 들기
        print('exit idle')
        pass
    def do(self): # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = 1 #(self.frame + 1) % 8
        pass

    # 외부에서 전달되는 self
    def draw(self):
        self.image.clip_draw(self.frame * 40, 42 * self.way, 40, 42, self.x, self.y, 120, 120)


class RUN:
    @staticmethod
    def enter(self, event):
        if event == RD:
            self.way = 0
            self.dir += 1
        elif event == LD:
            self.way = 1
            self.dir -= 1
        elif event == RU:
            self.way = 0
            self.dir -= 1
        elif event == LU:
            self.way = 1
            self.dir += 1


    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self): # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + 1) % 6



        self.x += 5 * self.dir

        print("self.dir = ", self.dir)
        print("self.way = ", self.way)

        self.x = pico2d.clamp(0, self.x, 800)

        pass

    @staticmethod
    def draw(self):
        self.image.clip_draw(self.frame * 40, 42 * self.way, 40, 42, self.x, self.y, 120, 120)


next_stage = {
    IDLE:  {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN},
    RUN:   {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE}
}

class character:
    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

        # global dir
        # global dir2
        # global way
        # global frame
        # global move

    def __init__(self):
        self.x, self.y = 0, 90 # 캐릭터 좌표
        # self.mouse_x, self.mouse_y = 600, 400 # 마우스 좌표
        self.frame = 0
        self.way = 0
        self.dir = 0
        # self.dir2 = 0
        self.face_dir = 1
        self.image = pico2d.load_image('character_sheet.png')
        # self.cursor = pico2d.load_image('gun_cursor.png')
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

        # self.y += self.dir2 * 5
        # pico2d.delay(0.01)

        # if self.x <= 0:
        #     self.x = 0
        # if self.x >= 1200:
        #     self.x = 1200
        # if self.y <= 0:
        #     self.y = 0
        # if self.y >= 800:
        #     self.y = 800

    def update2(self):
        pass

    def draw(self):
        self.cur_state.draw(self)
        # self.cursor.draw(self.mouse_x, self.mouse_y)