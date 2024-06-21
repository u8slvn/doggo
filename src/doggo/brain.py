from __future__ import annotations

import random

from dataclasses import dataclass
from enum import IntEnum
from enum import auto
from typing import Iterable


class State(IntEnum):
    IDLE = 0
    WALK = auto()
    SIT = auto()
    RUN = auto()
    EAT = auto()


@dataclass
class StateConfig:
    state: State
    text: str
    transitions: dict[State, float]
    time_range: tuple[int, int]

    def __post_init__(self) -> None:
        if not len(self.transitions) == len(State):
            raise ValueError(
                f"The number of transitions of state {self.state.name} must be equal "
                f"to the number of states"
            )

        if not sum(self.transitions.values()) == 1:
            raise ValueError(
                f"The sum of the transition probabilities of state {self.state.name} "
                f"must be equal to 1"
            )


class Brain:
    def __init__(self, states: Iterable[StateConfig]) -> None:
        self._config = {config.state: config for config in states}
        self.current_state = random.choice(list(State))

        if not set(self._config.keys()) == set(State):
            raise ValueError(
                f"The states must be defined for all the states, missing: {set(State) - set(self._config.keys())}"
            )

    def is_doing(self) -> str:
        return self._config[self.current_state].text

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.is_doing()}...)"
