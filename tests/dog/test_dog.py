from __future__ import annotations

import pytest

from doggo.dog import StateID
from doggo.dog.brain import Direction
from doggo.prepare import build_dog


def test_dog_can_move_right():
    dog = build_dog()
    dog.brain.change_state(StateID.WALK)  # We need a state that can move.
    dog.brain.current_state.direction = Direction.RIGHT
    start_x_pos = dog.rect.x

    dog.update(dt=1.0)

    assert dog.rect.x > start_x_pos


def test_dog_can_move_left():
    dog = build_dog()
    dog.brain.change_state(StateID.WALK)  # We need a state that can move.
    dog.brain.current_state.direction = Direction.LEFT
    start_x_pos = dog.rect.x

    dog.update(dt=1.0)

    assert dog.rect.x < start_x_pos


@pytest.mark.parametrize(
    "direction, start_pos, x_signe",
    [
        (Direction.RIGHT, lambda dog: dog.world_width - dog.rect.width, -1),
        (Direction.LEFT, lambda dog: 0, 1),
    ],
)
def test_dog_clone_appeared_when_hitting_a_world_boundary(
    direction, start_pos, x_signe
):
    dog = build_dog()
    dog.brain.change_state(StateID.WALK)  # We need a state that can move.
    dog.brain.current_state.direction = direction
    dog.x = dog.rect.x = start_pos(dog)  # Place the dog at the max direction boundary.

    assert dog.clone.visible is False

    dog.update(dt=1.0)

    assert dog.clone.visible is True
    # The clone should appear on the left side of the world showing only the right part
    # of the dog hidden by the boundary.
    assert dog.clone.rect.x == dog.rect.x + dog.world_width * x_signe


@pytest.mark.parametrize(
    "direction, start_pos",
    [
        (Direction.RIGHT, lambda dog: dog.world_width - dog.rect.width),
        (Direction.LEFT, lambda dog: 0),
    ],
)
def test_dog_clone_disappeared_when_not_hitting_a_world_boundary(direction, start_pos):
    dog = build_dog()
    dog.brain.change_state(StateID.WALK)
    dog.brain.current_state.direction = direction
    dog.brain.current_state.countdown = 100  # Make sure the dog will not change state.
    dog.x = dog.rect.x = start_pos(dog)
    dog.update(dt=1.0)

    assert dog.clone.visible is True

    # First update a huge timeframe should move the dog outside the boundary.
    dog.update(dt=3.0)
    clone_last_x_pos = dog.clone.rect.x

    # Second update with a null timeframe, the clone should disappear and the dog should
    # take the last position of the clone.
    dog.update(dt=0.0)

    assert clone_last_x_pos == dog.x
    assert dog.clone.visible is False


def test_dog_draw_on_screen(pg_screen_mock):
    dog = build_dog()

    dog.draw(screen=pg_screen_mock)

    pg_screen_mock.blit.assert_called_once_with(dog.image, dest=dog.rect)


def test_dog_draw_on_screen_with_its_clone(mocker, pg_screen_mock):
    dog = build_dog()
    dog.clone.visible = True

    dog.draw(screen=pg_screen_mock)

    assert pg_screen_mock.blit.call_count == 2
    assert pg_screen_mock.blit.call_args_list == [
        mocker.call(dog.image, dest=dog.rect),
        mocker.call(dog.image, dest=dog.clone.rect),
    ]


def test_dog_brain_info_are_accessible_from_dog():
    dog = build_dog()

    assert isinstance(dog.current_state, StateID)
    assert isinstance(dog.speed, int)
    assert isinstance(dog.direction, Direction)
