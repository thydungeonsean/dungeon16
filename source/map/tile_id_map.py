from random import randint
from map_tools import MapTools


class TileIDMap(object):

    def __init__(self, base_map, variance=50):

        self.base_map = base_map
        self.zone_map = base_map.zone_map

        self.variance = variance
        self.tile_id_map = self.set_tile_id_map()

    def set_tile_id_map(self):
        id_map = {}
        for x, y in self.base_map.all_coords:
            id_map[(x, y)] = self.set_tile_id((x, y))

        return id_map

    def set_tile_id(self, point):
        tileset = self.zone_map.get_tileset_for_point(point)
        if tileset.set_type == 'wall':
            return self.get_wall_tile(tileset, point)
        elif tileset.set_type == 'floor':
            return self.get_floor_tile(tileset, point)
        elif tileset.set_type == 'water':
            return self.get_water_tile(tileset, point)
        elif tileset.set_type == 'pit':
            return self.get_pit_tile(tileset, point)
        raise Exception('tileset does not have valid set_type')

    def get_tile_id(self, point, ani_key):
        tileset, tilekey = self.tile_id_map[point]
        if tilekey.endswith('ani'):
            tilekey = '_'.join((tilekey, ani_key))
        return tileset, tilekey

    def get_tile_id_from_tileset(self, tileset, **kwargs):
        vary = randint(1, 100)
        if vary <= self.variance:
            return tileset, tileset.get_varied_tile(**kwargs)
        else:
            return tileset, tileset.get_base_tile(**kwargs)

    # specific tileset methods
    def get_wall_tile(self, tileset, point):

        adj = self.base_map.get_adj_tile_dict(point, diag=True)

        single_width = MapTools.wall_is_single_width(adj)

        if 's' in adj['directions'] and adj['s'] != '#':
            return self.get_tile_id_from_tileset(tileset, hor=True, single_width=single_width)

        elif MapTools.wall_is_isolate(adj):
            tileset = self.zone_map.main_tilesets['pit']
            return tileset, 'pit'

        return self.get_tile_id_from_tileset(tileset, hor=False, single_width=single_width)

    def get_floor_tile(self, tileset, point):
        return self.get_tile_id_from_tileset(tileset)

    def get_water_tile(self, tileset, point):

        adj = self.base_map.get_adj_tile_dict(point)
        if 'n' in adj['directions'] and adj['n'] in ('#', '.'):
            return self.get_tile_id_from_tileset(tileset, edge=True)
        return self.get_tile_id_from_tileset(tileset)

    def get_pit_tile(self, tileset, point):

        adj = self.base_map.get_adj_tile_dict(point)
        if 'n' in adj['directions'] and adj['n'] in ('#', '.'):

            if adj['n'] == '.':
                edge_tileset = self.zone_map.get_tileset_for_point(adj['n_coord'])
                if edge_tileset.sub_type == 'floor':
                    return edge_tileset, 'pit_edge'
            elif adj['n'] == '#':
                edge_tileset = self.zone_map.get_tileset_for_point(adj['n_coord'], point_type='.')
                if edge_tileset.sub_type == 'floor':
                    return edge_tileset, 'pit_edge'

            return self.get_tile_id_from_tileset(tileset, edge=True)
        return self.get_tile_id_from_tileset(tileset)

