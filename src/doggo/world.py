from __future__ import annotations

import time

import pygame as pg


class World:
    def __init__(self, width: int, height: int, fps: int = 60) -> None:
        pg.display.set_caption("Doggo")
        pg.display.set_mode((width, height))
        self.screen: pg.Surface = pg.Surface((width, height))
        self.fps: int = fps
        self.clock: pg.time.Clock = pg.time.Clock()
        self.running: bool = False
        self.dt: float = 0.0
        self.prev_time: float = 0.0

    def process_input(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def get_dt(self) -> None:
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def update(self) -> None:
        pass

    def render(self) -> None:
        self.screen.fill((255, 0, 255))

    def start(self) -> None:
        pg.init()
        self.running = True

        while self.running:
            self.get_dt()
            self.process_input()
            self.update()
            self.render()
            self.clock.tick(self.fps)

        self.stop()

    @staticmethod
    def stop() -> None:
        pg.quit()
        exit()
