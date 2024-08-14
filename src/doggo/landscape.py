from __future__ import annotations

from abc import ABC
from abc import abstractmethod

import pygame as pg

from doggo import ASSETS_PATH


class LandscapeBase(ABC):
    """Abstract class for static landscape objects."""

    @abstractmethod
    def render(self, surface: pg.Surface) -> None:
        raise NotImplementedError


class Landscape(LandscapeBase):
    """The landscape of the world."""

    def __init__(self, items: list[LandscapeBase] | None = None) -> None:
        self._items = items or []

    def add(self, item: LandscapeBase) -> None:
        """Add a static item to the landscape."""
        self._items.append(item)

    def render(self, surface: pg.Surface) -> None:
        """Render the landscape."""
        for item in self._items:
            item.render(surface)


class StaticLandscape(LandscapeBase):
    """Abstract class for static landscape."""

    def __init__(self, topleft: tuple[int, int], path: str) -> None:
        self.topleft = topleft
        self._surface = pg.image.load(ASSETS_PATH.joinpath(path)).convert_alpha()

    def render(self, surface: pg.Surface) -> None:
        """Render the ground."""
        surface.blit(self._surface, self.topleft)
