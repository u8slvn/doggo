from __future__ import annotations

import random

from typing import TYPE_CHECKING

from doggo.body import Body
from doggo.config import WORLD_WIDTH
from doggo.mind import Direction


if TYPE_CHECKING:
    import pygame as pg

    from doggo.brain import Brain
    from doggo.mind import StateID


class Dog:
    """The doggo itself.

    It has a brain and a body. The first one is used to control the doggo's behavior,
    the second one is used to display it.
    """

    def __init__(self, brain: Brain, body: Body, y: int = 20) -> None:
        self.brain: Brain = brain
        self.body: Body = body
        self.current_animation_time_rate: float = 0.0
        self.pose: pg.Surface = self.body.get_pose(brain=self.brain)
        self.rect = self.pose.get_rect()
        self.x = float(random.randint(0, WORLD_WIDTH - self.rect.width))
        self.rect.topleft = (int(self.x), y)
        self.clone: BoundaryClone = BoundaryClone(self)

    @property
    def direction(self) -> Direction:
        """ "The current direction of the doggo."""
        return self.brain.current_state.direction

    @property
    def speed(self) -> int:
        """The current speed of the doggo."""
        return self.brain.current_state.speed

    @property
    def current_state(self) -> StateID:
        """The current state of the doggo."""
        return self.brain.current_state.id

    def update(self, dt: float) -> None:
        """Update the doggo."""
        self.brain.update()

        # Manage the doggo's animation.
        self.current_animation_time_rate += dt
        if (
            self.current_animation_time_rate
            >= self.brain.current_state.animation_time_rate
        ):
            self.current_animation_time_rate = 0.0
            self.pose = self.body.get_pose(brain=self.brain)

        # Manage world boundaries.
        if self.rect.right < 0:
            self.x = WORLD_WIDTH - self.rect.width
        elif self.rect.left > WORLD_WIDTH:
            self.x = 0

        # Move the doggo.
        if self.direction == Direction.LEFT:
            self.x -= self.speed * dt
        else:
            self.x += self.speed * dt
        self.rect.x = int(self.x)
        self.clone.update()  # Don't forget to update the clone after the doggo.

    def render(self, surface: pg.Surface) -> None:
        """Move the doggo."""
        self.clone.render(surface=surface)
        surface.blit(self.pose, dest=self.rect)


class BoundaryClone:
    """Boundary clone.

    Doggo clone that appears on the opposite side of the world when the doggo crosses
    a boundary.
    """

    def __init__(self, dog: Dog) -> None:
        self.dog = dog
        self.visible = False
        self.rect = dog.rect.copy()

    def update(self) -> None:
        """Update the clone."""
        if self.dog.rect.left < 0:
            self.visible = True
            self.rect.x = self.dog.rect.x + WORLD_WIDTH
        elif self.dog.rect.right > WORLD_WIDTH:
            self.visible = True
            self.rect.x = self.dog.rect.x - WORLD_WIDTH
        else:
            self.visible = False

    def render(self, surface: pg.Surface) -> None:
        """Render the clone."""
        if self.visible:
            surface.blit(self.dog.pose, dest=self.rect)
