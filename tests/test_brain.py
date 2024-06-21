from __future__ import annotations

import pytest

from doggo.brain import Brain
from doggo.brain import State
from doggo.brain import StateConfig


@pytest.mark.parametrize(
    "error_msg, transitions",
    [
        (
            "The number of transitions of state (.+) must be equal to the number of states",
            {
                State.IDLE: 0.2,
                State.WALK: 0.2,
                State.SIT: 0.2,
            },
        ),
        (
            "The sum of the transition probabilities of state (.+) must be equal to 1",
            {
                State.IDLE: 0.2,
                State.WALK: 0.2,
                State.SIT: 0.2,
                State.RUN: 0.2,
                State.EAT: 0.7,
            },
        ),
    ],
)
def test_state_config_cannot_be_built_with_invalid_transitions(error_msg, transitions):
    with pytest.raises(ValueError, match=error_msg):
        StateConfig(
            state=State.IDLE,
            text="I'm just chilling",
            transitions=transitions,
            time_range=(1, 5),
        )


def test_brain_must_be_configured_with_all_the_states():
    with pytest.raises(
        ValueError, match="The states must be defined for all the states, missing: {.*}"
    ):
        Brain(
            states=[
                StateConfig(
                    state=State.IDLE,
                    text="I'm just chilling",
                    transitions={
                        State.IDLE: 0.2,
                        State.WALK: 0.2,
                        State.SIT: 0.2,
                        State.RUN: 0.2,
                        State.EAT: 0.2,
                    },
                    time_range=(1, 5),
                ),
            ]
        )
