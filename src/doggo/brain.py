from __future__ import annotations

from loguru import logger

from doggo.mind import State
from doggo.mind import StateID


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
        self.current_state: State = self._states[initial_state_id]()

    @property
    def state_name(self) -> str:
        return self.current_state.name

    def is_doing(self) -> str:
        """Return a human-friendly representation of what the brain is doing."""
        return self.current_state.text

    def change_state(self, state_id: StateID) -> None:
        """Change the current state of the brain."""
        self.current_state = self._states[state_id]()
        logger.info(
            f"Doggo brain decided to {self.state_name} for {self.current_state.countdown}s: {self.is_doing()}"
        )

    def update(self) -> None:
        """Update the current brain state."""
        if self.current_state.is_done():
            self.change_state(state_id=self.current_state.get_next_state_id())

    def __repr__(self) -> str:
        """String representation of the brain."""
        return f"{self.__class__.__name__}({self.is_doing()}...)"
