from map_tools import MapTools
from source.image.tilesets.deco_tileset import DecoTileSet
from random import *


class DecoMap(object):

    def __init__(self, base_map):

        self.base_map = base_map

        self.deco_map = {}
        self.deco_coords = set()
        self.shadow_map = self.set_shadow_map()
        self.torch_map = self.set_torch_map()
        self.glow_map = self.set_glow_map()
        self.set_deco_map()

    def add_deco(self, point, key):
        self.deco_map[point] = key
        self.deco_coords.add(point)

    def get_tile(self, point):
        return self.deco_map[point]

    def set_shadow_map(self):

        wall_tiles = MapTools.all_walls(self.base_map)
        shadow_casters = list(filter(lambda x: MapTools.wall_casts_shadow(self.base_map, x), wall_tiles))

        shadow_coords = [(x, y+1) for x, y in shadow_casters]

        return set(shadow_coords)

    def set_torch_map(self):

        wall_tiles = MapTools.all_walls(self.base_map)
        hor_walls = list(filter(lambda x: MapTools.wall_valid_for_torch(self.base_map, x), wall_tiles))

        torches = sample(hor_walls, int(len(hor_walls)*.2))

        return set(torches)

    def set_glow_map(self):

        torches = list(self.torch_map)
        glow = list(map(lambda (x, y): (x, y+1), torches))
        glow = set(filter(lambda x: self.base_map.get_tile_code(x) == '.', glow))
        return glow

    def set_deco_map(self):

        open_floor = MapTools.all_floors(self.base_map)

        open_floor = self.add_cobwebs(open_floor)
        open_floor = self.add_gore(open_floor)
        open_floor = self.add_bones(open_floor)
        open_floor = self.add_tufts(open_floor)
        self.add_roots(open_floor)

    def add_cobwebs(self, open_floor):

        valid_for_cobwebs = MapTools.filter_corners(self.base_map, open_floor)
        cobwebs = sample(valid_for_cobwebs, int(len(valid_for_cobwebs)*.4))
        for point in cobwebs:
            corner_id = MapTools.get_corner_id(self.base_map, point)
            self.add_deco(point, ''.join(('cobweb', corner_id)))
            open_floor.remove(point)

        return open_floor

    def add_gore(self, open_floor):

        valid_for_gore = open_floor  # filter by tileset

        gore = sample(valid_for_gore, int(len(valid_for_gore) * .1))

        for point in gore:
            gore_id = DecoTileSet.get_any_gore()
            self.add_deco(point, gore_id)
            open_floor.remove(point)

        return open_floor

    def add_bones(self, open_floor):

        valid_for_bones = open_floor  # filter by tileset

        bones = sample(valid_for_bones, int(len(valid_for_bones) * .1))

        for point in bones:
            bones_id = DecoTileSet.get_any_bones()
            self.add_deco(point, bones_id)
            open_floor.remove(point)

        return open_floor

    def add_tufts(self, open_floor):

        valid_for_tufts = open_floor  # filter by tileset

        tufts = sample(valid_for_tufts, int(len(valid_for_tufts) * .1))

        for point in tufts:
            tufts_id = DecoTileSet.get_any_tuft()
            self.add_deco(point, tufts_id)
            open_floor.remove(point)

        return open_floor

    def add_roots(self, open_floor):

        valid_for_roots = open_floor  # filter by tileset

        roots = sample(valid_for_roots, int(len(valid_for_roots) * .1))

        for point in roots:
            root_id = DecoTileSet.get_any_root()
            self.add_deco(point, root_id)
            open_floor.remove(point)

        return open_floor
