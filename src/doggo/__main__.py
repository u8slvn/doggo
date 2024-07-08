from __future__ import annotations

import pygame as pg

from doggo import dna
from doggo import mind
from doggo.body import Body
from doggo.brain import Brain
from doggo.config import WORLD_FLOOR_LEVEL
from doggo.config import WORLD_HEIGHT
from doggo.config import WORLD_WIDTH
from doggo.dog import Dog
from doggo.world import World


def run() -> None:
    pg.init()
    pg.display.set_caption("Doggo")
    screen = pg.display.set_mode((WORLD_WIDTH, WORLD_HEIGHT))

    brain = Brain(states=mind.STATES)
    body = Body(
        fur=dna.Fur.random(),
        sprite_size=dna.SPRITE_SIZE,
        default_direction=dna.SPRITE_DIRECTION,
        sprite_conf_per_state=dna.SPRITE_CONF_PER_STATE,
    )
    dog = Dog(brain=brain, body=body, y=WORLD_FLOOR_LEVEL)
    world = World(screen=screen, dog=dog)
    world.start()


if __name__ == "__main__":
    run()
