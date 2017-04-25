from coord import Coord
from pixel_coord import PixelCoord

from source.image.tilesets.tileset_archive import TileSetArchive


class MapObject(object):

    def __init__(self, (x, y)):

        self.coord = Coord(x, y)
        self.pixel_coord = PixelCoord()
        self.coord.bind(self.pixel_coord)

        self.image = self.set_image()

    def set_image(self):
        return TileSetArchive.get_tileset('dungeon_wall').get_tile_image('pool')

    def draw(self, surface):
        self.image.draw(surface)

    def draw_to_map(self, surface, view):
        draw_coord = self.pixel_coord.subtract(view.pixel_coord)
        self.image.position(draw_coord)
        self.draw(surface)

    def on_bump(self):
        pass
