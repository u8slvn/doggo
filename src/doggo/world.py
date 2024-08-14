from __future__ import annotations

import time

import pygame as pg

from loguru import logger

from doggo.dog.dog import Dog
from doggo.prepare import build_bg_landscape
from doggo.prepare import build_dog
from doggo.prepare import build_fg_landscape
from doggo.ui import DraggableWindow


class World:
    """The world where the dog lives.

    It contains the game loop and the main logic of the game.
    """

    def __init__(self, title: str, size: tuple[int, int], fps: int = 60) -> None:
        self.window: pg.window.Window = pg.window.Window(
            title=title,
            size=size,
            borderless=True,
            always_on_top=True,
        )
        self.screen: pg.Surface = self.window.get_surface()
        self.draggable: DraggableWindow = DraggableWindow(window=self.window)
        self.fps: int = fps
        self.clock: pg.time.Clock = pg.time.Clock()
        self.running: bool = False
        self.dt: float = 0.0
        self.prev_time: float = time.time()

        self.bg_landscape = build_bg_landscape()
        self.dog: Dog = build_dog()
        self.fg_landscape = build_fg_landscape()

    def process_inputs(self) -> None:
        """Process the inputs of the world."""
        for event in pg.event.get():
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                self.running = False

            self.draggable.process_event(event=event)

    def get_dt(self) -> None:
        """Calculate the delta time."""
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def update(self) -> None:
        """Update the world."""
        self.dog.update(dt=self.dt)

    def render(self) -> None:
        """Render the world."""
        self.screen.fill((135, 206, 235))
        self.bg_landscape.render(surface=self.screen)
        self.dog.render(surface=self.screen)
        self.fg_landscape.render(surface=self.screen)
        self.window.flip()

    def start(self) -> None:
        """Start the world"""
        logger.info("World started. Dog is awake.")
        logger.info(
            f"Dog parachuted in the world and start to {self.dog.current_state} "
            f"for {self.dog.brain.current_state.countdown}s."
        )

        self.running = True

        while self.running:
            self.get_dt()
            self.process_inputs()
            self.update()
            self.render()
            self.clock.tick(self.fps)

        self.stop()

    @staticmethod
    def stop() -> None:
        """Stop the world."""
        pg.quit()
        logger.info("World stopped. Dog is going to sleep.")
        exit()
