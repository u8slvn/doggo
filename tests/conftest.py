from __future__ import annotations

import pygame as pg
import pytest


@pytest.fixture(scope="session", autouse=True)
def pygame():
    """Start and stop pygame instance for all tests."""

    pg.init()
    pg.display.set_mode((1, 1))

    yield

    pg.quit()
