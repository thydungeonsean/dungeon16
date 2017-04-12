from code.image.tilesheet_key_parser import *
from code.image.tilesets.wall_tileset import WallTileSet
from code.image.tilesets.floor_tileset import FloorTileSet
# from code.image.tilesets.door_tileset import DoorTileSet
from code.image.tilesets.water_tileset import WaterTileSet
from code.image.tilesets.pit_tileset import PitTileSet
# from code.image.tilesets.


class TileSetArchive(object):

    loaded_tilesets = {}

    wall_keys = None
    floor_keys = None
    door_keys = None
    water_keys = None
    # pit, house, trap door, shadow, deco, block, feature - only one set per category

    @classmethod
    def init_set_keys(cls):
        cls.wall_keys = cls.set_key_list('wall')
        cls.floor_keys = cls.set_floor_key_list()
        cls.door_keys = cls.set_key_list('door')
        cls.water_keys = cls.set_key_list('water')

    # key building methods
    @staticmethod
    def set_key_list(set_key):
        return tuple(get_set_keys('world_key', set_key))

    @staticmethod
    def set_floor_key_list():
        floor = get_set_keys('world_key', 'floor')
        floor.extend(get_set_keys('world_key', 'deco floor'))
        floor.extend(get_set_keys('world_key', 'town floor'))

        return tuple(floor)

    @classmethod
    def get_tileset(cls, tileset_key):

        if tileset_key in cls.loaded_tilesets.keys():
            return cls.loaded_tilesets[tileset_key]

        else:
            cls.loaded_tilesets[tileset_key] = cls.generate_tileset(tileset_key)
            return cls.loaded_tilesets[tileset_key]

    @classmethod
    def generate_tileset(cls, tileset_key):

        if tileset_key in cls.wall_keys:
            return WallTileSet(tileset_key)

        elif tileset_key in cls.floor_keys:
            return FloorTileSet(tileset_key)

        elif tileset_key in cls.door_keys:
            return

        elif tileset_key in cls.water_keys:
            return WaterTileSet(tileset_key)

        elif tileset_key == 'pit':
            return PitTileSet(tileset_key)

        elif tileset_key == 'trap door':
            return

        elif tileset_key == 'house':
            return

        elif tileset_key == 'shadow':
            return

        elif tileset_key == 'deco':
            return

        elif tileset_key == 'block':
            return

        elif tileset_key == 'feature':
            return