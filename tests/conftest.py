from __future__ import annotations

import pygame as pg
import pytest


@pytest.fixture(scope="session")
def pygame_test():
    """Start and stop pygame instance for a test."""

    pg.init()
    pg.display.set_mode((1, 1))

    yield

    pg.quit()


@pytest.fixture
def pg_screen_mock(mocker):
    """Mock the pygame screen surface."""

    return mocker.Mock(spec=pg.Surface, instance=True)


@pytest.fixture
def pg_window_mock(mocker):
    """Mock the pygame window."""

    window_mock = mocker.Mock(spec=pg.window.Window, instance=True)
    window_mock.position = (0, 0)

    return window_mock


@pytest.fixture
def pg_mouse_mock(mocker):
    """Mock the pygame mouse."""

    return mocker.patch("pygame.mouse", autospec=True)
