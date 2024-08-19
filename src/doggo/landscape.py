from __future__ import annotations

import random

from enum import IntEnum

import pygame as pg

from doggo import ASSETS_PATH
from doggo import config


class Biome(IntEnum):
    """The possible biomes of the game."""

    MOUNTAIN = 0

    @classmethod
    def random(cls) -> Biome:
        """Return a random fur color."""
        return random.choice(list(cls))  # nosec


class LandscapeLayer:
    """A layer of the landscape."""

    path = ASSETS_PATH.joinpath("landscape")

    def __init__(self, topleft: tuple[int, int], image: str) -> None:
        image_path = self.path.joinpath(image)
        self.image = pg.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=topleft)

    def draw(self, screen: pg.Surface) -> None:
        """Draw the landscape on the screen."""
        screen.blit(self.image, self.rect)


class Landscape:
    """The landscape of the game."""

    bg_suffix = "_bg.png"
    fg_suffix = "_fg.png"

    def __init__(self, biome: Biome) -> None:
        self.background = LandscapeLayer(
            topleft=(0, 0), image=f"{biome:02d}{self.bg_suffix}"
        )
        self.foreground = LandscapeLayer(
            topleft=(0, config.WORLD_GROUND), image=f"{biome:02d}{self.fg_suffix}"
        )
