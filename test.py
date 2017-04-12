import pygame

from code.image.map_image.map_image_generator import MapImageGenerator
from code.map.map_generator import MapGenerator
from code.states.test_state import TestState

from code.map.tileset_zone import TilesetZone
from code.image.tilesets.tileset_archive import TileSetArchive


def change_screen():

    TileSetArchive.init_set_keys()

    m = MapGenerator.load_map('test_map')
    # z = TilesetZone((10, 0), 7, 6, 'water', 'blue')
    # z2 = TilesetZone((0, 0), 7, 6, 'floor', 'cave_floor')
    # m.generate_zone_map()
    # m.zone_map.add_zone(z)
    # m.zone_map.add_zone(z2)
    m_image = MapImageGenerator.generate_image(m)
    return m_image


def render(m_image):
    m_image.draw(pygame.display.get_surface())


def test():

    pygame.init()
    pygame.display.set_mode((800, 600))

    state = TestState()
    state.init_state()
    
    m = change_screen()
    state.render = render

    while True:

        state.render(m)

        state.run()
        state.handle_input()

        pygame.display.update()
        state.clock.tick(60)
        
        
if __name__ == '__main__':
    test()
