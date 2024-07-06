from __future__ import annotations

from doggo.brain import Brain
from doggo.brain import Direction
from doggo.brain import State
from doggo.brain import StateID
from doggo.mind import STATES
from freezegun import freeze_time


def full_range(range_: tuple[int, int]) -> list[int]:
    return list(range(range_[0], range_[1] + 1))


def state_factory(state_id: StateID) -> State:
    return State(
        id=state_id,
        time_range=(1, 5),
        text=state_id.name.title(),
        transitions={
            StateID.IDLE: 0.3,
            StateID.WALK: 0.3,
            StateID.SIT: 0.2,
            StateID.RUN: 0.2,
            StateID.EAT: 0.0,
        },
    )


def get_states_test():
    return [
        State(
            id=StateID.IDLE,
            text=f"test {StateID.IDLE.name}",
            transitions={
                StateID.IDLE: 0.0,
                StateID.WALK: 0.3,
                StateID.SIT: 0.3,
                StateID.RUN: 0.2,
                StateID.EAT: 0.2,
            },
            time_range=(1, 5),
        ),
        State(
            id=StateID.WALK,
            text=f"test {StateID.WALK.name}",
            transitions={
                StateID.IDLE: 0.3,
                StateID.WALK: 0.0,
                StateID.SIT: 0.3,
                StateID.RUN: 0.2,
                StateID.EAT: 0.2,
            },
            time_range=(1, 5),
        ),
        State(
            id=StateID.SIT,
            text=f"test {StateID.SIT.name}",
            transitions={
                StateID.IDLE: 0.3,
                StateID.WALK: 0.3,
                StateID.SIT: 0.0,
                StateID.RUN: 0.2,
                StateID.EAT: 0.2,
            },
            time_range=(1, 5),
        ),
        State(
            id=StateID.RUN,
            text=f"test {StateID.RUN.name}",
            transitions={
                StateID.IDLE: 0.3,
                StateID.WALK: 0.3,
                StateID.SIT: 0.2,
                StateID.RUN: 0.0,
                StateID.EAT: 0.2,
            },
            time_range=(1, 5),
        ),
        State(
            id=StateID.EAT,
            text=f"test {StateID.EAT.name}",
            transitions={
                StateID.IDLE: 0.3,
                StateID.WALK: 0.3,
                StateID.SIT: 0.2,
                StateID.RUN: 0.2,
                StateID.EAT: 0.0,
            },
            time_range=(1, 5),
        ),
    ]


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
    state = state_factory(StateID.IDLE)

    assert state.name == state.id.name.title()


def test_state_is_done_when_time_is_up():
    with freeze_time("2024-07-01 00:00:00"):
        state = state_factory(StateID.IDLE)
    state.countdown = 1

    with freeze_time("2024-07-01 00:00:01"):
        assert state.is_done() is True


def test_wind_up_sets_countdown_and_direction():
    state = state_factory(StateID.IDLE)
    state.countdown = 0

    state.wind_up()

    assert state.countdown in full_range(state.time_range)


def test_brain_initializes_correctly():
    brain = Brain(states=STATES)

    assert isinstance(brain.current_state, State)
    assert brain.current_state.id in StateID
    assert brain.is_doing() == brain.current_state.text
    assert str(brain) == f"Brain({brain.current_state.text}...)"


def test_change_state_of_brain():
    brain = Brain(states=get_states_test(), default_state_id=StateID.IDLE)
    brain.current_state.countdown = 0

    brain.change_state(state_id=StateID.WALK)

    assert brain.current_state.id != StateID.IDLE
    assert brain.current_state.countdown in full_range(brain.current_state.time_range)


def test_update_brain_changes_state_when_time_is_up():
    with freeze_time("2024-07-01 00:00:00"):
        brain = Brain(states=get_states_test(), default_state_id=StateID.IDLE)
    brain.current_state.countdown = 1

    with freeze_time("2024-07-01 00:00:01"):
        brain.update()

    assert brain.current_state.id != StateID.IDLE
    assert brain.current_state.countdown in full_range(brain.current_state.time_range)
