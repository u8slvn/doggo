from __future__ import annotations

import random

from abc import ABC
from abc import abstractmethod
from enum import StrEnum
from enum import auto
from typing import ClassVar
from typing import Type


STATES: dict[StateID, Type[State]] = {}


class StateID(StrEnum):
    IDLE = auto()
    WALK = auto()
    SIT = auto()
    RUN = auto()
    EAT = auto()


class Brain:
    _states: ClassVar[dict[str, Type[State]]] = {}

    def __init__(self) -> None:
        self.current_state = self._states[random.choice(list(StateID))]()

        registered_states = set(self._states.keys())

        assert registered_states == set(StateID), (
            f"The states must be defined for all the states, missing: "
            f"{set(StateID) - registered_states}"
        )

    @classmethod
    def register_state(cls, state: Type[State]) -> None:
        cls._states[state.id] = state

    def is_doing(self) -> str:
        return self.current_state.text

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.is_doing()}...)"


class State(ABC):
    id: StateID
    text: str
    transitions: ClassVar[dict[StateID, float]]
    time_range: tuple[int, int]

    def __init_subclass__(cls) -> None:
        Brain.register_state(cls)

    def __init__(self) -> None:
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
        return self.id.name

    @abstractmethod
    def update(self) -> None:
        raise NotImplementedError


class Idle(State):
    id = StateID.IDLE
    text = "I'm just chilling"
    transitions: ClassVar[dict[StateID, float]] = {
        StateID.IDLE: 0.2,
        StateID.WALK: 0.2,
        StateID.SIT: 0.2,
        StateID.RUN: 0.2,
        StateID.EAT: 0.2,
    }
    time_range = (1, 5)

    def update(self) -> None:
        pass


class Walk(State):
    id = StateID.WALK
    text = "I'm going for a walk"
    transitions: ClassVar[dict[StateID, float]] = {
        StateID.IDLE: 0.2,
        StateID.WALK: 0.2,
        StateID.SIT: 0.2,
        StateID.RUN: 0.2,
        StateID.EAT: 0.2,
    }
    time_range = (1, 5)

    def update(self) -> None:
        pass


class Sit(State):
    id = StateID.SIT
    text = "I'm sitting"
    transitions: ClassVar[dict[StateID, float]] = {
        StateID.IDLE: 0.2,
        StateID.WALK: 0.2,
        StateID.SIT: 0.2,
        StateID.RUN: 0.2,
        StateID.EAT: 0.2,
    }
    time_range = (1, 5)

    def update(self) -> None:
        pass


class Run(State):
    id = StateID.RUN
    text = "I'm running"
    transitions: ClassVar[dict[StateID, float]] = {
        StateID.IDLE: 0.2,
        StateID.WALK: 0.2,
        StateID.SIT: 0.2,
        StateID.RUN: 0.2,
        StateID.EAT: 0.2,
    }
    time_range = (1, 5)

    def update(self) -> None:
        pass


class Eat(State):
    id = StateID.EAT
    text = "I'm eating"
    transitions: ClassVar[dict[StateID, float]] = {
        StateID.IDLE: 0.2,
        StateID.WALK: 0.2,
        StateID.SIT: 0.2,
        StateID.RUN: 0.2,
        StateID.EAT: 0.2,
    }
    time_range = (1, 5)

    def update(self) -> None:
        pass
