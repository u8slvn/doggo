# Prepare module is responsible for building the World dependencies.
from __future__ import annotations

from doggo.dog.body import Body
from doggo.dog.body import Fur

from doggo import config
from doggo.dog.brain import Brain
from doggo.dog.brain import State
from doggo.dog.dog import Dog
from doggo.landscape import Ground
from doggo.landscape import Landscape


def build_dog() -> Dog:
    """Build the dog."""
    states = [State(**state_config) for state_config in config.DOG_STATES]

    brain = Brain(states=states)
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


def build_landscape() -> Landscape:
    """Build the landscape."""
    ground = Ground(height=config.WORLD_GROUND)

    return Landscape(items=[ground])
