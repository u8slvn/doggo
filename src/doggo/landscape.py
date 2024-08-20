from __future__ import annotations

import random

from enum import IntEnum

import pygame as pg

from loguru import logger

from doggo import ASSETS_PATH


class Biome(IntEnum):
    """The possible biomes of the game."""

    MOUNTAIN = 0

    @classmethod
    def random(cls) -> Biome:
        """Return a random fur color."""
        biome_type = random.choice(list(cls))  # nosec
        logger.debug(f"Landscape biome: {biome_type.name}")

        return biome_type


class LandscapeLayer:
    """A layer of the landscape."""

    path = ASSETS_PATH.joinpath("landscape")

    def __init__(self, image: str, topleft: tuple[int, int] = (0, 0)) -> None:
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
        self.background = LandscapeLayer(image=f"{biome:02d}{self.bg_suffix}")
        self.foreground = LandscapeLayer(image=f"{biome:02d}{self.fg_suffix}")
