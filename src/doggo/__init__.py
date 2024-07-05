from __future__ import annotations

from importlib import metadata
from pathlib import Path


__app_name__ = "doggo"
__version__ = metadata.version(__app_name__)

ROOT_PATH = Path(__file__).parent
ASSETS_PATH = ROOT_PATH.joinpath("assets")
