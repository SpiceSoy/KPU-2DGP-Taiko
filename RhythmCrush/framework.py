# 메인 프레임워크
import time
from .utill.input_manager import *
from RhythmCrush.game_scene import game_map


class Framework:
    def __init__(self, w=int(1440), h=int(810)):
        self.w = w
        self.h = h
        self.is_active = False
        self.prev_time = 0
        self.now_time = 0
        self.game_scene = game_map.NotePlayScene(self, "Resource/Map/FirstTest/Camellia - Exit This Earth's Atomosphere (Camellia's PLANETARY200STEP Remix) (nyanmi-1828) [Satellite].osu")
        self.input_manager = InputHandlerManager(self)
        self.input_manager.add_handler(pico2d.SDL_KEYDOWN, self.key_end_handler(pico2d.SDLK_ESCAPE))

    def start(self):
        self.is_active = True
        print(self.w)
        print(self.h)
        pico2d.open_canvas(self.w, self.h)
        self.game_scene.load()
        self.game_scene.start()
        self.prev_time = time.time()
        self.now_time = time.time()

    def loop(self):
        while self.is_active:
            self.prev_time = self.now_time
            self.now_time = time.time()
            delta_time = self.now_time - self.prev_time
            self.update(delta_time)
            self.draw()

    def update(self, delta_time):
        self.input_manager.handle_event()
        self.game_scene.update(delta_time)
        # self.player.update(delta_time)

    def draw(self):
        pico2d.clear_canvas()
        self.game_scene.draw()
        # self.player.draw()
        pico2d.update_canvas()

    def key_end_handler(self, key):
        def ret(event):
            if event.key == key:
                self.is_active = False
            pass
        return ret
