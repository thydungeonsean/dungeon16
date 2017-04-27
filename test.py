import pygame

from source.controller.move_control import MoveControl
from source.image.tilesets.tileset_archive import TileSetArchive
from source.map.level.level_generator import LevelGenerator
from source.map.map_generator import MapGenerator
from source.objects.map_objects.actor import Actor
from source.objects.map_objects.door import Door
from source.states.game_state import GameState
from source.states.settings import Settings


def gen():

    l = LevelGenerator.load_level('map')

    m = MapGenerator.load_map('map')
    # z = TilesetZone((10, 0), 7, 6, 'water', 'blue')
    # z2 = TilesetZone((0, 0), 12, 9, 'floor', 'tile_floor_d')
    # m.generate_zone_map()
    # m.zone_map.add_zone(z)
    # m.zone_map.add_zone(z2)

    return l


def render(m_image):
    m_image.draw(pygame.display.get_surface())


def test():

    # basic init functions
    pygame.init()
    pygame.display.set_mode((800, 600))
    TileSetArchive.init_set_keys()

    # generate the level
    l = gen()

    # create the gamestate
    state = GameState()
    state.load_level(l)
    state.init_state()

    x = 16
    y = 10

    player = Actor((x, y), 'dragon')
    state.view.focus_object(player)
    MoveControl(player)

    c = state.view.coord.get

    x = Door((20, 7), 'hor', 'stone_door')
    y = Door((22, 8), 'ver', 'wooden_door')
    y.open()
    l.base_map.feature_map.add_feature((20, 7), x)
    l.base_map.feature_map.add_feature((22, 8), y)

    l.actors.add_actor(player)

    i = 0

    while True:
        #i += 1
        state.render()
        #draw_focus()

        state.run()

        state.handle_input()

        # c = print_coord(state.view, c)

        pygame.display.update()
        state.clock.tick(60)

        # if i == 60:
        #     y.toggle()
        #     x.toggle()
        #     i = 0


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
