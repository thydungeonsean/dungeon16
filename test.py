from code.image.map_tile_set import MapTileSet
from code.states.test_state import TestState
import pygame


def change_screen():
    t = MapTileSet('floor', 'cave')
    ta = t.get_tile_image('var_a')
    tr = ta.get_rect()
    pygame.display.get_surface().blit(ta, tr)


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