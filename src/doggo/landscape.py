from __future__ import annotations

import random

from enum import IntEnum

import pygame as pg

from loguru import logger

from doggo import ASSETS_PATH
from doggo.dog.body import SpriteSheet


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

    def __init__(self, image: pg.Surface, topleft: tuple[int, int] = (0, 0)) -> None:
        self.image = image
        self.rect = self.image.get_rect(topleft=topleft)

    def draw(self, screen: pg.Surface) -> None:
        """Draw the landscape on the screen."""
        screen.blit(self.image, self.rect)


class Landscape:
    """The landscape of the game."""

    path = ASSETS_PATH.joinpath("landscape")

    def __init__(self, biome: Biome) -> None:
        asset_path = self.path.joinpath(f"{biome:02d}.png")
        sprite_sheet = SpriteSheet(path=asset_path, columns=1, rows=2)

        self.background = LandscapeLayer(image=sprite_sheet.get_sprite((0, 1)))
        self.foreground = LandscapeLayer(image=sprite_sheet.get_sprite((0, 0)))
