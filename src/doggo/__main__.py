from __future__ import annotations

from loguru import logger

from doggo.brain import Brain
from doggo.brain import StateConfig
from doggo.brain import StateID


def run() -> None:
    brain = Brain(
        states=[
            StateConfig(
                state=StateID.IDLE,
                text="I'm just chilling",
                transitions={
                    StateID.IDLE: 0.2,
                    StateID.WALK: 0.2,
                    StateID.SIT: 0.2,
                    StateID.RUN: 0.2,
                    StateID.EAT: 0.2,
                },
                time_range=(1, 5),
            ),
            StateConfig(
                state=StateID.WALK,
                text="I'm going for a walk",
                transitions={
                    StateID.IDLE: 0.2,
                    StateID.WALK: 0.2,
                    StateID.SIT: 0.2,
                    StateID.RUN: 0.2,
                    StateID.EAT: 0.2,
                },
                time_range=(1, 5),
            ),
            StateConfig(
                state=StateID.SIT,
                text="I'm sitting",
                transitions={
                    StateID.IDLE: 0.2,
                    StateID.WALK: 0.2,
                    StateID.SIT: 0.2,
                    StateID.RUN: 0.2,
                    StateID.EAT: 0.2,
                },
                time_range=(1, 5),
            ),
            StateConfig(
                state=StateID.RUN,
                text="I'm running",
                transitions={
                    StateID.IDLE: 0.2,
                    StateID.WALK: 0.2,
                    StateID.SIT: 0.2,
                    StateID.RUN: 0.2,
                    StateID.EAT: 0.2,
                },
                time_range=(1, 5),
            ),
            StateConfig(
                state=StateID.EAT,
                text="I'm eating",
                transitions={
                    StateID.IDLE: 0.2,
                    StateID.WALK: 0.2,
                    StateID.SIT: 0.2,
                    StateID.RUN: 0.2,
                    StateID.EAT: 0.2,
                },
                time_range=(1, 5),
            ),
        ]
    )

    logger.info("Starting brain...")
    logger.info(f"Brain status: {brain.is_doing()}")


if __name__ == "__main__":
    run()
