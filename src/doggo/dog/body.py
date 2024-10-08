from __future__ import annotations

import random

from collections import defaultdict
from enum import IntEnum
from enum import auto
from itertools import cycle
from typing import TYPE_CHECKING
from typing import Iterator

import pygame as pg

from loguru import logger

from doggo import ASSETS_PATH
from doggo.dog import StateID
from doggo.dog.brain import Direction


if TYPE_CHECKING:
    from pathlib import Path

    from doggo.dog.brain import Brain


class Fur(IntEnum):
    """The possible fur colors of the dog."""

    DARK_BROWN = 0
    LIGHT_BROWN = auto()
    GREY = auto()
    RED_BROWN = auto()
    WHITE = auto()
    WHITE_WITH_BROWN_SPOTS = auto()
    DARK_BROWN_WITH_GREY_SPOTS = auto()
    WHITE_WITH_GREY_SPOTS = auto()
    LIGHT_BROWN_WITH_WHITE_SPOTS = auto()
    ORANGE = auto()

    @classmethod
    def random(cls) -> Fur:
        """Return a random fur color."""
        fur_color = random.choice(list(cls))  # nosec
        logger.debug(f"Dog fur color: {fur_color.name}")

        return fur_color


class Body:
    """The body of the dog.

    Manage the sprite sheet of the dog based on the fur color.
    """

    def __init__(
        self,
        fur: Fur,
        sprite_size: tuple[int, int],
        default_direction: Direction,
        sprite_conf_per_state: dict[StateID, tuple[int, int]],
    ) -> None:
        """Initialize the body of the dog.

        Fur color is used to load the correct sprite sheet.
        Default direction is used to set the initial direction sprite.
        Sprite sheet size represents the number of sprites in the sprite sheet
        (columns, rows).
        States sprites config is a dictionary that contains the configuration of the
        sprites for each state.
        """
        assert sprite_conf_per_state.keys() == set(StateID), (
            f"Sprite configuration must be defined for all the states, missing: "
            f"{set(StateID) - sprite_conf_per_state.keys()}"
        )

        self.__asked_image: tuple[StateID, Direction] | None = None
        self.__current_image: Iterator[pg.Surface] | None = None
        self.fur: Fur = fur
        self.default_direction: Direction = default_direction

        nb_row, nb_column = sprite_size
        asset_path = ASSETS_PATH.joinpath(f"dogs/{fur:02d}.png")
        self.sprite_sheet = SpriteSheet(path=asset_path, columns=nb_column, rows=nb_row)

        self.images: dict[StateID, dict[Direction, list[pg.Surface]]] = defaultdict(
            lambda: defaultdict(list)
        )
        for state, (col, row) in sprite_conf_per_state.items():
            for direction in Direction:
                for i in range(col):
                    flip_x = direction != self.default_direction
                    sprite = self.sprite_sheet.get_sprite((i, row), flip_x=flip_x)
                    self.images[state][direction].append(sprite)

    def get_image(self, brain: Brain) -> pg.Surface:
        """Return the pose of the dog based on the brain config."""
        state = brain.current_state.id
        direction = brain.current_state.direction

        if self.__asked_image != (state, direction) or self.__current_image is None:
            self.__asked_image = (state, direction)
            self.__current_image = cycle(self.images[state][direction])

        return next(self.__current_image)


class SpriteSheet:
    """Load a sprite sheet and extract sprites from it."""

    def __init__(self, path: Path, rows: int, columns: int) -> None:
        self._sprite_sheet = pg.image.load(path).convert_alpha()
        self.columns = columns
        self.rows = rows
        self.sprite_size = (
            self._sprite_sheet.get_width() // columns,
            self._sprite_sheet.get_height() // rows,
        )

    def get_sprite(
        self, loc: tuple[int, int], flip_x: bool = False, flip_y: bool = False
    ) -> pg.Surface:
        """Return a sprite from the sprite sheet based on the location.

        The location is a tuple (column, row) of the sprite in the sprite sheet.
        """
        if loc[0] >= self.columns or loc[1] >= self.rows:
            raise ValueError(f"Sprite location is out of bounds: {loc}")

        x = loc[0] * self.sprite_size[0]
        y = loc[1] * self.sprite_size[1]

        area = pg.Rect(x, y, *self.sprite_size)
        image = pg.Surface(self.sprite_size, pg.SRCALPHA)
        image.blit(self._sprite_sheet, dest=(0, 0), area=area)

        if flip_x or flip_y:
            image = pg.transform.flip(image, flip_x, flip_y)

        return image
