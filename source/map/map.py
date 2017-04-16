from source.map.tile_id_map import TileIDMap
from source.map.tileset_zone_map import TilesetZoneMap
from source.map.deco_map import DecoMap
from source.map.block_map import BlockMap


class Map(object):

    def __init__(self, w, h):

        self.w = w
        self.h = h
        self.map = None

        self.zone_map = None
        self.block_map = BlockMap(self)

        self.tile_id_map = None
        self.deco_map = None

    def init_basic_map(self):
        self.map = [['#' for y in range(self.h)] for x in range(self.w)]

    def set_map(self, map):
        self.map = map

    @property
    def all_coords(self):
        coords = []
        for y in range(self.h):
            for x in range(self.w):
                coords.append((x, y))
        return coords

    def generate_zone_map(self):
        self.zone_map = TilesetZoneMap.test(self)

    def generate_tile_id_map(self):
        self.tile_id_map = TileIDMap(self)

    def generate_deco_map(self):
        self.deco_map = DecoMap(self)

    # coordinate methods

    def is_on_map(self, (x, y)):
        if 0 <= x < self.w and 0 <= y < self.h:
            return True
        else:
            return False

    def get_adj_coords(self, (x, y), diag=False):

        raw_adj = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        if diag:
            raw_adj.extend([(x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)])
        adj_on_map = []
        for p in raw_adj:
            if self.is_on_map(p):
                adj_on_map.append(p)

        return adj_on_map

    def get_adj_tile_dict(self, (x, y), diag=False):

        direction_dict = {
            'n': (x, y-1),
            's': (x, y+1),
            'e': (x+1, y),
            'w': (x-1, y)
        }
        if diag:
            diag_directions = {
                'ne': (x+1, y-1),
                'nw': (x-1, y-1),
                'se': (x+1, y+1),
                'sw': (x-1, y+1)
            }
            direction_dict.update(diag_directions)

        adj_dict = {}
        direction_list = []

        for dir_key, point in direction_dict.items():
            if self.is_on_map(point):
                adj_dict[dir_key] = self.get_tile_code(point)
                adj_dict[''.join((dir_key, '_coord'))] = point
                direction_list.append(dir_key)

        adj_dict['directions'] = direction_list

        return adj_dict

    def get_tile_code(self, (x, y)):
        return self.map[x][y]


