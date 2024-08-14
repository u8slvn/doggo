# Prepare module is responsible for building the World dependencies.
from __future__ import annotations

from doggo import config
from doggo.dog.body import Body
from doggo.dog.body import Fur
from doggo.dog.brain import Brain
from doggo.dog.dog import Dog
from doggo.landscape import Landscape
from doggo.landscape import StaticLandscape


def build_dog() -> Dog:
    """Build the dog."""
    brain = Brain.from_config(state_configs=config.DOG_STATES)
    body = Body(
        fur=Fur.random(),
        sprite_size=config.SPRITE_SIZE,
        default_direction=config.SPRITE_DIRECTION,
        sprite_conf_per_state=config.SPRITE_CONF_PER_STATE,
    )

    return Dog(
        brain=brain,
        body=body,
        world_ground=config.WORLD_GROUND,
        world_width=config.WORLD_WIDTH,
    )


def build_bg_landscape() -> Landscape:
    """Build the background landscape."""
    mountain = StaticLandscape(topleft=(0, 0), path="landscape/mountain.png")

    return Landscape(items=[mountain])


def build_fg_landscape() -> Landscape:
    """Build the foreground landscape."""
    ground = StaticLandscape(
        topleft=(0, config.WORLD_GROUND), path="landscape/ground.png"
    )

    return Landscape(items=[ground])
