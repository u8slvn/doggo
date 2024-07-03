from __future__ import annotations

from doggo import mind
from doggo.brain import Brain
from doggo.world import World


def run() -> None:
    _ = Brain(states=mind.STATES)

    control = World(width=80, height=24)
    control.start()


if __name__ == "__main__":
    run()
