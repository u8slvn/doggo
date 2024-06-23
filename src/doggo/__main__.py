from __future__ import annotations

from loguru import logger

from doggo.brain import Brain


def run() -> None:
    brain = Brain()

    logger.info("Starting brain...")
    logger.info(f"Brain status: {brain.is_doing()}")


if __name__ == "__main__":
    run()
