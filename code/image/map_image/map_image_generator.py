from code.image.map_image.map_image import MapImage


class MapImageGenerator(object):

    @classmethod
    def generate_image(cls, map):

        if map.zone_map is None:  # these are temp!!!!
            map.generate_zone_map()

        if map.tile_map is None:  # TODO find a better init
            map.generate_tile_map()

        map_image = MapImage(map.w, map.h)

        for ani_key in ('a', 'b'):
            cls.render_map(map, map_image, ani_key)

        map_image.scale_up()
        return map_image

    @classmethod
    def render_map(cls, map, map_image, ani_key):

        for x, y in map.all_coords:
            tileset, tilekey = map.tile_map.get_tile_id((x, y), ani_key)
            tile = tileset.get_tile_image(tilekey)
            tile.position((x*MapImage.tile_w, y*MapImage.tile_h))
            tile.draw(map_image.get_image(ani_key))


