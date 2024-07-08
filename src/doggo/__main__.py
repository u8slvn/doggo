from __future__ import annotations

import pygame as pg

from doggo.config import DOGGO_STATES
from doggo.config import SPRITE_CONF_PER_STATE
from doggo.config import SPRITE_DIRECTION
from doggo.config import SPRITE_SIZE
from doggo.config import WORLD_FLOOR
from doggo.config import WORLD_FPS
from doggo.config import WORLD_HEIGHT
from doggo.config import WORLD_WIDTH
from doggo.dog.body import Body
from doggo.dog.body import Fur
from doggo.dog.brain import Brain
from doggo.dog.dog import Dog
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

    brain = Brain(states=DOGGO_STATES)
    body = Body(
        fur=Fur.random(),
        sprite_size=SPRITE_SIZE,
        default_direction=SPRITE_DIRECTION,
        sprite_conf_per_state=SPRITE_CONF_PER_STATE,
    )
    dog = Dog(brain=brain, body=body, world_floor=WORLD_FLOOR, world_width=WORLD_WIDTH)

    world = World(screen=screen, dog=dog, fps=WORLD_FPS)
    world.start()


if __name__ == "__main__":
    run()
