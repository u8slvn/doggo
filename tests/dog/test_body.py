from __future__ import annotations

import pygame as pg
import pytest

from doggo import ASSETS_PATH
from doggo import config
from doggo.dog import StateID
from doggo.dog.body import Body
from doggo.dog.body import Fur
from doggo.dog.body import SpriteSheet
from doggo.dog.brain import Brain
from doggo.dog.brain import Direction


def test_fur_random_returns_a_fur_color():
    fur = Fur.random()

    assert isinstance(fur, Fur)


def test_body_get_image_returns_surface_cyclically(pygame_test):
    body = Body(
        fur=Fur.random(),
        sprite_size=config.SPRITE_SIZE,
        default_direction=config.SPRITE_DIRECTION,
        sprite_conf_per_state=config.SPRITE_CONF_PER_STATE,
    )
    # Take SLEEP state for testing because it has only 4 frames.
    brain = Brain.from_config(
        state_configs=config.DOG_STATES, default_state_id=StateID.SLEEP
    )
    frames = []

    # Test the first cyclic of the get_image method.
    for index in range(0, config.SPRITE_CONF_PER_STATE[StateID.SLEEP][0]):
        image = body.get_image(brain=brain)
        frames.append(image)

        assert isinstance(image, pg.Surface)
        assert image is body.images[StateID.SLEEP][brain.current_state.direction][index]

    # The next call should return the first frame.
    next_cycle_image = body.get_image(brain=brain)
    assert next_cycle_image is frames[0]


def test_body_return_cycle_images_while_brain_state_is_the_same(pygame_test):
    body = Body(
        fur=Fur.random(),
        sprite_size=config.SPRITE_SIZE,
        default_direction=config.SPRITE_DIRECTION,
        sprite_conf_per_state=config.SPRITE_CONF_PER_STATE,
    )
    brain = Brain.from_config(
        state_configs=config.DOG_STATES, default_state_id=StateID.SLEEP
    )
    brain.current_state.direction = Direction.LEFT

    first_image = body.get_image(brain=brain)
    second_image = body.get_image(brain=brain)

    assert first_image is body.images[StateID.SLEEP][Direction.LEFT][0]
    assert second_image is body.images[StateID.SLEEP][Direction.LEFT][1]

    # Change the brain state to test the switch of the images.
    brain.change_state(StateID.IDLE)
    brain.current_state.direction = Direction.RIGHT

    third_image = body.get_image(brain=brain)
    fourth_image = body.get_image(brain=brain)

    assert third_image is body.images[StateID.IDLE][Direction.RIGHT][0]
    assert fourth_image is body.images[StateID.IDLE][Direction.RIGHT][1]


def test_sprite_sheet_get_sprite_returns_a_sprite(pygame_test):
    sprite_sheet_path = ASSETS_PATH.joinpath("dogs/00.png")
    sprite_sheet = SpriteSheet(path=sprite_sheet_path, columns=8, rows=9)

    sprite = sprite_sheet.get_sprite(loc=(0, 0))

    assert isinstance(sprite, pg.Surface)
    assert sprite.get_width() == 64
    assert sprite.get_height() == 48


def test_sprite_sheet_get_sprite_fails_if_loc_is_outside_of_the_sheet(pygame_test):
    sprite_sheet_path = ASSETS_PATH.joinpath("dogs/00.png")
    sprite_sheet = SpriteSheet(path=sprite_sheet_path, columns=8, rows=9)

    with pytest.raises(ValueError, match="Sprite location is out of bounds"):
        sprite_sheet.get_sprite(loc=(8, 9))
