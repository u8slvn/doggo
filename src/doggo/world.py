from __future__ import annotations

import sys
import time

from typing import TYPE_CHECKING

import pygame as pg

from loguru import logger

from doggo.dog.dog import Dog
from doggo.prepare import build_dog
from doggo.prepare import build_landscape
from doggo.ui import DraggableWindow


if TYPE_CHECKING:
    from pathlib import Path


class World:
    """The world where the dog lives.

    It contains the game loop and the main logic of the game.
    """

    def __init__(
        self,
        title: str,
        size: tuple[int, int],
        icon: Path,
        fps: int = 60,
        fullscreen: bool = False,
    ) -> None:
        self.window: pg.window.Window = pg.window.Window(
            title=title,
            size=size,
            borderless=True,
            always_on_top=True,
            fullscreen=fullscreen,
        )
        self.window_surf: pg.Surface = self.window.get_surface()
        self.screen: pg.Surface = pg.Surface(size=size)
        self.window.set_icon(pg.image.load(icon).convert_alpha())
        self.draggable: DraggableWindow = DraggableWindow(window=self.window)
        self.fullscreen: bool = fullscreen
        self.fps: int = fps
        self.clock: pg.time.Clock = pg.time.Clock()
        self.running: bool = False
        self.dt: float = 0.0
        self.prev_time: float = time.time()
        self.landscape = build_landscape()
        self.dog: Dog = build_dog()

    def get_screen(self) -> pg.Surface:
        """Adapt the screen to the window size if fullscreen.

        Didn't respect the aspect ratio, to use only if the display ratio is the same
        as the default window size one.
        """
        if self.fullscreen:
            return pg.transform.scale(self.screen, self.window_surf.get_size())

        return self.screen

    def process_inputs(self) -> None:
        """Process the inputs of the world."""
        for event in pg.event.get():
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                self.running = False

            if not self.fullscreen:
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
        self.landscape.background.draw(screen=self.screen)
        self.dog.draw(screen=self.screen)
        self.landscape.foreground.draw(screen=self.screen)
        self.window_surf.blit(self.get_screen(), (0, 0))
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
        sys.exit()
