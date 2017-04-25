from source.image.tilesheet_key_parser import *

from source.image.tilesets.wall_tileset import WallTileSet
from source.image.tilesets.floor_tileset import FloorTileSet
from source.image.tilesets.door_tileset import DoorTileSet
from source.image.tilesets.water_tileset import WaterTileSet
from source.image.tilesets.pit_tileset import PitTileSet
from source.image.tilesets.deco_tileset import DecoTileSet
from source.image.tilesets.shadow_tileset import ShadowTileSet
from source.image.tilesets.block_tileset import BlockTileSet
from source.image.tilesets.feature_tileset import FeatureTileSet


class TileSetArchive(object):

    loaded_tilesets = {}

    wall_keys = None
    floor_keys = None
    door_keys = None
    water_keys = None
    # house, trap door- only one set per category

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
            return DoorTileSet(tileset_key)

        elif tileset_key in cls.water_keys:
            return WaterTileSet(tileset_key)

        elif tileset_key == 'pit':
            return PitTileSet()

        elif tileset_key == 'trap door':
            return

        elif tileset_key == 'house':
            return

        elif tileset_key == 'shadow':
            return ShadowTileSet()

        elif tileset_key == 'deco':
            return DecoTileSet()

        elif tileset_key == 'block':
            return BlockTileSet()

        elif tileset_key == 'feature':
            return FeatureTileSet()
