from __future__ import annotations

from doggo.config import DOG_STATES
from doggo.dog import StateID
from doggo.dog.brain import Brain
from doggo.dog.brain import Direction
from doggo.dog.brain import State
from freezegun import freeze_time


def full_range(range_: tuple[int, int]) -> list[int]:
    return list(range(range_[0], range_[1] + 1))


def state_factory(state_id: StateID) -> State:
    return State(
        id=state_id,
        time_range=(1, 5),
        transitions={
            StateID.IDLE: 0.1,
            StateID.IDLE_AND_BARK: 0.1,
            StateID.WALK: 0.1,
            StateID.WALK_AND_BARK: 0.1,
            StateID.SIT: 0.1,
            StateID.SIT_AND_BARK: 0.1,
            StateID.LIE_DOWN: 0.1,
            StateID.LIE_DOWN_AND_BARK: 0.0,
            StateID.RUN: 0.1,
            StateID.RUN_AND_BARK: 0.1,
            StateID.STAND: 0.05,
            StateID.STAND_AND_BARK: 0.05,
            StateID.SLEEP: 0.0,
        },
    )


def get_states_test():
    return [
        State(
            id=StateID.IDLE,
            transitions={
                StateID.IDLE: 0.0,
                StateID.IDLE_AND_BARK: 0.2,
                StateID.WALK: 0.1,
                StateID.WALK_AND_BARK: 0.1,
                StateID.SIT: 0.1,
                StateID.SIT_AND_BARK: 0.1,
                StateID.LIE_DOWN: 0.1,
                StateID.LIE_DOWN_AND_BARK: 0.0,
                StateID.RUN: 0.1,
                StateID.RUN_AND_BARK: 0.1,
                StateID.STAND: 0.05,
                StateID.STAND_AND_BARK: 0.05,
                StateID.SLEEP: 0.0,
            },
            time_range=(1, 5),
        ),
        State(
            id=StateID.IDLE_AND_BARK,
            transitions={
                StateID.IDLE: 0.0,
                StateID.IDLE_AND_BARK: 0.1,
                StateID.WALK: 0.2,
                StateID.WALK_AND_BARK: 0.1,
                StateID.SIT: 0.1,
                StateID.SIT_AND_BARK: 0.1,
                StateID.LIE_DOWN: 0.1,
                StateID.LIE_DOWN_AND_BARK: 0.0,
                StateID.RUN: 0.1,
                StateID.RUN_AND_BARK: 0.1,
                StateID.STAND: 0.05,
                StateID.STAND_AND_BARK: 0.05,
                StateID.SLEEP: 0.0,
            },
            time_range=(1, 5),
        ),
        State(
            id=StateID.WALK,
            transitions={
                StateID.IDLE: 0.1,
                StateID.IDLE_AND_BARK: 0.1,
                StateID.WALK: 0.1,
                StateID.WALK_AND_BARK: 0.1,
                StateID.SIT: 0.15,
                StateID.SIT_AND_BARK: 0.1,
                StateID.LIE_DOWN: 0.0,
                StateID.LIE_DOWN_AND_BARK: 0.0,
                StateID.RUN: 0.2,
                StateID.RUN_AND_BARK: 0.05,
                StateID.STAND: 0.05,
                StateID.STAND_AND_BARK: 0.05,
                StateID.SLEEP: 0.0,
            },
            time_range=(5, 10),
        ),
        State(
            id=StateID.WALK_AND_BARK,
            transitions={
                StateID.IDLE: 0.1,
                StateID.IDLE_AND_BARK: 0.1,
                StateID.WALK: 0.1,
                StateID.WALK_AND_BARK: 0.1,
                StateID.SIT: 0.15,
                StateID.SIT_AND_BARK: 0.1,
                StateID.LIE_DOWN: 0.0,
                StateID.LIE_DOWN_AND_BARK: 0.0,
                StateID.RUN: 0.2,
                StateID.RUN_AND_BARK: 0.05,
                StateID.STAND: 0.05,
                StateID.STAND_AND_BARK: 0.05,
                StateID.SLEEP: 0.0,
            },
            time_range=(5, 10),
        ),
        State(
            id=StateID.SIT,
            transitions={
                StateID.IDLE: 0.1,
                StateID.IDLE_AND_BARK: 0.05,
                StateID.WALK: 0.1,
                StateID.WALK_AND_BARK: 0.05,
                StateID.SIT: 0.1,
                StateID.SIT_AND_BARK: 0.05,
                StateID.LIE_DOWN: 0.25,
                StateID.LIE_DOWN_AND_BARK: 0.05,
                StateID.RUN: 0.05,
                StateID.RUN_AND_BARK: 0.0,
                StateID.STAND: 0.05,
                StateID.STAND_AND_BARK: 0.05,
                StateID.SLEEP: 0.1,
            },
            time_range=(5, 10),
            speed=0,
        ),
        State(
            id=StateID.SIT_AND_BARK,
            transitions={
                StateID.IDLE: 0.1,
                StateID.IDLE_AND_BARK: 0.05,
                StateID.WALK: 0.1,
                StateID.WALK_AND_BARK: 0.05,
                StateID.SIT: 0.1,
                StateID.SIT_AND_BARK: 0.05,
                StateID.LIE_DOWN: 0.25,
                StateID.LIE_DOWN_AND_BARK: 0.05,
                StateID.RUN: 0.05,
                StateID.RUN_AND_BARK: 0.0,
                StateID.STAND: 0.05,
                StateID.STAND_AND_BARK: 0.05,
                StateID.SLEEP: 0.1,
            },
            time_range=(5, 10),
            speed=0,
        ),
        State(
            id=StateID.LIE_DOWN,
            transitions={
                StateID.IDLE: 0.1,
                StateID.IDLE_AND_BARK: 0.1,
                StateID.WALK: 0.1,
                StateID.WALK_AND_BARK: 0.1,
                StateID.SIT: 0.2,
                StateID.SIT_AND_BARK: 0.05,
                StateID.LIE_DOWN: 0.1,
                StateID.LIE_DOWN_AND_BARK: 0.05,
                StateID.RUN: 0.1,
                StateID.RUN_AND_BARK: 0.0,
                StateID.STAND: 0.0,
                StateID.STAND_AND_BARK: 0.0,
                StateID.SLEEP: 0.1,
            },
            time_range=(5, 10),
            speed=0,
        ),
        State(
            id=StateID.LIE_DOWN_AND_BARK,
            transitions={
                StateID.IDLE: 0.1,
                StateID.IDLE_AND_BARK: 0.1,
                StateID.WALK: 0.1,
                StateID.WALK_AND_BARK: 0.1,
                StateID.SIT: 0.2,
                StateID.SIT_AND_BARK: 0.05,
                StateID.LIE_DOWN: 0.1,
                StateID.LIE_DOWN_AND_BARK: 0.05,
                StateID.RUN: 0.1,
                StateID.RUN_AND_BARK: 0.0,
                StateID.STAND: 0.0,
                StateID.STAND_AND_BARK: 0.0,
                StateID.SLEEP: 0.1,
            },
            time_range=(5, 10),
            speed=0,
        ),
        State(
            id=StateID.RUN,
            transitions={
                StateID.IDLE: 0.35,
                StateID.IDLE_AND_BARK: 0.05,
                StateID.WALK: 0.3,
                StateID.WALK_AND_BARK: 0.05,
                StateID.SIT: 0.0,
                StateID.SIT_AND_BARK: 0.0,
                StateID.LIE_DOWN: 0.0,
                StateID.LIE_DOWN_AND_BARK: 0.0,
                StateID.RUN: 0.2,
                StateID.RUN_AND_BARK: 0.05,
                StateID.STAND: 0.0,
                StateID.STAND_AND_BARK: 0.0,
                StateID.SLEEP: 0.0,
            },
            time_range=(5, 10),
            speed=100,
        ),
        State(
            id=StateID.RUN_AND_BARK,
            transitions={
                StateID.IDLE: 0.35,
                StateID.IDLE_AND_BARK: 0.05,
                StateID.WALK: 0.3,
                StateID.WALK_AND_BARK: 0.05,
                StateID.SIT: 0.0,
                StateID.SIT_AND_BARK: 0.0,
                StateID.LIE_DOWN: 0.0,
                StateID.LIE_DOWN_AND_BARK: 0.0,
                StateID.RUN: 0.2,
                StateID.RUN_AND_BARK: 0.05,
                StateID.STAND: 0.0,
                StateID.STAND_AND_BARK: 0.0,
                StateID.SLEEP: 0.0,
            },
            time_range=(5, 10),
            speed=100,
        ),
        State(
            id=StateID.STAND,
            transitions={
                StateID.IDLE: 0.1,
                StateID.IDLE_AND_BARK: 0.1,
                StateID.WALK: 0.1,
                StateID.WALK_AND_BARK: 0.1,
                StateID.SIT: 0.1,
                StateID.SIT_AND_BARK: 0.05,
                StateID.LIE_DOWN: 0.1,
                StateID.LIE_DOWN_AND_BARK: 0.05,
                StateID.RUN: 0.1,
                StateID.RUN_AND_BARK: 0.0,
                StateID.STAND: 0.05,
                StateID.STAND_AND_BARK: 0.05,
                StateID.SLEEP: 0.1,
            },
            time_range=(5, 10),
            speed=0,
        ),
        State(
            id=StateID.STAND_AND_BARK,
            transitions={
                StateID.IDLE: 0.1,
                StateID.IDLE_AND_BARK: 0.1,
                StateID.WALK: 0.1,
                StateID.WALK_AND_BARK: 0.1,
                StateID.SIT: 0.1,
                StateID.SIT_AND_BARK: 0.05,
                StateID.LIE_DOWN: 0.1,
                StateID.LIE_DOWN_AND_BARK: 0.05,
                StateID.RUN: 0.1,
                StateID.RUN_AND_BARK: 0.0,
                StateID.STAND: 0.05,
                StateID.STAND_AND_BARK: 0.05,
                StateID.SLEEP: 0.1,
            },
            time_range=(5, 10),
            speed=0,
        ),
        State(
            id=StateID.SLEEP,
            transitions={
                StateID.IDLE: 0.1,
                StateID.IDLE_AND_BARK: 0.1,
                StateID.WALK: 0.0,
                StateID.WALK_AND_BARK: 0.0,
                StateID.SIT: 0.3,
                StateID.SIT_AND_BARK: 0.1,
                StateID.LIE_DOWN: 0.3,
                StateID.LIE_DOWN_AND_BARK: 0.1,
                StateID.RUN: 0.0,
                StateID.RUN_AND_BARK: 0.0,
                StateID.STAND: 0.0,
                StateID.STAND_AND_BARK: 0.0,
                StateID.SLEEP: 0.0,
            },
            time_range=(5, 10),
            animation_time_rate=0.2,
            speed=0,
        ),
    ]


def test_get_random_state_id():
    state_id = StateID.random()

    assert state_id in StateID


def test_get_random_state_id_with_probs():
    probs = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    state_id = StateID.random_with_probs(probs)

    assert state_id in StateID


def test_get_random_direction():
    direction = Direction.random()

    assert direction in Direction


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
    brain = Brain.from_config(state_configs=DOG_STATES)

    assert isinstance(brain.current_state, State)
    assert brain.current_state.id in StateID
    assert str(brain) == f"Brain({brain.current_state.id})"


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
