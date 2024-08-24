from __future__ import annotations

import sys

from pathlib import Path

from doggo.config import COMPILED_ENV


if COMPILED_ENV:
    ROOT_PATH = Path(sys._MEIPASS)  # type: ignore
elif __file__:
    ROOT_PATH = Path(__file__).parent
ASSETS_PATH = ROOT_PATH.joinpath("assets")
