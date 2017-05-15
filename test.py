import pygame

from source.controller.move_control import MoveControl
from source.image.tilesets.map_tileset_archive import MapTileSetArchive
from source.map.level.level_generator import LevelGenerator
from source.map.map_generator import MapGenerator
from source.objects.map_objects.actor import Actor
from source.objects.map_objects.door import Door
from source.states.game_state import GameState
from source.states.settings import Settings


from source.map.map_tools import MapTools
from random import randint, choice
from source.objects.effects.impact_effect import ImpactEffect
from source.objects.map_objects.monster import Monster
from source.objects.map_objects.party_member import PartyMember
from source.objects.effects.animation_effect import AnimationEffect


def gen():

    l = LevelGenerator.load_level('map')

    # z = TilesetZone((10, 0), 7, 6, 'water', 'blue')
    # z2 = TilesetZone((0, 0), 12, 9, 'floor', 'tile_floor_d')
    # m.generate_zone_map()
    # m.zone_map.add_zone(z)
    # m.zone_map.add_zone(z2)

    return l


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

    c = state.view.coord.get

    x = Door((20, 7), 'hor', 'stone_door')
    y = Door((22, 8), 'ver', 'wooden_door')
    #y.open()
    l.feature_map.add_feature((20, 7), x)
    l.feature_map.add_feature((22, 8), y)

    l.actors.add_actor(player)

    l.fov_map.set_fov_map()
    l.fov_map.recompute_fov(player, state.view)

    add_actors(l, (px, py))

    # l.effects.add_effect(AnimationEffect(player))

    i = 0

    while True:
        #i += 1
        state.render()

        state.run()

        state.handle_input()

        # c = print_coord(state.view, c)

        pygame.display.update()
        state.clock.tick(60)
        # print state.clock.get_fps()

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


def add_actors(l, p):

    for c in MapTools.all_floors(l.base_map):
        if c == p:
            pass
        else:
            if randint(0, 6) == 0:
                l.actors.add_actor(Monster(c, choice(('goblin', 'skeleton', 'cube'))))


if __name__ == '__main__':
    test()
