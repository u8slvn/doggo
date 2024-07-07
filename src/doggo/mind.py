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
    WALK = auto()
    SIT = auto()
    RUN = auto()
    SLEEP = auto()

    @classmethod
    def random(cls) -> StateID:
        """Return a random state."""
        return random.choice(list(cls))

    @classmethod
    def random_with_probs(cls, p: list[float]) -> StateID:
        """Return a random state based on the given probabilities."""
        return cls(np.random.choice(list(cls), p=p))


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
    text: str
    transitions: dict[StateID, float]
    time_range: tuple[int, int]
    countdown: int = 0
    direction: Direction = field(default_factory=Direction.random)
    animation_time_rate: float = 0.1

    def __post_init__(self) -> None:
        assert len(self.transitions) == len(StateID), (
            f"The number of transitions of state {self.name} must be equal "
            f"to the number of states"
        )
        assert sum(self.transitions.values()) == 1, (
            f"The sum of the transition probabilities of state {self.name} "
            f"must be equal to 1"
        )

        self.wind_up()

    def __call__(self) -> State:
        """Renew the state for a new iteration."""
        self.wind_up()
        self.direction = Direction.random()

        return self

    @property
    def name(self) -> str:
        """Return the stylized name of the state."""
        return self.id.name.title()

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
        text="I'm just chilling",
        transitions={
            StateID.IDLE: 0.2,
            StateID.WALK: 0.2,
            StateID.SIT: 0.2,
            StateID.RUN: 0.2,
            StateID.SLEEP: 0.2,
        },
        time_range=(5, 10),
    ),
    State(
        id=StateID.WALK,
        text="I'm going for a walk",
        transitions={
            StateID.IDLE: 0.2,
            StateID.WALK: 0.2,
            StateID.SIT: 0.2,
            StateID.RUN: 0.2,
            StateID.SLEEP: 0.2,
        },
        time_range=(5, 10),
    ),
    State(
        id=StateID.SIT,
        text="I'm sitting",
        transitions={
            StateID.IDLE: 0.2,
            StateID.WALK: 0.2,
            StateID.SIT: 0.2,
            StateID.RUN: 0.2,
            StateID.SLEEP: 0.2,
        },
        time_range=(5, 10),
    ),
    State(
        id=StateID.RUN,
        text="I'm running",
        transitions={
            StateID.IDLE: 0.2,
            StateID.WALK: 0.2,
            StateID.SIT: 0.2,
            StateID.RUN: 0.2,
            StateID.SLEEP: 0.2,
        },
        time_range=(5, 10),
    ),
    State(
        id=StateID.SLEEP,
        text="I'm sleeping, zzzz...",
        transitions={
            StateID.IDLE: 0.2,
            StateID.WALK: 0.2,
            StateID.SIT: 0.2,
            StateID.RUN: 0.2,
            StateID.SLEEP: 0.2,
        },
        time_range=(5, 10),
        animation_time_rate=0.2,
    ),
]
