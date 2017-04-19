import pygame

from source.image.map_image.map_image_generator import MapImageGenerator
from source.map.map_generator import MapGenerator


from source.states.test_state import TestState
from source.states.game_state import GameState

from source.objects.dummy import Dummy
from source.map.tileset_zone import TilesetZone
from source.image.tilesets.tileset_archive import TileSetArchive

from source.states.settings import Settings


def gen():

    TileSetArchive.init_set_keys()

    m = MapGenerator.load_map('test_map')
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

    #state = TestState()
    state = GameState()
    state.load_level(m)
    state.init_state()

    x = 1
    y = 2

    player = Dummy(x, y)
    player.pixel_coord.set((100, 100))
    state.view.focus_object(player)

    while True:

        state.render()
        draw_focus()

        state.run()

        state.handle_input()

        pygame.display.update()
        state.clock.tick(60)


def draw_focus():
    s = pygame.display.get_surface()
    x_offset = ((25 - 1) / 2) * Settings.SC_TILE_W
    y_offset = ((17 - 1) / 2) * Settings.SC_TILE_H
    i = pygame.Surface((Settings.SC_TILE_W, Settings.SC_TILE_H))
    i.fill((230, 10, 15))
    i2 = pygame.Surface((Settings.SC_TILE_W - 2 , Settings.SC_TILE_H-2))
    r2 = i2.get_rect()
    r2.topleft = (1, 1)
    i2.fill((255, 255, 255))
    i.blit(i2, r2)
    i.set_colorkey((255, 255, 255))
    r = i.get_rect()
    r.topleft = (x_offset, y_offset)
    s.blit(i, r)
        
if __name__ == '__main__':
    test()
