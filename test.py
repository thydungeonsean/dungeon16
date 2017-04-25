import pygame

from source.image.map_image.map_image_generator import MapImageGenerator
from source.map.map_generator import MapGenerator


from source.states.test_state import TestState
from source.states.game_state import GameState

from source.objects.dummy import Dummy
from source.objects.map_object import MapObject
from source.map.tileset_zone import TilesetZone
from source.image.tilesets.tileset_archive import TileSetArchive

from source.states.settings import Settings

from source.controller.move_control import MoveControl
from source.objects.coord import Coord
from source.objects.pixel_coord import PixelCoord

def gen():

    TileSetArchive.init_set_keys()

    m = MapGenerator.load_map('map')
    # z = TilesetZone((10, 0), 7, 6, 'water', 'blue')
    # z2 = TilesetZone((0, 0), 12, 9, 'floor', 'tile_floor_d')
    # m.generate_zone_map()
    # m.zone_map.add_zone(z)
    # m.zone_map.add_zone(z2)

    return m


def render(m_image):
    m_image.draw(pygame.display.get_surface())


def test():

    pygame.init()
    pygame.display.set_mode((800, 600))

    m = gen()

    state = GameState()
    state.load_level(m)
    state.init_state()

    x = 10
    y = 10

    player = Dummy(x, y)
    state.view.focus_object(player)
    MoveControl(player)

    c = state.view.coord.get

    x = MapObject((9, 11))
    y = MapObject((10, 11))
    z = MapObject((11, 11))
    m.feature_map.add_feature((9, 11), x)
    m.feature_map.add_feature((10, 11), y)
    m.feature_map.add_feature((11, 11), z)

    while True:

        state.render()
        draw_focus()

        state.run()

        state.handle_input()

        c = print_coord(state.view, c)

        pygame.display.update()
        state.clock.tick(60)


def draw_focus():
    s = pygame.display.get_surface()
    x_offset = ((25 - 1) / 2) * Settings.SC_TILE_W
    y_offset = ((17 - 1) / 2) * Settings.SC_TILE_H
    i = pygame.Surface((Settings.SC_TILE_W, Settings.SC_TILE_H))
    i.fill((230, 10, 15))
    i2 = pygame.Surface((Settings.SC_TILE_W-2, Settings.SC_TILE_H-2))
    r2 = i2.get_rect()
    r2.topleft = (1, 1)
    i2.fill((255, 255, 255))
    i.blit(i2, r2)
    i.set_colorkey((255, 255, 255))
    r = i.get_rect()
    r.topleft = (x_offset, y_offset)
    s.blit(i, r)


def print_coord(v, c):

    if c != v.coord.get:
        print v.coord.get
        return v.coord.get
    return c


if __name__ == '__main__':
    test()
