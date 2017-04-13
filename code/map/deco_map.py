from map_tools import MapTools


class DecoMap(object):

    def __init__(self, base_map):

        self.base_map = base_map

        self.deco_map = None
        self.shadow_map = self.set_shadow_map()

    def add_deco(self, (x, y), key):
        pass


    def set_shadow_map(self):

        wall_tiles = list(filter(lambda x: self.base_map.get_tile_code(x) == '#', self.base_map.all_coords))
        shadow_casters = list(filter(lambda x: MapTools.wall_casts_shadow(self.base_map, x), wall_tiles))

        shadow_coords = [(x, y+1) for x, y in shadow_casters]
        return set(shadow_coords)
