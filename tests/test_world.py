from __future__ import annotations

import time

import pytest

from doggo import ASSETS_PATH
from doggo.world import World


def test_world_initializes_correctly():
    world = World(
        title="Doggo Test",
        size=(340, 106),
        icon=ASSETS_PATH.joinpath("icon.png"),
        fps=30,
        fullscreen=False,
    )

    assert world.window.title == "Doggo Test"
    assert world.window.size == (340, 106)
    assert world.window.borderless is True
    assert world.window.always_on_top is True
    assert world.window_surf.get_size() == (340, 106)
    assert world.screen.get_size() == (340, 106)
    assert world.fullscreen is False
    assert world.fps == 30
    assert world.running is False
    assert world.dt == 0.0


@pytest.mark.parametrize("fullscreen", [True, False])
def test_world_screen_is_scaled_regarding_fullscreen(fullscreen):
    world = World(
        title="Doggo Test",
        size=(340, 106),
        icon=ASSETS_PATH.joinpath("icon.png"),
        fps=30,
        fullscreen=fullscreen,
    )

    screen = world.get_screen()

    if fullscreen:
        assert screen.get_size() == (340, 106)
    else:
        assert screen.get_size() == world.window_surf.get_size()


def test_world_get_dt():
    world = World(
        title="Doggo Test",
        size=(340, 106),
        icon=ASSETS_PATH.joinpath("icon.png"),
        fps=30,
        fullscreen=False,
    )
    time.sleep(0.1)

    world.get_dt()

    assert world.dt > 0.0
