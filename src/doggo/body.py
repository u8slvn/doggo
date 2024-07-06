from __future__ import annotations

from typing import TYPE_CHECKING

import pygame as pg

from doggo import ASSETS_PATH
from doggo.dna import Fur
from doggo.mind import Direction
from doggo.mind import StateID


if TYPE_CHECKING:
    from pathlib import Path


class Body:
    """The body of the doggo.

    Manage the sprite sheet of the doggo based on the fur color.
    """

    def __init__(
        self,
        fur: Fur,
        sprite_size: tuple[int, int],
        default_direction: Direction,
        sprite_conf_per_state: dict[StateID, tuple[int, int]],
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

        nb_row, nb_column = sprite_size
        asset_path = ASSETS_PATH.joinpath(f"dogs-{fur:02d}.png")
        self.sprite_sheet = SpriteSheet(path=asset_path, columns=nb_column, rows=nb_row)

        self.poses: dict[StateID, dict[Direction, list[pg.Surface]]] = {}

        for state, (col, row) in sprite_conf_per_state.items():
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

    def __init__(self, path: Path, rows: int, columns: int) -> None:
        self._sprite_sheet = pg.image.load(path).convert_alpha()
        self.columns = columns
        self.rows = rows
        self.sprite_size = (
            self._sprite_sheet.get_width() // columns,
            self._sprite_sheet.get_height() // rows,
        )
        print(self._sprite_sheet.get_width())
        print(self.sprite_size)

    def get_sprite(
        self, loc: tuple[int, int], flip_x: bool = False, flip_y: bool = False
    ) -> pg.Surface:
        """Return a sprite from the sprite sheet based on the location."""
        if loc[0] >= self.rows or loc[1] >= self.columns:
            raise ValueError("Sprite location is out of bounds")

        x = loc[0] * self.sprite_size[0]
        y = loc[1] * self.sprite_size[1]

        area = pg.Rect(x, y, *self.sprite_size)
        image = pg.Surface(self.sprite_size, pg.SRCALPHA)
        image.blit(self._sprite_sheet, dest=(0, 0), area=area)

        if flip_x or flip_y:
            image = pg.transform.flip(image, flip_x, flip_y)

        return image
