

class BlockMap(object):

    def __init__(self, base_map):

        self.base_map = base_map

        self.block_map = {}
        self.block_coords = set()

    def add_block(self, point, key):
        self.block_map[point] = key
        self.block_coords.add(point)

    def get_tile(self, point, ani_key='a'):
        tilekey = self.block_map[point]
        if tilekey.endswith('ani'):
            tilekey = '_'.join((tilekey, ani_key))
        return tilekey
