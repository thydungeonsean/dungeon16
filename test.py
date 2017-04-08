from code.image.map_tile_set import MapTileSet
from code.states.test_state import TestState
import pygame

from code.map.map_generator import MapGenerator
from code.image.map_image_generator import MapImageGenerator


def change_screen():

    m = MapGenerator.load_map('test_map')
    m_image = MapImageGenerator.generate_image(m)
    m_image.draw(pygame.display.get_surface())

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
