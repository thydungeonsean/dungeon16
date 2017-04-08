import pygame
from ..image.image import Image
from map_tile_set import MapTileSet


class MapImageGenerator(object):

    tile_w = 16
    tile_h = 16

    @classmethod
    def generate_image(cls, map):

        wall_tiles = MapTileSet('wall', 'ruin')
        floor_tiles = MapTileSet('floor', 'cave')

        image_w = map.w * cls.tile_w
        image_h = map.h * cls.tile_h

        map_image = Image(image_w, image_h)

        for y in range(map.h):
            for x in range(map.w):
                tile = cls.get_tile(map, (x, y), wall_tiles, floor_tiles)
                tile.position((x*cls.tile_w, y*cls.tile_h))
                tile.draw(map_image)

        map_image.scale_up(scale=2)
        return map_image

    @classmethod
    def get_tile(cls, map, point, wall_set, floor_set):

        if map.get_tile(point) == '#':
            adj = map.get_adj_tile_dict(point)
            if 's' in adj['directions'] and adj['s'] == '.':
                return wall_set.get_tile_image('hor')
            else:
                return wall_set.get_tile_image('ver')

        return floor_set.get_tile_image('var_c')



