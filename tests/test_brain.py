from __future__ import annotations

from doggo.brain import Brain
from doggo.brain import Direction
from doggo.brain import State
from doggo.brain import StateID
from doggo.mind import STATES

from tests.conftest import STATES_TEST


def full_range(range_: tuple[int, int]) -> list[int]:
    return list(range(range_[0], range_[1] + 1))


def test_get_random_state_id():
    state_id = StateID.random()

    assert state_id in StateID


def test_get_random_state_id_with_probs():
    probs = [0.1, 0.1, 0.1, 0.1, 0.6]
    state_id = StateID.random_with_probs(probs)

    assert state_id in StateID


def test_get_random_direction():
    direction = Direction.random()

    assert direction in Direction


def test_brain_initializes_correctly():
    brain = Brain(states=STATES)

    assert isinstance(brain.current_state, State)
    assert brain.current_state.id in StateID
    assert brain.is_doing() == brain.current_state.text
    assert str(brain) == f"Brain({brain.current_state.text}...)"
    assert brain.current_state.name == brain.current_state.id.name.title()
    assert brain.current_state_time in full_range(brain.current_state.time_range)


def test_change_state_of_brain():
    brain = Brain(states=STATES_TEST, default_state_id=StateID.IDLE)
    brain.current_state_time = 0

    brain.change_state(state_id=StateID.WALK)

    assert brain.current_state.id != StateID.IDLE
    assert brain.current_state_time in full_range(brain.current_state.time_range)
    assert brain.direction in Direction


def test_update_brain_changes_state_when_time_is_up():
    brain = Brain(states=STATES_TEST, default_state_id=StateID.IDLE)
    brain.current_state_time = 1

    brain.update()

    assert brain.current_state.id != StateID.IDLE
    assert brain.current_state_time in full_range(brain.current_state.time_range)
    assert brain.direction in Direction
