from random import *

from map_tools import MapTools
from source.image.tilesets.map_tilesets.deco_tileset import DecoTileSet


class DecoMap(object):

    def __init__(self, base_map):

        self.base_map = base_map

        self.deco_map = {}
        self.deco_coords = set()
        self.shadow_map = self.set_shadow_map()
        self.set_deco_map()

        self.torch_map = self.set_torch_map()
        self.glow_map = self.set_glow_map()

    def add_deco(self, point, key):
        self.deco_map[point] = key
        self.deco_coords.add(point)

    def get_tile(self, point, ani_key='a'):
        tilekey = self.deco_map[point]
        if tilekey.endswith('ani'):
            tilekey = '_'.join((tilekey, ani_key))
        return tilekey

    def set_shadow_map(self):

        wall_tiles = MapTools.all_walls(self.base_map)
        shadow_casters = list(filter(lambda x: MapTools.wall_casts_shadow(self.base_map, x), wall_tiles))

        shadow_coords = [(x, y+1) for x, y in shadow_casters]

        return set(shadow_coords)

    def set_torch_map(self):

        wall_tiles = MapTools.all_walls(self.base_map)
        valid_torches = list(filter(lambda x: MapTools.wall_valid_for_torch(self.base_map, self, x), wall_tiles))

        target_num_torches = int(len(valid_torches)*.2)
        max_iterations = len(valid_torches)
        shuffle(valid_torches)

        torches = set()

        for i in range(max_iterations):
            if self.torch_is_single(valid_torches[i], torches):
                torches.add(valid_torches[i])
            if len(torches) >= target_num_torches:
                return torches

        return set(torches)

    def torch_is_single(self, point, torches):
        adj = self.base_map.get_adj_coords(point)
        for a in adj:
            if a in torches:
                return False
        return True

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

        water = MapTools.all_water(self.base_map)
        self.add_lily_pads(water)

    def valid_for_deco(self, key, point):

        if point in self.base_map.block_map.block_coords:
            return False

        toggle = self.passes_deco_toggle(key, point)
        valid_tile = True
        tileset, tilekey = self.base_map.tile_id_map.tile_id_map[point]
        if tileset.set_type == 'floor' and tileset.sub_type == 'floor':
            if tilekey != 'base':
                valid_tile = False

        return toggle and valid_tile

    def passes_deco_toggle(self, key, point):
        tileset = self.base_map.zone_map.get_tileset_for_point(point)
        return tileset.deco_toggles[key]

    def add_cobwebs(self, open_floor):

        valid_for_cobwebs = MapTools.filter_corners(self.base_map, open_floor)
        valid_for_cobwebs = list(filter(lambda x: self.valid_for_deco('cobweb', x), valid_for_cobwebs))
        cobwebs = sample(valid_for_cobwebs, int(len(valid_for_cobwebs)*.4))
        for point in cobwebs:
            corner_id = MapTools.get_corner_id(self.base_map, point)
            self.add_deco(point, ''.join(('cobweb', corner_id)))
            open_floor.remove(point)

        return open_floor

    def add_gore(self, open_floor):

        valid_for_gore = list(filter(lambda x: self.valid_for_deco('gore', x), open_floor))

        gore = sample(valid_for_gore, int(len(valid_for_gore) * .05))

        for point in gore:
            gore_id = DecoTileSet.get_any_gore()
            self.add_deco(point, gore_id)
            open_floor.remove(point)

        return open_floor

    def add_bones(self, open_floor):

        valid_for_bones = list(filter(lambda x: self.valid_for_deco('bones', x), open_floor))

        bones = sample(valid_for_bones, int(len(valid_for_bones) * .05))

        for point in bones:
            bones_id = DecoTileSet.get_any_bones()
            self.add_deco(point, bones_id)
            open_floor.remove(point)

        return open_floor

    def add_tufts(self, open_floor):

        valid_for_tufts = list(filter(lambda x: self.valid_for_deco('tufts', x), open_floor))

        tufts = sample(valid_for_tufts, int(len(valid_for_tufts) * .1))

        for point in tufts:
            tufts_id = DecoTileSet.get_any_tuft()
            self.add_deco(point, tufts_id)
            open_floor.remove(point)

        return open_floor

    def add_roots(self, open_floor):

        valid_for_roots = list(filter(lambda x: self.valid_for_deco('roots', x), open_floor))

        roots = sample(valid_for_roots, int(len(valid_for_roots) * .1))

        for point in roots:
            root_id = DecoTileSet.get_any_root()
            self.add_deco(point, root_id)
            open_floor.remove(point)

        return open_floor

    def add_lily_pads(self, water):

        valid_for_lilypads = list(filter(lambda x: self.valid_for_deco('lilypad', x), water))

        lilypads = sample(valid_for_lilypads, int(len(valid_for_lilypads) * .1))

        for point in lilypads:
            lilypad_id = DecoTileSet.get_any_lilypad()
            self.add_deco(point, lilypad_id)


