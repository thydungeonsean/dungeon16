from map_tile_set import MapTileSet
from random import choice
from code.image.tilesheet_key_parser import get_set_keys


class FloorTileSet(MapTileSet):

    standard_sets = None
    deco_sets = None

    std_variable_tiles = ('var_a', 'var_b', 'var_c', 'var_d', 'var_e')
    deco_variable_tiles = ('base', 'var_a', 'var_b', 'var_c', 'var_d')

    @classmethod
    def init_set_tuples(cls):
        if cls.standard_sets is None:
            cls.standard_sets = tuple(get_set_keys('world_key', 'floor'))
        if cls.deco_sets is None:
            cls.deco_sets = tuple(get_set_keys('world_key', 'deco floor'))

    def __init__(self, set_id):
        FloorTileSet.init_set_tuples()
        set_type = self.get_set_type(set_id)
        MapTileSet.__init__(self, set_type, set_id)
        self.set_type = 'floor'
        self.sub_type = set_type
        self.variable_tiles = self.get_variable_tile_list(set_type)
        self.set_base_tile_function(set_type)

    def get_base_tile(self, **kwargs):
        return 'base'

    def get_varied_tile(self, **kwargs):
        return choice(self.variable_tiles)

    def set_base_tile_function(self, set_type):
        if set_type == 'floor':
            return
        self.get_base_tile = self.get_varied_tile

    @classmethod
    def get_set_type(cls, set_id):
        if set_id in cls.standard_sets:
            return 'floor'
        elif set_id in cls.deco_sets:
            return 'deco floor'
        raise Exception('set_id: %s is not valid ' % set_id)

    @classmethod
    def get_variable_tile_list(cls, set_type):
        if set_type == 'floor':
            return cls.std_variable_tiles[:]
        return cls.deco_variable_tiles[:]



