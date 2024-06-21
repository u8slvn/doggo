from __future__ import annotations

import logging

from types import MappingProxyType

from doggo import __app_name__


_logger: logging.Logger | None = None


class LogColor:
    WHITE = "\x1b[97;20m"
    GREY = "\x1b[37;20m"
    CYAN = "\x1b[36;20m"
    YELLOW = "\x1b[33;20m"
    RED = "\x1b[31;20m"
    RED_BACKGROUND = "\x1b[97;41m"
    RESET = "\x1b[0m"


class ColorFormatter(logging.Formatter):
    log_format = "{level}[%(levelname)s]{reset} {base}%(message)s{reset}"
    log_level_colors = MappingProxyType(
        {
            logging.DEBUG: (LogColor.GREY, LogColor.GREY),
            logging.INFO: (LogColor.WHITE, LogColor.CYAN),
            logging.WARNING: (LogColor.WHITE, LogColor.YELLOW),
            logging.ERROR: (LogColor.WHITE, LogColor.RED),
            logging.CRITICAL: (LogColor.RED, LogColor.RED_BACKGROUND),
        }
    )
    log_level_default = log_level_colors[logging.DEBUG]

    def format(self, record: logging.LogRecord) -> str:
        base, level = self.log_level_colors.get(record.levelno, self.log_level_default)
        log_format = self.log_format.format(
            base=base, level=level, reset=LogColor.RESET
        )
        formatter = logging.Formatter(log_format)
        return formatter.format(record)


def get_logger() -> logging.Logger:
    global _logger

    if _logger is None:
        logger = logging.getLogger(__app_name__)
        logger.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(ColorFormatter())

        logger.addHandler(ch)

        _logger = logger

    return _logger
