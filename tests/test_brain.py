from __future__ import annotations

from doggo.brain import Brain
from doggo.brain import State
from doggo.brain import StateID

from tests.conftest import STATES_TEST


def full_range(range_: tuple[int, int]) -> list[int]:
    return list(range(range_[0], range_[1] + 1))


def test_brain_start_with_random_state():
    brain = Brain(states=STATES_TEST)

    assert isinstance(brain.current_state, State)
    assert brain.current_state.id in StateID
    assert brain.is_doing() == brain.current_state.text
    assert str(brain) == f"Brain({brain.current_state.text}...)"
    assert brain.current_state.name == brain.current_state.id.name.title()
    assert brain.current_state.time in full_range(brain.current_state.time_range)
