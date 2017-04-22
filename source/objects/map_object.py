from coord import Coord
from pixel_coord import PixelCoord


class MapObject(object):

    def __init__(self, (x, y)):

        self.coord = Coord(x, y)
        self.pixel_coord = PixelCoord()
        self.coord.bind(self.pixel_coord)

    def draw(self, surface):
        print 'draw'

    def on_bump(self):
        pass
