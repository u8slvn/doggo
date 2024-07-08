from __future__ import annotations

import pygame as pg

import doggo.config

from doggo.config import WORLD_FLOOR_LEVEL
from doggo.config import WORLD_HEIGHT
from doggo.config import WORLD_WIDTH
from doggo.dog.body import Body
from doggo.dog.body import Fur
from doggo.dog.brain import Brain
from doggo.dog.dog import Dog
from doggo.world import World


def run() -> None:
    pg.init()
    pg.display.set_caption("Doggo")
    screen = pg.display.set_mode((WORLD_WIDTH, WORLD_HEIGHT))

    brain = Brain(states=doggo.config.DOGGO_STATES)
    body = Body(
        fur=Fur.random(),
        sprite_size=doggo.config.SPRITE_SIZE,
        default_direction=doggo.config.SPRITE_DIRECTION,
        sprite_conf_per_state=doggo.config.SPRITE_CONF_PER_STATE,
    )
    dog = Dog(brain=brain, body=body, y=WORLD_FLOOR_LEVEL)
    world = World(screen=screen, dog=dog)
    world.start()


if __name__ == "__main__":
    run()
