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

    def update(self, dt: float) -> None:
        """Update the doggo."""
        self.brain.update()

    def move(self, surface: pg.Surface) -> None:
        """Move the doggo."""
        pose = self.body.get_pose(
            self.brain.current_state.id, self.brain.current_state.direction
        )
        surface.blit(pose, (10, 10))
