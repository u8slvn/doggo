from __future__ import annotations

import pygame as pg

from doggo import ASSETS_PATH


class Landscape(pg.sprite.Sprite):
    """Abstract class for landscape."""


class StaticLandscape(Landscape):
    """Abstract class for static landscape."""

    def __init__(self, topleft: tuple[int, int], path: str) -> None:
        super().__init__()
        self.image = pg.image.load(ASSETS_PATH.joinpath(path)).convert_alpha()
        self.rect = self.image.get_rect(topleft=topleft)
