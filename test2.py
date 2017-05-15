import pygame

from source.controller.move_control import MoveControl
from source.map.level.level_generator import LevelGenerator
from source.objects.map_objects.door import Door
from source.states.game_state import GameState
from source.states.settings import Settings


from source.map.map_tools import MapTools
from random import randint, choice
from source.objects.map_objects.monster import Monster
from source.objects.map_objects.party_member import PartyMember

import source.map.dijkstra_maps.dijkstra_map as dm
from source.map.dijkstra_maps.dijkstra_tools import *
from source.map.dijkstra_maps.dijkstra_collection import DijkstraCollection


def gen():

    l = LevelGenerator.load_level('map')

    return l


def d(m):

    m.calculate()


def draw_d_map(m, p, my=0):

    w = m.w
    h = m.h

    s = pygame.display.get_surface()

    tw = 5

    image = pygame.Surface((w*tw, h*tw)).convert()

    dot = pygame.Surface((tw, tw)).convert()
    r = dot.get_rect()

    for y in range(h):
        for x in range(w):

            if (x, y) == p.coord.get:
                dot.fill((255, 0, 10))
                r.topleft = (x * tw, (y * tw))
                image.blit(dot, r)
                continue

            col_v = m.d_map[x][y]

            if col_v > 255:
                col_v = 255

            if m.d_map[x][y] is None:
                col_v = 0
            else:
                col_v = m.d_map[x][y]+5

            if m.d_map[x][y] == 0:
                #col = (50, 0, 100)
                pass
            else:
                col = (col_v, col_v, col_v)
            dot.fill(col)
            r.topleft = (x*tw, (y*tw))
            image.blit(dot, r)

    r = image.get_rect()
    r.topleft = (0, my)
    s.blit(image, r)


def test():

    # basic init functions
    pygame.init()
    pygame.display.set_mode((800, 600))

    # generate the level
    l = gen()

    # create the gamestate
    state = GameState()
    state.load_level(l)
    state.init_state()

    px = 16
    py = 10

    player = PartyMember((px, py), 'wizard')
    state.view.focus_object(player)
    MoveControl(player)

    l.actors.add_actor(player)
    #l.actors.add_actor(PartyMember((18, 6), 'paladin'))

    l.fov_map.set_fov_map()
    l.fov_map.recompute_fov(player, state.view)

    add_actors(l, (px, py))

    #m = dm.DijkstraMap(l, walker_passable, get_party_source)

    m = l.dijkstra_collection.access_map('range_3_party_walker')
    x = l.dijkstra_collection.access_map('party_walker')

    d(m)

    m._print()

    i = 0

    while True:
        #i += 1
        #state.render()
        draw_d_map(m, player, 0)
        #draw_d_map(x, player, 200)

        state.run()

        state.handle_input()

        pygame.display.update()
        state.clock.tick(60)

        #m.calculate()
        #y.calculate()
        print state.clock.get_fps()


def add_actors(l, p):

    for c in MapTools.all_floors(l.base_map):
        if c == p:
            pass
        else:
            if randint(0, 6) == 0:
                l.actors.add_actor(Monster(c, choice(('goblin', 'skeleton', 'cube'))))


if __name__ == '__main__':
    test()
