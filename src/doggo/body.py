from __future__ import annotations

import random

from enum import IntEnum
from enum import auto
from typing import TYPE_CHECKING

import pygame as pg

from doggo import ASSETS_PATH
from doggo.brain import Direction
from doggo.brain import StateID


if TYPE_CHECKING:
    from pathlib import Path


class Fur(IntEnum):
    """The possible fur colors of the doggo."""

    DARK_BROWN = 0
    LIGHT_BROWN = auto()
    GREY = auto()
    BLUE = auto()
    RED_BROWN = auto()
    WHITE = auto()
    WHITE_WITH_BROWN_SPOTS = auto()
    DARK_BROWN_WITH_GREY_SPOTS = auto()
    WHITE_WITH_GREY_SPOTS = auto()
    BLUE_WITH_BROWN_SPOTS = auto()
    LIGHT_BROWN_WITH_WHITE_SPOTS = auto()
    ORANGE = auto()

    @classmethod
    def random(cls) -> Fur:
        """Return a random fur color."""
        return random.choice(list(cls))


class Body:
    """The body of the doggo.

    Manage the sprite sheet of the doggo based on the fur color.
    """

    def __init__(
        self,
        fur: Fur,
        default_direction: Direction,
        sprite_sheet_size: tuple[int, int],
        states_sprites_config: dict[StateID, tuple[int, int]],
    ) -> None:
        """Initialize the body of the doggo.

        Fur color is used to load the correct sprite sheet.
        Default direction is used to set the initial direction sprite.
        Sprite sheet size represents the number of sprites in the sprite sheet
        (columns, rows).
        States sprites config is a dictionary that contains the configuration of the
        sprites for each state.
        """
        self.fur: Fur = fur
        self.default_direction: Direction = default_direction

        columns, rows = sprite_sheet_size
        asset_path = ASSETS_PATH.joinpath(f"dogs_{fur:02d}.png")
        self.sprite_sheet = SpriteSheet(path=asset_path, columns=columns, rows=rows)

        self.poses: dict[StateID, dict[Direction, list[pg.Surface]]] = {}

        for state, (col, row) in states_sprites_config.items():
            self.poses[state] = {
                direction: [
                    self.sprite_sheet.get_sprite(
                        loc=(col, row), flip_x=(direction == Direction.LEFT)
                    )
                    for direction in Direction
                ]
                for direction in Direction
            }

    def get_pose(self, state: StateID, direction: Direction) -> pg.Surface:
        """Return the pose of the doggo based on the state and the direction."""
        return self.poses[state][direction][0]


class SpriteSheet:
    """Load a sprite sheet and extract sprites from it."""

    def __init__(self, path: Path, columns: int, rows: int) -> None:
        self._sprite_sheet = pg.image.load(path).convert_alpha()
        self.rows = rows
        self.columns = columns
        self.sprite_size = (
            self._sprite_sheet.get_width() // columns,
            self._sprite_sheet.get_height() // rows,
        )

    def get_sprite(
        self, loc: tuple[int, int], flip_x: bool = False, flip_y: bool = False
    ) -> pg.Surface:
        """Return a sprite from the sprite sheet based on the location."""
        if loc[0] >= self.columns or loc[1] >= self.rows:
            raise ValueError("Sprite location is out of bounds")

        x = loc[0] * self.sprite_size[0]
        y = loc[1] * self.sprite_size[1]

        area = pg.Rect(x, y, *self.sprite_size)
        image = pg.Surface(self.sprite_size, pg.SRCALPHA)
        image.blit(self._sprite_sheet, dest=(0, 0), area=area)

        if flip_x or flip_y:
            image = pg.transform.flip(image, flip_x, flip_y)

        return image
