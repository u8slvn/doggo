from __future__ import annotations

from typing import TYPE_CHECKING

from doggo.body import Body


if TYPE_CHECKING:
    import pygame as pg

    from doggo.brain import Brain


class Dog:
    """The doggo itself.

    It has a brain and a body. The first one is used to control the doggo's behavior,
    the second one is used to display it.
    """

    def __init__(self, brain: Brain, body: Body) -> None:
        self.brain: Brain = brain
        self.body: Body = body
        self.current_animation_time_rate: float = 0.0
        self.pose: pg.Surface = self.body.get_pose(brain=self.brain)

    def update(self, dt: float) -> None:
        """Update the doggo."""
        self.brain.update()

        self.current_animation_time_rate += dt
        if (
            self.current_animation_time_rate
            >= self.brain.current_state.animation_time_rate
        ):
            self.current_animation_time_rate = 0.0
            self.pose = self.body.get_pose(brain=self.brain)

    def move(self, surface: pg.Surface) -> None:
        """Move the doggo."""
        surface.blit(self.pose, dest=(10, 10))
