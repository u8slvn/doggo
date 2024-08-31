from __future__ import annotations

from doggo.dog.body import Body
from doggo.dog.brain import Brain
from doggo.dog.brain import State
from doggo.dog.dog import Dog
from doggo.landscape import Landscape
from doggo.landscape import LandscapeLayer
from doggo.prepare import build_dog
from doggo.prepare import build_landscape


def test_build_dog(pygame_test):
    dog = build_dog()

    assert isinstance(dog, Dog)
    assert isinstance(dog.brain, Brain)
    assert isinstance(dog.brain.current_state, State)
    assert isinstance(dog.body, Body)


def test_build_landscape(pygame_test):
    landscape = build_landscape()

    assert isinstance(landscape, Landscape)
    assert isinstance(landscape.background, LandscapeLayer)
    assert isinstance(landscape.foreground, LandscapeLayer)
