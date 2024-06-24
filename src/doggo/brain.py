from __future__ import annotations

import random

from dataclasses import dataclass
from enum import IntEnum
from enum import auto

import numpy as np


class StateID(IntEnum):
    """The possible states of the doggo."""

    IDLE = 0
    WALK = auto()
    SIT = auto()
    RUN = auto()
    EAT = auto()

    @staticmethod
    def random() -> StateID:
        """Return a random state."""
        return StateID(random.choice(list(StateID)))

    @staticmethod
    def random_with_probs(p: list[float]) -> StateID:
        """Return a random state based on the given probabilities."""
        return StateID(np.random.choice(list(StateID), p=p))


class Direction(IntEnum):
    """The possible directions of the doggo."""

    LEFT = 0
    RIGHT = auto()

    @staticmethod
    def random() -> Direction:
        """Return a random direction."""
        return Direction(random.getrandbits(1))


class Brain:
    """The brain of the doggo.

    The brain is responsible for managing the states and the transitions between them.
    It's a simple state machine that changes the state based on the transition
    probabilities. The remaining time of the current state is defined randomly at each
    state change.
    """

    def __init__(self, states: list[State]) -> None:
        states.sort(key=lambda state: state.id)
        self._states = tuple(states)

        registered_states = {state.id for state in self._states}
        assert registered_states == set(StateID), (
            f"The states must be defined for all the states, missing: "
            f"{set(StateID) - registered_states}"
        )

        self.current_state = self._states[StateID.random()]
        self.state_time = self.current_state.get_remaining_time()
        self.direction = Direction.random()

    def is_doing(self) -> str:
        """Return a human-friendly representation of what the brain is doing based on
        the current state.
        """
        return self.current_state.text

    def update(self) -> None:
        """Update the current brain state."""
        self.state_time -= 1

        if self.state_time == 0:
            transition_probs = list(self.current_state.transitions.values())
            next_state_id = StateID.random_with_probs(transition_probs)

            self.current_state = self._states[next_state_id]
            self.state_time = self.current_state.get_remaining_time()
            self.direction = Direction.random()

    def __repr__(self) -> str:
        """String representation of the brain."""
        return f"{self.__class__.__name__}({self.is_doing()}...)"


@dataclass
class State:
    """A state of the doggo."""

    id: StateID
    text: str
    transitions: dict[StateID, float]
    time_range: tuple[int, int]

    def __post_init__(self) -> None:
        assert len(self.transitions) == len(StateID), (
            f"The number of transitions of state {self.name} must be equal "
            f"to the number of states"
        )
        assert sum(self.transitions.values()) == 1, (
            f"The sum of the transition probabilities of state {self.name} "
            f"must be equal to 1"
        )

    @property
    def name(self) -> str:
        """Return the stylized name of the state."""
        return self.id.name.title()

    def get_remaining_time(self) -> int:
        """Wind up the state by setting the time to a random value within the time
        range.
        """
        return random.randint(*self.time_range)
