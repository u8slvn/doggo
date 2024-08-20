from __future__ import annotations

import pygame as pg

from doggo.ui import DraggableWindow


def test_draggable_window_change_cursor_when_clicked(pg_window_mock, pg_mouse_mock):
    pg_mouse_mock.get_pos.return_value = (10, 10)
    draggable_window = DraggableWindow(window=pg_window_mock)
    mouse_down_event = pg.event.Event(pg.MOUSEBUTTONDOWN)
    mouse_up_event = pg.event.Event(pg.MOUSEBUTTONUP)

    # Click the window
    draggable_window.process_event(mouse_down_event)

    assert draggable_window.dragged is True
    assert draggable_window.start_position == pg.Vector2(10, 10)
    pg_mouse_mock.set_cursor.assert_called_once_with(pg.SYSTEM_CURSOR_SIZEALL)

    # Release the window
    draggable_window.process_event(mouse_up_event)

    assert draggable_window.dragged is False
    pg_mouse_mock.set_cursor.assert_called_with(pg.SYSTEM_CURSOR_ARROW)


def test_draggable_window_can_be_moved_around(pg_window_mock, pg_mouse_mock):
    pg_mouse_mock.get_pos.side_effect = [(10, 10), (20, 20), (30, 30)]
    draggable_window = DraggableWindow(window=pg_window_mock)
    mouse_down_event = pg.event.Event(pg.MOUSEBUTTONDOWN)
    mouse_motion_event = pg.event.Event(pg.MOUSEMOTION)

    # Click the window
    draggable_window.process_event(mouse_down_event)

    # Move the window a first time
    draggable_window.process_event(mouse_motion_event)

    assert draggable_window.window.position == (10, 10)

    # Move the window a second time
    draggable_window.process_event(mouse_motion_event)

    assert draggable_window.window.position == (30, 30)
