import pygame

from code.image.map_image.map_image_generator import MapImageGenerator
from code.map.map_generator import MapGenerator
from code.states.test_state import TestState
from code.map.tileset_zone import TilesetZone


def change_screen():

    m = MapGenerator.load_map('test_map')
    # z = TilesetZone((0, 0), 7, 6, 'wall', 'ruin')
    # z2 = TilesetZone((0, 0), 7, 6, 'floor', 'grass')
    # m.generate_zone_map()
    # m.zone_map.add_zone(z)
    # m.zone_map.add_zone(z2)
    m_image = MapImageGenerator.generate_image(m)
    m_image.draw(pygame.display.get_surface(), 'a')


def test():

    pygame.init()
    pygame.display.set_mode((800, 600))

    state = TestState()
    state.init_state()
    
    change_screen()

    while True:

        state.render()

        state.run()
        state.handle_input()

        pygame.display.update()
        state.clock.tick(60)
        
        
if __name__ == '__main__':
    test()
