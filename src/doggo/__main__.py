from __future__ import annotations

from time import sleep

from loguru import logger

from doggo.brain import Brain


def run() -> None:
    brain = Brain()

    logger.info("Starting brain...")
    while True:
        brain.update()
        logger.info(
            f"Brain: {brain.is_doing()} - {brain.current_state.time} seconds left..."
        )
        sleep(1)


if __name__ == "__main__":
    run()
