from __future__ import annotations

from typing import cast

import pygame as pg


class DraggableWindow:
    """A draggable window.

    Allow the user to drag the window by clicking and dragging it.
    """

    def __init__(self, window: pg.window.Window) -> None:
        self.window: pg.window.Window = window
        self.start_position = pg.Vector2(self.window.position)
        self.dragged = False

    def process_event(self, event: pg.event.Event) -> None:
        """Process the event to drag the window."""
        if event.type == pg.MOUSEBUTTONDOWN:
            self.dragged = True
            self.start_position = pg.Vector2(pg.mouse.get_pos())
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_SIZEALL)

        elif event.type == pg.MOUSEMOTION:
            if self.dragged:
                window_position = pg.Vector2(self.window.position)
                mouse_position = pg.Vector2(pg.mouse.get_pos())

                self.window.position = cast(
                    tuple[int, int],
                    window_position + mouse_position - self.start_position,
                )

        elif event.type == pg.MOUSEBUTTONUP:
            self.dragged = False
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
