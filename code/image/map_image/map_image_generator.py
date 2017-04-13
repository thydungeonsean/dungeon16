from code.image.map_image.map_image import MapImage
from code.image.tilesets.tileset_archive import TileSetArchive
from pygame.locals import *
import pygame


class MapImageGenerator(object):

    @classmethod
    def generate_image(cls, map):

        if map.zone_map is None:  # these are temp!!!!
            map.generate_zone_map()

        if map.tile_map is None:  # TODO find a better init
            map.generate_tile_map()

        if map.deco_map is None:
            map.generate_deco_map()

        map_image = MapImage(map.w, map.h)

        for ani_key in ('a', 'b'):
            cls.render_map(map, map_image, ani_key)

        map_image.scale_up()
        return map_image

    @classmethod
    def render_map(cls, map, map_image, ani_key):

        for x, y in map.all_coords:

            tile_x = x * MapImage.tile_w
            tile_y = y * MapImage.tile_h

            # draw base tiles
            tileset, tilekey = map.tile_map.get_tile_id((x, y), ani_key)
            tile = tileset.get_tile_image(tilekey)
            tile.position((tile_x, tile_y))
            tile.draw(map_image.get_image(ani_key))

            # draw deco


            # draw shadow
            if (x, y) in map.deco_map.shadow_map:
                tileset = TileSetArchive.get_tileset('shadow')
                tile = tileset.get_tile_image(tileset.get_base_tile())

                blended = tile.get_blended_image(map_image.get_image(ani_key), (tile_x, tile_y))
                blended.draw(map_image.get_image(ani_key))

            # draw torches


            # draw blocks


            # draw features
