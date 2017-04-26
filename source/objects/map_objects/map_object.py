from source.objects.coord import Coord
from source.objects.pixel_coord import PixelCoord

from source.image.tilesets.tileset_archive import TileSetArchive


class MapObject(object):

    def __init__(self, (x, y)):

        self.coord = Coord(x, y)
        self.pixel_coord = PixelCoord()
        self.coord.bind(self.pixel_coord)

        self.images = self.set_images()

        self.block_move = True
        self.block_view = False

    def set_images(self):
        return {0: TileSetArchive.get_tileset('dungeon_wall').get_tile_image('pool')}

    def get_image_key(self):
        return 0

    @property
    def current_image(self):
        return self.images[self.get_image_key()]

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
