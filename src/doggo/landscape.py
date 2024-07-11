from __future__ import annotations

from abc import ABC
from abc import abstractmethod

import pygame as pg

from doggo import ASSETS_PATH


class StaticLandscapeObject(ABC):
    """Abstract class for static landscape objects."""

    @abstractmethod
    def render(self, surface: pg.Surface) -> None:
        raise NotImplementedError


class Ground(StaticLandscapeObject):
    """The ground of the world."""

    def __init__(self, height: int, path: str = "landscape/ground.png") -> None:
        self.height = height
        self._surface = pg.image.load(ASSETS_PATH.joinpath(path)).convert()

    def render(self, surface: pg.Surface) -> None:
        """Render the ground."""
        surface.blit(self._surface, (0, self.height))
