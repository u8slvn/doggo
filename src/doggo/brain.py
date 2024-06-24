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

    @classmethod
    def random(cls) -> StateID:
        """Return a random state."""
        return cls(random.choice(list(StateID)))

    @classmethod
    def random_with_probs(cls, p: list[float]) -> StateID:
        """Return a random state based on the given probabilities."""
        return cls(np.random.choice(list(StateID), p=p))


class Direction(IntEnum):
    """The possible directions of the doggo."""

    LEFT = 0
    RIGHT = auto()

    @classmethod
    def random(cls) -> Direction:
        """Return a random direction."""
        return cls(random.getrandbits(1))


class Brain:
    """The brain of the doggo.

    The brain is responsible for managing the states and the transitions between them.
    It's a simple state machine that changes the state based on the transition
    probabilities. The remaining time of the current state is defined randomly at each
    state change.
    """

    def __init__(
        self, states: list[State], default_state_id: None | StateID = None
    ) -> None:
        states.sort(key=lambda state: state.id)
        self._states = tuple(states)

        registered_states = {state.id for state in self._states}
        assert registered_states == set(StateID), (
            f"The states must be defined for all the states, missing: "
            f"{set(StateID) - registered_states}"
        )

        initial_state_id = (
            StateID.random() if default_state_id is None else default_state_id
        )
        self.current_state = self._states[initial_state_id]
        self.current_state_time = self.current_state.get_state_time()
        self.direction = Direction.random()

    def is_doing(self) -> str:
        """Return a human-friendly representation of what the brain is doing."""
        return self.current_state.text

    def change_state(self, state_id: StateID) -> None:
        """Change the current state of the brain.

        It also sets a new random lifetime for the new state and a random direction.
        """
        self.current_state = self._states[state_id]
        self.current_state_time = self.current_state.get_state_time()
        self.direction = Direction.random()

    def update(self) -> None:
        """Update the current brain state."""
        self.current_state_time -= 1

        if self.current_state_time <= 0:
            self.change_state(state_id=self.current_state.get_next_state_id())

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

    def get_state_time(self) -> int:
        """Return a new random lifetime for the state."""
        return random.randint(*self.time_range)

    def get_next_state_id(self) -> StateID:
        """Return the next state based on the transition probabilities."""
        # We want to be sure that the order of the transitions is the same as one of
        # the StateID.
        transition_probs = [self.transitions[state_id] for state_id in StateID]

        return StateID.random_with_probs(transition_probs)
