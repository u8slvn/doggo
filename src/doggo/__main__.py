from __future__ import annotations

from time import sleep

from loguru import logger

from doggo import mind
from doggo.brain import Brain


def run() -> None:
    brain = Brain(states=mind.STATES)

    logger.info("Starting brain...")
    while True:
        brain.update()
        logger.info(
            f"Brain: {brain.is_doing()} - Direction: {brain.direction.name} - {brain.current_state_time} seconds left..."
        )
        sleep(1)


if __name__ == "__main__":
    run()
