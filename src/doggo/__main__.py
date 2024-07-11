from __future__ import annotations

import pygame as pg

from doggo.config import WORLD_FPS
from doggo.config import WORLD_HEIGHT
from doggo.config import WORLD_WIDTH
from doggo.prepare import build_dog
from doggo.prepare import build_landscape
from doggo.world import World


def run() -> None:
    """Run Doggo.

    Initialize the game and start the world.
    """
    pg.init()
    pg.display.set_caption("Doggo")
    screen = pg.display.set_mode((WORLD_WIDTH, WORLD_HEIGHT))

    # Workaround to make the window always on top
    window = pg.Window.from_display_module()
    window.always_on_top = True

    dog = build_dog()
    landscape = build_landscape()

    world = World(
        screen=screen,
        dog=dog,
        landscape=landscape,
        fps=WORLD_FPS,
    )
    world.start()


if __name__ == "__main__":
    run()
