# DNA module contains the possible fur colors and movements of the doggo.
# This is the sprites configurations.

from __future__ import annotations

import random

from enum import IntEnum
from enum import auto

from doggo.mind import Direction
from doggo.mind import StateID


SPRITE_SIZE = (9, 8)  # rows, columns in the sprite sheet
SPRITE_DIRECTION = Direction.LEFT  # Default direction of the sprite
# Number of sprites per state in the sprite sheet and row index
SPRITE_CONF_PER_STATE = {
    StateID.IDLE: (6, 0),
    StateID.IDLE_AND_BARK: (8, 0),
    StateID.WALK: (8, 4),
    StateID.WALK_AND_BARK: (8, 6),
    StateID.SIT: (6, 1),
    StateID.SIT_AND_BARK: (8, 1),
    StateID.LIE_DOWN: (6, 2),
    StateID.LIE_DOWN_AND_BARK: (8, 2),
    StateID.RUN: (8, 3),
    StateID.RUN_AND_BARK: (8, 5),
    StateID.STAND: (6, 7),
    StateID.STAND_AND_BARK: (8, 7),
    StateID.SLEEP: (4, 8),
}


class Fur(IntEnum):
    """The possible fur colors of the doggo."""

    DARK_BROWN = 0
    LIGHT_BROWN = auto()
    GREY = auto()
    BLUE = auto()
    RED_BROWN = auto()
    WHITE = auto()
    WHITE_WITH_BROWN_SPOTS = auto()
    DARK_BROWN_WITH_GREY_SPOTS = auto()
    WHITE_WITH_GREY_SPOTS = auto()
    BLUE_WITH_BROWN_SPOTS = auto()
    LIGHT_BROWN_WITH_WHITE_SPOTS = auto()
    ORANGE = auto()

    @classmethod
    def random(cls) -> Fur:
        """Return a random fur color."""
        return random.choice(list(cls))
