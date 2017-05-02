from map_tileset import MapTileSet
from random import choice
from source.image.tilesheet_key_parser import get_set_keys


class FloorTileSet(MapTileSet):

    standard_sets = None
    deco_sets = None
    town_sets = None

    std_variable_tiles = ('var_a', 'var_b', 'var_c', 'var_d', 'var_e')
    deco_variable_tiles = ('base', 'var_a', 'var_b', 'var_c', 'var_d')
    town_variable_tiles = ('base', 'var_a', 'var_b', 'var_c')

    deco_toggle_keys = ('gore', 'bones', 'cobweb', 'tufts', 'roots')

    toggle_set_dungeon = ('gore', 'bones', 'cobweb')
    toggle_set_cave = ('gore', 'bones', 'cobweb', 'tufts', 'roots')
    toggle_set_outdoor = ('tufts', 'roots')

    deco_toggle_def = {
        'dungeon_floor_a': toggle_set_dungeon,
        'dungeon_floor_b': toggle_set_dungeon,
        'cave_floor': toggle_set_cave,
        'grass_floor': toggle_set_outdoor,
        'tile_floor_a': toggle_set_dungeon,
        'tile_floor_b': toggle_set_dungeon,
        'tile_floor_c': toggle_set_dungeon,
        'cobble_floor': toggle_set_dungeon,
        'tile_floor_d': toggle_set_dungeon,
        'wood_floor': (),
        'outdoor_floor': ()
    }

    @classmethod
    def init_set_tuples(cls):
        if cls.standard_sets is None:
            cls.standard_sets = tuple(get_set_keys('world_key', 'floor'))
        if cls.deco_sets is None:
            cls.deco_sets = tuple(get_set_keys('world_key', 'deco floor'))
        if cls.town_sets is None:
            cls.town_sets = tuple(get_set_keys('world_key', 'town floor'))

    def __init__(self, set_id):
        FloorTileSet.init_set_tuples()
        set_type = self.get_set_type(set_id)
        MapTileSet.__init__(self, set_type, set_id)
        self.set_type = 'floor'
        self.sub_type = set_type
        self.variable_tiles = self.get_variable_tile_list(self.sub_type)
        self.set_base_tile_function(self.sub_type)

        self.deco_toggles = self.set_deco_toggles()

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
        elif set_id in cls.town_sets:
            return 'town floor'
        raise Exception('set_id: %s is not valid ' % set_id)

    @classmethod
    def get_variable_tile_list(cls, set_type):
        if set_type == 'floor':
            return cls.std_variable_tiles[:]
        elif set_type == 'deco floor':
            return cls.deco_variable_tiles[:]
        elif set_type == 'town floor':
            return cls.town_variable_tiles[:]

    def set_deco_toggles(self):

        cls = FloorTileSet

        deco_toggles = {}

        if self.set_id in cls.deco_toggle_def.keys():
            modify = cls.deco_toggle_def[self.set_id]
        else:
            modify = ()

        for key in cls.deco_toggle_keys:
            if key in modify:
                deco_toggles[key] = True
            else:
                deco_toggles[key] = False

        return deco_toggles

