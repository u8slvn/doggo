from __future__ import annotations

import random

from enum import IntEnum
from enum import auto

import numpy as np


class StateID(IntEnum):
    """The possible states of the dog."""

    IDLE = 0
    IDLE_AND_BARK = auto()
    WALK = auto()
    WALK_AND_BARK = auto()
    SIT = auto()
    SIT_AND_BARK = auto()
    LIE_DOWN = auto()
    LIE_DOWN_AND_BARK = auto()
    RUN = auto()
    RUN_AND_BARK = auto()
    STAND = auto()
    STAND_AND_BARK = auto()
    SLEEP = auto()

    @classmethod
    def random(cls) -> StateID:
        """Return a random state."""
        return random.choice(list(cls))  # nosec

    @classmethod
    def random_with_probs(cls, p: list[float]) -> StateID:
        """Return a random state based on the given probabilities."""
        return cls(np.random.choice(list(cls), p=p))

    def __str__(self) -> str:
        """Human-readable representation of the state."""
        return self.name.replace("_", " ")
