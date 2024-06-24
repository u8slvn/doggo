from __future__ import annotations

from doggo.brain import State
from doggo.brain import StateID


STATES = [
    State(
        id=StateID.IDLE,
        text="I'm just chilling",
        transitions={
            StateID.IDLE: 0.2,
            StateID.WALK: 0.2,
            StateID.SIT: 0.2,
            StateID.RUN: 0.2,
            StateID.EAT: 0.2,
        },
        time_range=(1, 5),
    ),
    State(
        id=StateID.WALK,
        text="I'm going for a walk",
        transitions={
            StateID.IDLE: 0.2,
            StateID.WALK: 0.2,
            StateID.SIT: 0.2,
            StateID.RUN: 0.2,
            StateID.EAT: 0.2,
        },
        time_range=(1, 5),
    ),
    State(
        id=StateID.SIT,
        text="I'm sitting",
        transitions={
            StateID.IDLE: 0.2,
            StateID.WALK: 0.2,
            StateID.SIT: 0.2,
            StateID.RUN: 0.2,
            StateID.EAT: 0.2,
        },
        time_range=(1, 5),
    ),
    State(
        id=StateID.RUN,
        text="I'm running",
        transitions={
            StateID.IDLE: 0.2,
            StateID.WALK: 0.2,
            StateID.SIT: 0.2,
            StateID.RUN: 0.2,
            StateID.EAT: 0.2,
        },
        time_range=(1, 5),
    ),
    State(
        id=StateID.EAT,
        text="I'm eating",
        transitions={
            StateID.IDLE: 0.2,
            StateID.WALK: 0.2,
            StateID.SIT: 0.2,
            StateID.RUN: 0.2,
            StateID.EAT: 0.2,
        },
        time_range=(1, 5),
    ),
]
