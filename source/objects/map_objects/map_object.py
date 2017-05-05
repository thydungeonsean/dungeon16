from source.objects.coord import Coord
from source.objects.pixel_coord import PixelCoord

from source.image.tilesets.map_tileset_archive import MapTileSetArchive


class MapObject(object):

    def __init__(self, (x, y)):

        self.coord = Coord(x, y)
        self.pixel_coord = PixelCoord()
        self.coord.bind(self.pixel_coord)

        self.drawable = True
        self.images = self.set_images()

        self.block_move = True
        self.block_view = False

        self.level = None

    def set_level(self, level):
        self.level = level

    def set_images(self):
        raise NotImplementedError  # should be dict of tile ids to Image objects

    def get_image_key(self):
        raise NotImplementedError

    @property
    def current_image(self):
        return self.images.get(self.get_image_key())

    def draw(self, surface):
        self.current_image.draw(surface)

    def draw_to_map(self, surface, view):
        draw_coord = self.pixel_coord.subtract(view.pixel_coord)
        self.current_image.position(draw_coord)
        self.current_image.draw(surface)

    def on_bump(self):
        pass

    def move(self, c):
        raise Exception('Attempting to move non mobile map object')
