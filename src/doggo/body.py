from __future__ import annotations

import random

from enum import IntEnum
from enum import auto

import pygame as pg

from doggo import ASSETS_PATH
from doggo.brain import Direction
from doggo.brain import StateID


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
    # TODO: split this class into two classes: Body and generic SpriteSheet
    """The body of the doggo.

    Manage the sprite sheet of the doggo based on the fur color.
    """

    # sprite_size = (64, 48)
    # default_direction = Direction.LEFT

    def __init__(
        self, sprite_size: tuple[int, int], direction: Direction, fur: Fur
    ) -> None:
        self.fur: Fur = fur
        self.sprite_size: tuple[int, int] = sprite_size
        self.default_direction: Direction = direction

        asset_path = ASSETS_PATH.joinpath(f"dogs_{fur:02d}.png")
        self._sprite_sheet = pg.image.load(str(asset_path)).convert_alpha()

        self.poses: dict[StateID, dict[Direction, pg.Surface]] = self._build_poses()

    def _build_poses(self) -> dict[StateID, dict[Direction, pg.Surface]]:
        """Build the sprites of the doggo based on the fur color."""
        return {state: self.get_sprites(state) for state in StateID}

    def get_pose(self, state: StateID, direction: Direction) -> pg.Surface:
        """Return the pose of the doggo based on the state and the direction."""
        return self.poses[state][direction]

    def get_sprites(self, state: StateID) -> dict[Direction, pg.Surface]:
        """Return the sprites of the doggo based on the state."""
        return {direction: self.get_sprite(state, direction) for direction in Direction}

    def get_sprite(self, state: StateID, direction: Direction) -> pg.Surface:
        """Return the sprite of the doggo based on the state and the direction."""
        x = 0
        y = 0

        area = pg.Rect(x, y, *self.sprite_size)
        image = pg.Surface(self.sprite_size, pg.SRCALPHA)
        image.blit(self._sprite_sheet, dest=(0, 0), area=area)

        if direction is not self.default_direction:
            image = pg.transform.flip(image, flip_x=True, flip_y=False)

        return image
