from __future__ import annotations

from doggo.brain import Brain
from doggo.brain import State
from doggo.brain import StateConfig
from doggo.logger import get_logger


logger = get_logger()


def run() -> None:
    brain = Brain(
        states=[
            StateConfig(
                state=State.IDLE,
                text="I'm just chilling",
                transitions={
                    State.IDLE: 0.2,
                    State.WALK: 0.2,
                    State.SIT: 0.2,
                    State.RUN: 0.2,
                    State.EAT: 0.2,
                },
                time_range=(1, 5),
            ),
            StateConfig(
                state=State.WALK,
                text="I'm going for a walk",
                transitions={
                    State.IDLE: 0.2,
                    State.WALK: 0.2,
                    State.SIT: 0.2,
                    State.RUN: 0.2,
                    State.EAT: 0.2,
                },
                time_range=(1, 5),
            ),
            StateConfig(
                state=State.SIT,
                text="I'm sitting",
                transitions={
                    State.IDLE: 0.2,
                    State.WALK: 0.2,
                    State.SIT: 0.2,
                    State.RUN: 0.2,
                    State.EAT: 0.2,
                },
                time_range=(1, 5),
            ),
            StateConfig(
                state=State.RUN,
                text="I'm running",
                transitions={
                    State.IDLE: 0.2,
                    State.WALK: 0.2,
                    State.SIT: 0.2,
                    State.RUN: 0.2,
                    State.EAT: 0.2,
                },
                time_range=(1, 5),
            ),
            StateConfig(
                state=State.EAT,
                text="I'm eating",
                transitions={
                    State.IDLE: 0.2,
                    State.WALK: 0.2,
                    State.SIT: 0.2,
                    State.RUN: 0.2,
                    State.EAT: 0.2,
                },
                time_range=(1, 5),
            ),
        ]
    )

    logger.info("Starting brain...")
    logger.info(f"Brain status: {brain.is_doing()}")


if __name__ == "__main__":
    run()
