from __future__ import annotations

import time

import pygame as pg

from loguru import logger

from doggo.config import WORLD_GROUND
from doggo.dog.dog import Dog
from doggo.landscape import Ground
from doggo.ui import DraggableWindow


class World:
    """The world where the dog lives.

    It contains the game loop and the main logic of the game.
    """

    def __init__(self, screen: pg.Surface, dog: Dog, fps: int = 60) -> None:
        self.draggable_window: DraggableWindow = DraggableWindow()
        self.screen: pg.Surface = screen
        self.fps: int = fps
        self.clock: pg.time.Clock = pg.time.Clock()
        self.running: bool = False
        self.dt: float = 0.0
        self.prev_time: float = time.time()
        self.dog: Dog = dog
        self.ground = Ground(height=WORLD_GROUND)

    def process_inputs(self) -> None:
        """Process the inputs of the world."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            self.draggable_window.process_event(event=event)

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
        self.dog.render(surface=self.screen)
        self.ground.render(surface=self.screen)
        pg.display.update()

    def start(self) -> None:
        """Start the world"""
        logger.info("World started. Doggo is awake.")
        logger.info(
            f"Doggo parachuted in the world and start to {self.dog.current_state} "
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
        logger.info("World stopped. Doggo is going to sleep.")
        exit()
