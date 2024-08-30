from __future__ import annotations

import pygame as pg

from doggo import ASSETS_PATH
from doggo import config
from doggo.config import COMPILED_ENV
from doggo.config import WIN
from doggo.world import World


if COMPILED_ENV and WIN:
    # Import the PyInstaller splash screen module only if the app is compiled and
    # running on Windows.
    import pyi_splash


def run() -> None:
    """Run Doggo.

    Initialize the pygame and start the world.
    """
    pg.init()

    world = World(
        title=config.WORLD_TITLE,
        size=(config.WORLD_WIDTH, config.WORLD_HEIGHT),
        icon=ASSETS_PATH.joinpath("icon-42.png"),
        fps=config.WORLD_FPS,
    )

    if COMPILED_ENV and WIN:
        pyi_splash.close()

    try:
        world.start()
    except KeyboardInterrupt:
        world.stop()


if __name__ == "__main__":
    run()
