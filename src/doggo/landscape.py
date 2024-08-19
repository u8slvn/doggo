from __future__ import annotations

import pygame as pg

from doggo import ASSETS_PATH


class Landscape:
    """The landscape of the game."""

    path = ASSETS_PATH.joinpath("landscape")

    def __init__(self, topleft: tuple[int, int], image: str) -> None:
        super().__init__()
        image_path = self.path.joinpath(image)
        self.image = pg.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=topleft)

    def draw(self, screen: pg.Surface) -> None:
        """Draw the landscape on the screen."""
        screen.blit(self.image, self.rect)
