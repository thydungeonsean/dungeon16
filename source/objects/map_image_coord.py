from coord import Coord


class MapImageCoord(Coord):

    def __init__(self, x=0, y=0):
        Coord.__init__(self, x, y)

    @property
    def get(self):
        return (-1 * self.x) + self.x_offset, (-1 * self.y) + self.y_offset

    def set(self, (x, y)):
        self.set_coords((x, y))
        if self.bound is not None:
            for c in self.bound:
                c.set((self.x, self.y))
        if self.auto_position_owner:
            self.auto_position()

    def set_coords(self, (x, y)):
        self.x = x
        self.y = y

    def bind(self, coord):
        if self.bound is None:
            self.bound = []
        self.bound.append(coord)
        coord.set(self.get)

    def translate(self, (x, y)):
        self.set((x, y))
