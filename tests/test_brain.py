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


def test_state_name_is_well_formatted():
    state = STATES_TEST[0]

    assert state.name == state.id.name.title()


def test_state_tick_decreases_time():
    state = STATES_TEST[0]
    state.time = 5

    state.tick()

    assert state.time == 4


def test_state_is_done_when_time_is_up():
    state = STATES_TEST[0]
    state.time = 0

    assert state.is_done() is True


def test_wind_up_sets_time_and_direction():
    state = STATES_TEST[0]
    state.time = 0

    state.wind_up()

    assert state.time in full_range(state.time_range)


def test_brain_initializes_correctly():
    brain = Brain(states=STATES)

    assert isinstance(brain.current_state, State)
    assert brain.current_state.id in StateID
    assert brain.is_doing() == brain.current_state.text
    assert str(brain) == f"Brain({brain.current_state.text}...)"


def test_change_state_of_brain():
    brain = Brain(states=STATES_TEST, default_state_id=StateID.IDLE)
    brain.current_state.time = 0

    brain.change_state(state_id=StateID.WALK)

    assert brain.current_state.id != StateID.IDLE
    assert brain.current_state.time in full_range(brain.current_state.time_range)


def test_update_brain_changes_state_when_time_is_up():
    brain = Brain(states=STATES_TEST, default_state_id=StateID.IDLE)
    brain.current_state.time = 1

    brain.update()

    assert brain.current_state.id != StateID.IDLE
    assert brain.current_state.time in full_range(brain.current_state.time_range)
