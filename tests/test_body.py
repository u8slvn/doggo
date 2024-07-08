from __future__ import annotations

import pygame as pg
import pytest

from doggo import ASSETS_PATH
from doggo.dog.body import SpriteSheet


def test_sprite_sheet_get_sprite_returns_a_sprite():
    sprite_sheet_path = ASSETS_PATH.joinpath("dogs-00.png")
    sprite_sheet = SpriteSheet(path=sprite_sheet_path, columns=8, rows=9)

    sprite = sprite_sheet.get_sprite(loc=(0, 0))

    assert isinstance(sprite, pg.Surface)
    assert sprite.get_width() == 64
    assert sprite.get_height() == 48


def test_sprite_sheet_get_sprite_fails_if_loc_is_outside_of_the_sheet():
    sprite_sheet_path = ASSETS_PATH.joinpath("dogs-00.png")
    sprite_sheet = SpriteSheet(path=sprite_sheet_path, columns=8, rows=9)

    with pytest.raises(ValueError, match="Sprite location is out of bounds"):
        sprite_sheet.get_sprite(loc=(8, 9))
