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


class Brain:
    """The brain of the doggo.

    The brain is responsible for managing the states and the transitions between them.
    It's a simple state machine that changes the state based on the transition
    probabilities. The remaining time of the current state is defined randomly at each
    state change.
    """

    def __init__(self, states: list[State]) -> None:
        self._states = states
        self._states.sort(key=lambda state: state.id)

        registered_states = {state.id for state in self._states}
        assert registered_states == set(StateID), (
            f"The states must be defined for all the states, missing: "
            f"{set(StateID) - registered_states}"
        )

        self.current_state = self._states[random.choice(list(StateID))]

    def is_doing(self) -> str:
        """Return a human-friendly representation of what the brain is doing based on
        the current state.
        """
        return self.current_state.text

    def update(self) -> None:
        """Update the current brain state."""
        self.current_state.update()

        if self.current_state.is_done():
            next_state_id = np.random.choice(
                list(StateID), p=list(self.current_state.transitions.values())
            )
            self.current_state = self._states[next_state_id]
            self.current_state.wind_up()

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
    time: int = 0

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

    @property
    def name(self) -> str:
        """Return the stylized name of the state."""
        return self.id.name.title()

    def wind_up(self) -> None:
        """Wind up the state by setting the time to a random value within the time
        range.
        """
        self.time = random.randint(*self.time_range)

    def is_done(self) -> bool:
        """Check if the state is done."""
        return self.time == 0

    def update(self) -> None:
        """Update the state by decreasing the time left."""
        self.time -= 1
