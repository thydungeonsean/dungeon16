import pygame
from code.image.image import Image
from code.image.map_tile_set import MapTileSet


class MapImageGenerator(object):

    tile_w = 16
    tile_h = 16

    @classmethod
    def generate_image(cls, map):

        if map.zone_map is None:  # these are temp!!!!
            map.generate_zone_map()

        if map.tile_map is None: # TODO find a better init
            map.generate_tile_map()

        image_w = map.w * cls.tile_w
        image_h = map.h * cls.tile_h

        map_image = Image(image_w, image_h)

        for x, y in map.all_coords:
            tileset, tilekey = map.tile_map.get_tile_id((x, y))
            tile = tileset.get_tile_image(tilekey)
            tile.position((x*cls.tile_w, y*cls.tile_h))
            tile.draw(map_image)

        map_image.scale_up()
        return map_image




