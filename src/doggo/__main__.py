from __future__ import annotations

import pygame as pg

from doggo import mind
from doggo.body import Body
from doggo.body import Fur
from doggo.brain import Brain
from doggo.brain import StateID
from doggo.dog import Dog
from doggo.world import World


def run() -> None:
    pg.init()
    pg.display.set_caption("Doggo")
    screen = pg.display.set_mode((300, 100))

    states_sprites_config = {
        StateID.IDLE: (0, 0),
        StateID.WALK: (1, 1),
        StateID.RUN: (2, 2),
        StateID.EAT: (3, 3),
        StateID.SIT: (4, 4),
    }

    brain = Brain(states=mind.STATES)
    body = Body(
        fur=Fur.random(),
        sprite_sheet_size=(9, 8),
        states_sprites_config=states_sprites_config,
    )
    dog = Dog(brain=brain, body=body)
    world = World(screen=screen, dog=dog)
    world.start()


if __name__ == "__main__":
    run()
