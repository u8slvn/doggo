from __future__ import annotations

import random

from dataclasses import dataclass
from enum import IntEnum
from enum import auto

import numpy as np


class StateID(IntEnum):
    IDLE = 0
    WALK = auto()
    SIT = auto()
    RUN = auto()
    EAT = auto()


class Brain:
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
        return self.current_state.text

    def update(self) -> None:
        self.current_state.update()

        if self.current_state.is_done():
            next_state_id = np.random.choice(
                list(StateID), p=list(self.current_state.transitions.values())
            )
            self.current_state = self._states[next_state_id]
            self.current_state.wind_up()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.is_doing()}...)"


@dataclass
class State:
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
        return self.id.name.title()

    def wind_up(self) -> None:
        self.time = random.randint(*self.time_range)

    def is_done(self) -> bool:
        return self.time == 0

    def update(self) -> None:
        self.time -= 1
