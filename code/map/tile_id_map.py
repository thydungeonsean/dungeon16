

class TileIDMap(object):

    def __init__(self, base_map):

        self.base_map = base_map
        self.zone_map = base_map.zone_map

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
        return tileset, tileset.get_any_tile_id()

    def get_wall_tile(self, tileset, point):
        adj = self.base_map.get_adj_tile_dict(point, diag=True)

        if 's' in adj['directions'] and adj['s'] != '#':
            return tileset, 'hor'

        elif self.wall_is_isolate(adj):
            tileset = self.zone_map.main_tilesets['pit']
            return tileset, 'pit'

        return tileset, 'ver'

    def wall_is_isolate(self, adj):
        for d in adj['directions']:
            if adj[d] != '#':
                return False
        return True

    def get_tile_id(self, point):
        return self.tile_id_map[point]
