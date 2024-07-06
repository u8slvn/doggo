from __future__ import annotations

import pygame as pg
import pytest

from doggo.brain import State
from doggo.brain import StateID


STATES_TEST = [
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


@pytest.fixture(scope="session", autouse=True)
def pygame():
    """Start and stop pygame instance for all tests."""

    pg.init()
    pg.display.set_mode((800, 600))

    yield

    pg.quit()
