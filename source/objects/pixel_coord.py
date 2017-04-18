from coord import Coord
from source.states.settings import Settings


class PixelCoord(Coord):

    """
    only bind to other pixel coords
    """

    def __init__(self, x=0, y=0):

        Coord.__init__(self, x, y)
        self.coord_type = 'pixel'

    def translate(self, (x, y)):
        self.translate_coords((x, y))
        if self.bound is not None:
            self.bound.set((self.x, self.y))
        if self.auto_position_owner:
            self.auto_position()

    def translate_coords(self, (x, y)):
        self.x = (x * Settings.TILE_W)
        self.y = (y * Settings.TILE_H)

