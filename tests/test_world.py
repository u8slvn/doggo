from __future__ import annotations

import time

import pygame as pg
import pytest

from doggo import ASSETS_PATH
from doggo.world import World


@pytest.fixture
def create_world():
    world = None

    def _(fullscreen=False):
        nonlocal world
        world = World(
            title="Doggo Test",
            size=(340, 106),
            icon=ASSETS_PATH.joinpath("icon.png"),
            fps=30,
            fullscreen=fullscreen,
        )

        return world

    yield _

    if world is not None:
        world.window.destroy()


def test_world_initializes_correctly(create_world):
    world = create_world()

    assert world.window.title == "Doggo Test"
    assert world.window.size == (340, 106)
    assert world.window.borderless is True
    assert world.window.always_on_top is True
    assert world.window_surf.get_size() == (340, 106)
    assert world.screen.get_size() == (340, 106)
    assert world.fullscreen is False
    assert world.fps == 30
    assert world._running is False
    assert world.dt == 0.0


@pytest.mark.parametrize("fullscreen", [True, False])
def test_world_screen_is_scaled_regarding_fullscreen(create_world, fullscreen):
    world = create_world(fullscreen)
    screen = world.get_screen()

    if fullscreen:
        assert screen.get_size() == world.window_surf.get_size()
    else:
        assert screen.get_size() == (340, 106)


def test_world_get_dt(create_world):
    world = create_world()
    time.sleep(0.1)

    world.get_dt()

    assert world.dt > 0.0


@pytest.mark.parametrize(
    "event",
    [
        pg.event.Event(pg.QUIT),
        pg.event.Event(pg.KEYDOWN, {"key": pg.K_ESCAPE}),
    ],
)
def test_world_stop_at_some_events(mocker, create_world, event):
    mocker.patch("pygame.event.get", return_value=[event])
    world = create_world()
    world._running = True

    world.process_inputs()

    assert world._running is False


@pytest.mark.parametrize(
    "fullscreen",
    [True, False],
)
def test_world_draggable_window_is_processed_correctly(
    mocker, create_world, fullscreen
):
    mocker.patch("pygame.event.get", return_value=[pg.event.Event(pg.MOUSEBUTTONDOWN)])
    world = create_world(fullscreen)
    mocker.patch.object(world.draggable, "process_event", spec=True)

    world.process_inputs()

    if fullscreen:
        world.draggable.process_event.assert_not_called()
    else:
        world.draggable.process_event.assert_called_once_with(event=pg.event.get()[0])


def test_world_update(mocker, create_world):
    world = create_world()
    world.dt = 0.1
    mocker.patch.object(world.dog, "update", spec=True)

    world.update()

    world.dog.update.assert_called_once_with(dt=0.1)


def test_world_render(mocker, create_world):
    world = create_world()
    screen = mocker.patch.object(world, "screen", spec=True)
    landscape = mocker.patch.object(world, "landscape", spec=True)
    dog = mocker.patch.object(world, "dog", spec=True)
    window_surf = mocker.patch.object(world, "window_surf", spec=True)
    window = mocker.patch.object(world, "window", spec=True)

    world.render()

    screen.fill.assert_called_once_with((135, 206, 235))
    landscape.background.draw.assert_called_once_with(screen=screen)
    dog.draw.assert_called_once_with(screen=screen)
    landscape.foreground.draw.assert_called_once_with(screen=screen)
    window_surf.blit.assert_called_once_with(screen, (0, 0))
    window.flip.assert_called_once()


def test_world_start(mocker, create_world):
    world = create_world()
    run = mocker.patch.object(world, "run", spec=True)

    world.start()

    assert world._running is True
    run.assert_called_once()


def test_world_run_game_loop(mocker, create_world):
    world = create_world()
    mocker.patch.object(world, "is_running", side_effect=[True, False])
    get_dt = mocker.patch.object(world, "get_dt", spec=True)
    process_inputs = mocker.patch.object(world, "process_inputs", spec=True)
    update = mocker.patch.object(world, "update", spec=True)
    render = mocker.patch.object(world, "render", spec=True)
    clock = mocker.patch.object(world, "clock", spec=True)
    destroy = mocker.patch.object(world, "destroy", spec=True)

    world.run()

    get_dt.assert_called_once()
    process_inputs.assert_called_once()
    update.assert_called_once()
    render.assert_called_once()
    clock.tick.assert_called_once_with(world.fps)
    destroy.assert_called_once()


@pytest.mark.parametrize("raise_exception", [KeyboardInterrupt, Exception])
def test_world_run_initializes_dedstruction_on_exception(
    mocker, create_world, raise_exception
):
    world = create_world()
    mocker.patch.object(world, "get_dt", spec=True, side_effect=[raise_exception])
    process_inputs = mocker.patch.object(world, "process_inputs", spec=True)
    destroy = mocker.patch.object(world, "destroy", spec=True)

    world.start()  # It will call the run method.

    process_inputs.assert_not_called()
    destroy.assert_called_once()


def test_world_stop(mocker, create_world):
    world = create_world()
    mocker.patch.object(world, "run", spec=True)
    world.start()

    world.stop()

    assert not world.is_running()


def test_world_destroy(mocker, create_world):
    pg_quit = mocker.patch("pygame.quit")
    sys_exit = mocker.patch("sys.exit")
    world = create_world()

    world.destroy()

    pg_quit.assert_called_once()
    sys_exit.assert_called_once()
