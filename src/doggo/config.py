from __future__ import annotations

from doggo.dog.brain import Direction
from doggo.dog.brain import State
from doggo.dog.brain import StateID


# --- World configuration ---

WORLD_FPS = 60
WORLD_WIDTH = 350
WORLD_HEIGHT = 100
WORLD_GROUND_HEIGHT = 15  # The size of the floor in the world.
WORLD_GROUND = (
    WORLD_HEIGHT - WORLD_GROUND_HEIGHT
)  # The floor level in the world, where the doggo can walk on.

# --- Doggo sprite sheet configuration ---

SPRITE_SIZE = (9, 8)  # rows, columns in the sprite sheet
SPRITE_DIRECTION = Direction.LEFT  # Default direction of the sprite
# For each state, (number of frames, row index in the sprite sheet)
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

# --- Doggo states configuration ---

DOGGO_STATES = [
    State(
        id=StateID.IDLE,
        transitions={
            StateID.IDLE: 0.1,
            StateID.IDLE_AND_BARK: 0.1,
            StateID.WALK: 0.1,
            StateID.WALK_AND_BARK: 0.1,
            StateID.SIT: 0.1,
            StateID.SIT_AND_BARK: 0.1,
            StateID.LIE_DOWN: 0.1,
            StateID.LIE_DOWN_AND_BARK: 0.0,
            StateID.RUN: 0.1,
            StateID.RUN_AND_BARK: 0.1,
            StateID.STAND: 0.05,
            StateID.STAND_AND_BARK: 0.05,
            StateID.SLEEP: 0.0,
        },
        time_range=(2, 10),
        speed=0,
    ),
    State(
        id=StateID.IDLE_AND_BARK,
        transitions={
            StateID.IDLE: 0.1,
            StateID.IDLE_AND_BARK: 0.1,
            StateID.WALK: 0.15,
            StateID.WALK_AND_BARK: 0.1,
            StateID.SIT: 0.15,
            StateID.SIT_AND_BARK: 0.1,
            StateID.LIE_DOWN: 0.0,
            StateID.LIE_DOWN_AND_BARK: 0.0,
            StateID.RUN: 0.1,
            StateID.RUN_AND_BARK: 0.05,
            StateID.STAND: 0.1,
            StateID.STAND_AND_BARK: 0.05,
            StateID.SLEEP: 0.0,
        },
        time_range=(2, 10),
        speed=0,
    ),
    State(
        id=StateID.WALK,
        transitions={
            StateID.IDLE: 0.1,
            StateID.IDLE_AND_BARK: 0.1,
            StateID.WALK: 0.1,
            StateID.WALK_AND_BARK: 0.1,
            StateID.SIT: 0.15,
            StateID.SIT_AND_BARK: 0.1,
            StateID.LIE_DOWN: 0.0,
            StateID.LIE_DOWN_AND_BARK: 0.0,
            StateID.RUN: 0.2,
            StateID.RUN_AND_BARK: 0.05,
            StateID.STAND: 0.05,
            StateID.STAND_AND_BARK: 0.05,
            StateID.SLEEP: 0.0,
        },
        time_range=(2, 20),
    ),
    State(
        id=StateID.WALK_AND_BARK,
        transitions={
            StateID.IDLE: 0.1,
            StateID.IDLE_AND_BARK: 0.1,
            StateID.WALK: 0.1,
            StateID.WALK_AND_BARK: 0.1,
            StateID.SIT: 0.15,
            StateID.SIT_AND_BARK: 0.1,
            StateID.LIE_DOWN: 0.0,
            StateID.LIE_DOWN_AND_BARK: 0.0,
            StateID.RUN: 0.2,
            StateID.RUN_AND_BARK: 0.05,
            StateID.STAND: 0.05,
            StateID.STAND_AND_BARK: 0.05,
            StateID.SLEEP: 0.0,
        },
        time_range=(3, 10),
    ),
    State(
        id=StateID.SIT,
        transitions={
            StateID.IDLE: 0.1,
            StateID.IDLE_AND_BARK: 0.05,
            StateID.WALK: 0.1,
            StateID.WALK_AND_BARK: 0.05,
            StateID.SIT: 0.1,
            StateID.SIT_AND_BARK: 0.05,
            StateID.LIE_DOWN: 0.25,
            StateID.LIE_DOWN_AND_BARK: 0.05,
            StateID.RUN: 0.05,
            StateID.RUN_AND_BARK: 0.0,
            StateID.STAND: 0.05,
            StateID.STAND_AND_BARK: 0.05,
            StateID.SLEEP: 0.1,
        },
        time_range=(5, 15),
        speed=0,
    ),
    State(
        id=StateID.SIT_AND_BARK,
        transitions={
            StateID.IDLE: 0.1,
            StateID.IDLE_AND_BARK: 0.05,
            StateID.WALK: 0.1,
            StateID.WALK_AND_BARK: 0.05,
            StateID.SIT: 0.1,
            StateID.SIT_AND_BARK: 0.05,
            StateID.LIE_DOWN: 0.25,
            StateID.LIE_DOWN_AND_BARK: 0.05,
            StateID.RUN: 0.05,
            StateID.RUN_AND_BARK: 0.0,
            StateID.STAND: 0.05,
            StateID.STAND_AND_BARK: 0.05,
            StateID.SLEEP: 0.1,
        },
        time_range=(5, 10),
        speed=0,
    ),
    State(
        id=StateID.LIE_DOWN,
        transitions={
            StateID.IDLE: 0.1,
            StateID.IDLE_AND_BARK: 0.1,
            StateID.WALK: 0.1,
            StateID.WALK_AND_BARK: 0.1,
            StateID.SIT: 0.2,
            StateID.SIT_AND_BARK: 0.05,
            StateID.LIE_DOWN: 0.1,
            StateID.LIE_DOWN_AND_BARK: 0.05,
            StateID.RUN: 0.1,
            StateID.RUN_AND_BARK: 0.0,
            StateID.STAND: 0.0,
            StateID.STAND_AND_BARK: 0.0,
            StateID.SLEEP: 0.1,
        },
        time_range=(10, 20),
        speed=0,
    ),
    State(
        id=StateID.LIE_DOWN_AND_BARK,
        transitions={
            StateID.IDLE: 0.1,
            StateID.IDLE_AND_BARK: 0.1,
            StateID.WALK: 0.1,
            StateID.WALK_AND_BARK: 0.1,
            StateID.SIT: 0.2,
            StateID.SIT_AND_BARK: 0.05,
            StateID.LIE_DOWN: 0.1,
            StateID.LIE_DOWN_AND_BARK: 0.05,
            StateID.RUN: 0.1,
            StateID.RUN_AND_BARK: 0.0,
            StateID.STAND: 0.0,
            StateID.STAND_AND_BARK: 0.0,
            StateID.SLEEP: 0.1,
        },
        time_range=(5, 10),
        speed=0,
    ),
    State(
        id=StateID.RUN,
        transitions={
            StateID.IDLE: 0.35,
            StateID.IDLE_AND_BARK: 0.05,
            StateID.WALK: 0.3,
            StateID.WALK_AND_BARK: 0.05,
            StateID.SIT: 0.0,
            StateID.SIT_AND_BARK: 0.0,
            StateID.LIE_DOWN: 0.0,
            StateID.LIE_DOWN_AND_BARK: 0.0,
            StateID.RUN: 0.2,
            StateID.RUN_AND_BARK: 0.05,
            StateID.STAND: 0.0,
            StateID.STAND_AND_BARK: 0.0,
            StateID.SLEEP: 0.0,
        },
        time_range=(3, 15),
        speed=100,
    ),
    State(
        id=StateID.RUN_AND_BARK,
        transitions={
            StateID.IDLE: 0.35,
            StateID.IDLE_AND_BARK: 0.05,
            StateID.WALK: 0.3,
            StateID.WALK_AND_BARK: 0.05,
            StateID.SIT: 0.0,
            StateID.SIT_AND_BARK: 0.0,
            StateID.LIE_DOWN: 0.0,
            StateID.LIE_DOWN_AND_BARK: 0.0,
            StateID.RUN: 0.2,
            StateID.RUN_AND_BARK: 0.05,
            StateID.STAND: 0.0,
            StateID.STAND_AND_BARK: 0.0,
            StateID.SLEEP: 0.0,
        },
        time_range=(3, 15),
        speed=100,
    ),
    State(
        id=StateID.STAND,
        transitions={
            StateID.IDLE: 0.1,
            StateID.IDLE_AND_BARK: 0.1,
            StateID.WALK: 0.1,
            StateID.WALK_AND_BARK: 0.1,
            StateID.SIT: 0.1,
            StateID.SIT_AND_BARK: 0.05,
            StateID.LIE_DOWN: 0.1,
            StateID.LIE_DOWN_AND_BARK: 0.05,
            StateID.RUN: 0.1,
            StateID.RUN_AND_BARK: 0.0,
            StateID.STAND: 0.05,
            StateID.STAND_AND_BARK: 0.05,
            StateID.SLEEP: 0.1,
        },
        time_range=(3, 10),
        speed=0,
    ),
    State(
        id=StateID.STAND_AND_BARK,
        transitions={
            StateID.IDLE: 0.1,
            StateID.IDLE_AND_BARK: 0.1,
            StateID.WALK: 0.1,
            StateID.WALK_AND_BARK: 0.1,
            StateID.SIT: 0.1,
            StateID.SIT_AND_BARK: 0.05,
            StateID.LIE_DOWN: 0.1,
            StateID.LIE_DOWN_AND_BARK: 0.05,
            StateID.RUN: 0.1,
            StateID.RUN_AND_BARK: 0.0,
            StateID.STAND: 0.05,
            StateID.STAND_AND_BARK: 0.05,
            StateID.SLEEP: 0.1,
        },
        time_range=(3, 10),
        speed=0,
    ),
    State(
        id=StateID.SLEEP,
        transitions={
            StateID.IDLE: 0.1,
            StateID.IDLE_AND_BARK: 0.1,
            StateID.WALK: 0.0,
            StateID.WALK_AND_BARK: 0.0,
            StateID.SIT: 0.3,
            StateID.SIT_AND_BARK: 0.1,
            StateID.LIE_DOWN: 0.3,
            StateID.LIE_DOWN_AND_BARK: 0.1,
            StateID.RUN: 0.0,
            StateID.RUN_AND_BARK: 0.0,
            StateID.STAND: 0.0,
            StateID.STAND_AND_BARK: 0.0,
            StateID.SLEEP: 0.0,
        },
        time_range=(10, 30),
        animation_time_rate=0.2,
        speed=0,
    ),
]
