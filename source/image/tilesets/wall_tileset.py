from map_tileset import MapTileSet
from random import choice


class WallTileSet(MapTileSet):

    horizontal_var = ('hor_a', 'hor_b', 'hor_c', 'hor_d')
    vertical_var = ['ver_a', 'ver_b', 'ver_c', 'ver_d']

    def __init__(self, set_id):
        MapTileSet.__init__(self, 'wall', set_id)
        self.horizontal_var = WallTileSet.horizontal_var[:]
        self.vertical_var = WallTileSet.vertical_var[:]

    def get_base_tile(self, **kwargs):
        if kwargs.get('hor', False):
            return 'hor'
        else:
            return 'ver'

    def get_varied_tile(self, **kwargs):
        if kwargs.get('hor', False):
            if kwargs['single_width']:
                return choice(self.horizontal_var)
            return choice(self.horizontal_var[:3])
        else:
            if kwargs['single_width']:
                return choice(self.vertical_var)
            return choice(self.vertical_var[:3])
