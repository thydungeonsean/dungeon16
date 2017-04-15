from source.image.tilesets.tileset_archive import TileSetArchive


class TilesetZoneMap(object):

    @classmethod
    def dungeon(cls, map):
        return cls(map, 'dungeon_wall', 'dungeon_floor_a')

    @classmethod
    def crypt(cls, map):
        return cls(map, 'crypt_wall', 'dungeon_floor_a', 'murky')

    @classmethod
    def cavern(cls, map):
        return cls(map, 'cave_wall', 'cave_floor')

    @classmethod
    def ruin(cls, map):
        return cls(map, 'ruin_wall', 'dungeon_floor_b', 'sewer')

    @classmethod
    def town(cls, map):
        return cls(map, 'ruin_wall', 'grass_floor')

    @classmethod
    def test(cls, map):
        return cls(map, 'crypt_wall', 'cobble_floor', 'sewer')

    def __init__(self, base_map, wall='dungeon_wall', floor='dungeon_floor_a', water='blue'):
        self.base_map = base_map
        self.w = base_map.w
        self.h = base_map.h

        self.main_tilesets = {
                'wall': TileSetArchive.get_tileset(wall),
                'floor': TileSetArchive.get_tileset(floor),
                'water': TileSetArchive.get_tileset(water),
                'pit': TileSetArchive.get_tileset('pit')
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
        except KeyError:
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

        raise Exception('invalid point source in map array')

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


