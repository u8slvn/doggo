from __future__ import annotations

import pygame as pg


class DraggableWindow:
    """A draggable window.

    Allow the user to drag the window by clicking and dragging it.
    """

    def __init__(self) -> None:
        self.start_position = pg.Vector2(pg.display.get_window_position())
        self.dragged = False

    def process_event(self, event: pg.event.Event) -> None:
        """Process the event to drag the window."""
        if event.type == pg.MOUSEBUTTONDOWN:
            self.dragged = True
            self.start_position = pg.Vector2(pg.mouse.get_pos())
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_SIZEALL)

        elif event.type == pg.MOUSEMOTION:
            if self.dragged:
                window_position = pg.Vector2(pg.display.get_window_position())
                mouse_position = pg.Vector2(pg.mouse.get_pos())

                pg.display.set_window_position(
                    window_position + mouse_position - self.start_position
                )

        elif event.type == pg.MOUSEBUTTONUP:
            self.dragged = False
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
