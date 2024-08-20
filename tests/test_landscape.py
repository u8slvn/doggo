from __future__ import annotations

from doggo.landscape import Biome
from doggo.landscape import LandscapeLayer


def test_get_random_biome():
    biome = Biome.random()

    assert isinstance(biome, Biome)
    assert biome in list(Biome)


def test_landscape_layer_draw_on_screen(pg_screen_mock):
    image = f"{Biome.MOUNTAIN:02d}_bg.png"
    landscape_layer = LandscapeLayer(image=image, topleft=(10, 10))

    landscape_layer.draw(pg_screen_mock)

    assert landscape_layer.rect.topleft == (10, 10)
    pg_screen_mock.blit.assert_called_once_with(
        landscape_layer.image, landscape_layer.rect
    )
