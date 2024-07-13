from __future__ import annotations

import pygame as pg

from doggo import config
from doggo.world import World


def run() -> None:
    """Run Doggo.

    Initialize the pygame and start the world.
    """
    pg.init()

    world = World(
        title=config.WORLD_TITLE,
        size=(config.WORLD_WIDTH, config.WORLD_HEIGHT),
        fps=config.WORLD_FPS,
    )
    world.start()


if __name__ == "__main__":
    run()
