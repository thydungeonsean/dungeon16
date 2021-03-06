from source.image.map_image.map_image import MapImage
from source.image.tilesets.map_tileset_archive import MapTileSetArchive
from source.states.settings import Settings


class MapImageGenerator(object):

    @classmethod
    def generate_image(cls, map):

        map_image = MapImage(map.w, map.h)

        for ani_key in ('a', 'b'):
            cls.render_map(map, map_image, ani_key)

        return map_image

    @classmethod
    def render_map(cls, map, map_image, ani_key):

        for x, y in map.all_coords:

            tile_x = x * Settings.SC_TILE_W
            tile_y = y * Settings.SC_TILE_H

            cls.render_tile((x, y), (tile_x, tile_y), map, map_image, ani_key)

    @classmethod
    def render_tile(cls, (x, y), (tile_x, tile_y), map, map_image, ani_key):

        # draw base tiles
        tileset, tilekey = map.tile_id_map.get_tile_id((x, y), ani_key)
        tile = tileset.get_tile_image(tilekey)
        tile.position((tile_x, tile_y))
        tile.draw(map_image.get_image(ani_key))

        # draw deco
        tileset = MapTileSetArchive.get_tileset('deco')
        deco = map.deco_map
        if (x, y) in deco.deco_coords:
            tilekey = deco.get_tile((x, y), ani_key)
            tile = tileset.get_tile_image(tilekey)
            tile.position((tile_x, tile_y))
            tile.draw(map_image.get_image(ani_key))

        # draw shadow
        if (x, y) in map.deco_map.shadow_map:
            tileset = MapTileSetArchive.get_tileset('shadow')
            tile = tileset.get_tile_image(tileset.get_base_tile())

            blended = tile.get_blended_image(map_image.get_image(ani_key), (tile_x, tile_y))
            blended.draw(map_image.get_image(ani_key))

        # draw torches
        if (x, y) in map.deco_map.torch_map:
            tileset = MapTileSetArchive.get_tileset('deco')
            tile = tileset.get_tile_image(tileset.get_torch_tile(ani_key))
            tile.position((tile_x, tile_y))
            tile.draw(map_image.get_image(ani_key))

        # draw_torch_glow
        if (x, y) in map.deco_map.glow_map:
            tileset = MapTileSetArchive.get_tileset('deco')
            tile = tileset.get_tile_image(tileset.get_torch_glow_tile(ani_key))
            tile.position((tile_x, tile_y))
            tile.draw(map_image.get_image(ani_key))

        # draw blocks
        if (x, y) in map.block_map.block_coords:
            tileset = MapTileSetArchive.get_tileset('block')
            tile = tileset.get_tile_image(map.block_map.get_tile((x, y), ani_key))
            tile.position((tile_x, tile_y))
            tile.draw(map_image.get_image(ani_key))
