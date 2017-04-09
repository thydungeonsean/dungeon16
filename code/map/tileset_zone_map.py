from code.image.tilesets.wall_tileset import WallTileSet
from code.image.tilesets.floor_tileset import FloorTileSet
from code.image.tilesets.water_tileset import WaterTileSet
from code.image.tilesets.pit_tileset import PitTileSet


class TilesetZoneMap(object):

    @classmethod
    def dungeon(cls, map):
        return cls(map, 'dungeon', 'dungeon_a')

    @classmethod
    def crypt(cls, map):
        return cls(map, 'crypt', 'dungeon_a', 'murky')

    @classmethod
    def cavern(cls, map):
        return cls(map, 'cave', 'cave')

    @classmethod
    def ruin(cls, map):
        return cls(map, 'ruin', 'dungeon_b')

    @classmethod
    def town(cls, map):
        return cls(map, 'ruin', 'grass')

    def __init__(self, base_map, wall='dungeon', floor='dungeon_a', water='blue'):
        self.base_map = base_map
        self.w = base_map.w
        self.h = base_map.h

        self.main_tilesets = {
                'wall': WallTileSet(wall),
                'floor': FloorTileSet(floor),
                'water': WaterTileSet(water),
                'pit': PitTileSet('pit')
                }
        self.zones = {
            'wall': [],
            'floor': [],
            'water': [],
            'pit': []
            }

    def add_zone(self, zone):
        key = zone.set_type
        try:
            self.zones[key].append(zone)
        except ZeroDivisionError:
            self.zones[key] = [zone]

    def get_tileset_for_point(self, point):

        point_type = self.base_map.get_tile_code(point)

        if point_type == '#':
            return self.get_wall_tileset(point)

        elif point_type == '.':
            return self.get_floor_tileset(point)

        elif point_type == '~':
            return self.get_water_tileset(point)

        elif point_type == '"':
            return self.get_pit_tileset(point)

        raise Exception('invalid point code in map array')

    def get_tileset(self, point, tile_type):
        if self.zones[tile_type]:
            for zone in self.zones[tile_type]:
                if zone.is_in_zone(point):
                    return zone.tileset
        return self.main_tilesets[tile_type]

    def get_wall_tileset(self, point):
        return self.get_tileset(point, 'wall')

    def get_floor_tileset(self, point):
        return self.get_tileset(point, 'floor')

    def get_water_tileset(self, point):
        return self.get_tileset(point, 'water')

    def get_pit_tileset(self, point):
        return self.get_tileset(point, 'pit')


