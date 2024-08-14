from __future__ import annotations

import random
import time

from enum import IntEnum
from enum import auto
from typing import NotRequired
from typing import TypedDict

from loguru import logger

from doggo.dog import StateID


class Direction(IntEnum):
    """The possible directions of the dog."""

    LEFT = 0
    RIGHT = auto()

    @classmethod
    def random(cls) -> Direction:
        """Return a random direction."""
        return cls(random.getrandbits(1))


StateConfig = TypedDict(
    "StateConfig",
    {
        "id": StateID,
        "transitions": dict[StateID, float],
        "time_range": tuple[int, int],
        "countdown": NotRequired[int],
        "direction": NotRequired[Direction],
        "speed": NotRequired[int],
        "animation_time_rate": NotRequired[float],
    },
)


class State:
    """A state of the dog."""

    def __init__(
        self,
        id: StateID,
        transitions: dict[StateID, float],
        time_range: tuple[int, int],
        countdown: int = 0,
        direction: Direction | None = None,
        speed: int = 50,
        animation_time_rate: float = 0.1,
    ) -> None:
        assert len(transitions) == len(StateID), (
            f"The number of transitions of state {id} must be equal "
            f"to the number of states"
        )
        assert sum(transitions.values()) == 1, (
            f"The sum of the transition probabilities of state {id} "
            f"must be equal to 1"
        )

        self._clock: float = time.time()
        self.id: StateID = id
        # We want to be sure that the order of the transitions is the same as the one
        # of the StateID enum.
        self.transitions: list[float] = [transitions[state_id] for state_id in StateID]
        self.time_range: tuple[int, int] = time_range
        self.countdown: int = countdown
        self.direction: Direction = direction or Direction.random()
        self.speed: int = speed
        self.animation_time_rate: float = animation_time_rate
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
        self.countdown = random.randint(*self.time_range)  # nosec

    def get_next_state_id(self) -> StateID:
        """Return the next state based on the transition probabilities."""
        return StateID.random_with_probs(self.transitions)


class Brain:
    """The brain of the dog.

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
        self.current_state: State = self._states[initial_state_id]()

    @classmethod
    def from_config(
        cls, state_configs: list[StateConfig], default_state_id: None | StateID = None
    ) -> Brain:
        """Create a brain from a configuration list."""
        states = [State(**state_config) for state_config in state_configs]

        return cls(states=states, default_state_id=default_state_id)

    def change_state(self, state_id: StateID) -> None:
        """Change the current state of the brain."""
        self.current_state = self._states[state_id]()
        logger.info(
            f"Dog's brain decided to {self.current_state.id} for "
            f"{self.current_state.countdown}s."
        )

    def update(self) -> None:
        """Update the current brain state."""
        if self.current_state.is_done():
            self.change_state(state_id=self.current_state.get_next_state_id())

    def __repr__(self) -> str:
        """String representation of the brain."""
        return f"{self.__class__.__name__}({self.current_state.id})"
