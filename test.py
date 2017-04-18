import pygame

from source.image.map_image.map_image_generator import MapImageGenerator
from source.map.map_generator import MapGenerator


from source.states.test_state import TestState
from source.states.game_state import GameState

from source.objects.dummy import Dummy
from source.map.tileset_zone import TilesetZone
from source.image.tilesets.tileset_archive import TileSetArchive


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

    player = Dummy(10, 10)
    state.view.bind_view(player)

    while True:

        state.render()

        state.run()

        state.handle_input()

        pygame.display.update()
        state.clock.tick(60)
        
        
if __name__ == '__main__':
    test()
