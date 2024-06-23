from __future__ import annotations

from doggo.brain import Brain
from doggo.brain import State
from doggo.brain import StateID


def test_brain_start_with_random_state():
    brain = Brain()

    assert isinstance(brain.current_state, State)
    assert brain.current_state.id in StateID
    assert brain.is_doing() == brain.current_state.text
    assert str(brain) == f"Brain({brain.current_state.text}...)"
    assert brain.current_state.name == brain.current_state.id.name
