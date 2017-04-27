from level import Level
from map_generator import MapGenerator
from source.image.map_image.map_image_generator import MapImageGenerator


class LevelGenerator(object):

    @classmethod
    def generate_level(cls, map):

        level = Level()

        if map.zone_map is None:
            map.generate_zone_map()

        if map.tile_id_map is None:
            map.generate_tile_id_map()

        if map.deco_map is None:
            map.generate_deco_map()

        level.set_base_map(map)

        level.set_map_image(MapImageGenerator.generate_image(map))

        return level

    @classmethod
    def load_level(cls, map_name):

        base_map = MapGenerator.load_map(map_name)

        return cls.generate_level(base_map)

