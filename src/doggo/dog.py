from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from doggo.brain import Brain


class Dog:
    def __init__(self, brain: Brain) -> None:
        self.brain: Brain = brain
