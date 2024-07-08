# Mind module contains the states and transitions of the doggo's brain.
# This is basically the configuration of the doggo's brain.

from __future__ import annotations

import random
import time

from dataclasses import dataclass
from dataclasses import field
from enum import IntEnum
from enum import auto

import numpy as np


class StateID(IntEnum):
    """The possible states of the doggo."""

    IDLE = 0
    IDLE_AND_BARK = auto()
    WALK = auto()
    WALK_AND_BARK = auto()
    SIT = auto()
    SIT_AND_BARK = auto()
    LIE_DOWN = auto()
    LIE_DOWN_AND_BARK = auto()
    RUN = auto()
    RUN_AND_BARK = auto()
    STAND = auto()
    STAND_AND_BARK = auto()
    SLEEP = auto()

    @classmethod
    def random(cls) -> StateID:
        """Return a random state."""
        return random.choice(list(cls))

    @classmethod
    def random_with_probs(cls, p: list[float]) -> StateID:
        """Return a random state based on the given probabilities."""
        return cls(np.random.choice(list(cls), p=p))

    def __str__(self) -> str:
        return self.name.replace("_", " ")


class Direction(IntEnum):
    """The possible directions of the doggo."""

    LEFT = 0
    RIGHT = auto()

    @classmethod
    def random(cls) -> Direction:
        """Return a random direction."""
        return cls(random.getrandbits(1))


@dataclass
class State:
    """A state of the doggo."""

    _clock: float = field(init=False, default_factory=time.time)
    id: StateID
    transitions: dict[StateID, float]
    time_range: tuple[int, int]
    countdown: int = 0
    direction: Direction = field(default_factory=Direction.random)
    speed: int = 50
    animation_time_rate: float = 0.1

    def __post_init__(self) -> None:
        assert len(self.transitions) == len(StateID), (
            f"The number of transitions of state {self.id} must be equal "
            f"to the number of states"
        )
        assert sum(self.transitions.values()) == 1, (
            f"The sum of the transition probabilities of state {self.id} "
            f"must be equal to 1"
        )

        self.wind_up()

    def __call__(self) -> State:
        """Renew the state for a new iteration."""
        self.wind_up()
        self.direction = Direction.random()

        return self

    def is_done(self) -> bool:
        """Return whether the state is done or not."""
        return self.countdown <= time.time() - self._clock

    def wind_up(self) -> None:
        """Wind up the state for a new iteration."""
        self._clock = time.time()
        self.countdown = random.randint(*self.time_range)

    def get_next_state_id(self) -> StateID:
        """Return the next state based on the transition probabilities."""
        # We want to be sure that the order of the transitions is the same as the one
        # of the StateID.
        transition_probs = [self.transitions[state_id] for state_id in StateID]

        return StateID.random_with_probs(transition_probs)


STATES = [
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
        time_range=(3, 10),
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
        time_range=(3, 10),
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
        time_range=(5, 10),
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
        time_range=(5, 10),
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
        time_range=(5, 10),
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
        time_range=(5, 10),
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
        time_range=(5, 10),
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
        time_range=(5, 10),
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
        time_range=(5, 10),
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
        time_range=(5, 10),
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
        time_range=(5, 10),
        animation_time_rate=0.2,
        speed=0,
    ),
]
