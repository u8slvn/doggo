from __future__ import annotations

import os

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
    # Check if the app should run in fullscreen mode.
    fullscreen = os.getenv("DOGGO_FULLSCREEN", "False").lower() in ("1", "true")

    pg.init()

    world = World(
        title=config.WORLD_TITLE,
        size=(config.WORLD_WIDTH, config.WORLD_HEIGHT),
        icon=ASSETS_PATH.joinpath("icon.png"),
        fps=config.WORLD_FPS,
        fullscreen=fullscreen,
    )

    if COMPILED_ENV and WIN:
        pyi_splash.close()

    try:
        world.start()
    except KeyboardInterrupt:
        world.stop()


if __name__ == "__main__":
    run()
