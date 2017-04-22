from coord import Coord
from source.states.settings import Settings


class PixelCoord(Coord):

    def __init__(self, x=0, y=0):

        Coord.__init__(self, x, y)
        self.coord_type = 'pixel'

    def translate_coords(self, (x, y)):
        self.x = (x * Settings.SC_TILE_W)
        self.y = (y * Settings.SC_TILE_H)

