from coord import Coord


class PixelCoord(Coord):

    """
    pixel coords
    """

    def __init__(self, x=0, y=0):

        Coord.__init__(self, x, y)
        self.coord_type = 'pixel'
        self.x_offset = 0
        self.y_offset = 0

    def translate(self, (x, y)):
        self.translate_coords((x, y))
        if self.bound is not None:
            self.bound.set((self.x, self.y))
        if self.auto_position_owner:
            self.auto_position()

    def translate_coords(self, (x, y)):
        self.x = (x * 16) + self.x_offset
        self.y = (y * 16) + self.y_offset