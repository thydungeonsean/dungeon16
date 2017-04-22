from source.states.settings import Settings


class Coord(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.bound = None
        self.owner = None
        self.auto_position_owner = False
        self.coord_type = 'base'
        self.x_offset = 0
        self.y_offset = 0

    def set_x_offset(self, off):
        self.x_offset = off

    def set_y_offset(self, off):
        self.y_offset = off

    def set_owner(self, owner):
        self.owner = owner

    def toggle_auto_position_owner(self):
        if self.auto_position_owner:
            self.auto_position_owner = False
        else:
            self.auto_position_owner = True

    def auto_position(self):
        self.owner.reset_position()

    @property
    def get(self):
        return self.x + self.x_offset, self.y + self.y_offset
        
    def set(self, (x, y)):
        self.set_coords((x, y))
        if self.bound is not None:
            for coord in self.bound:
                if coord.coord_type != self.coord_type:
                    coord.translate(self.get)
                else:
                    coord.set(self.get)
        if self.auto_position_owner:
            self.auto_position()

    def set_coords(self, (x, y)):
        self.x = x
        self.y = y

    def bind(self, coord):
        if self.bound is None:
            self.bound = []
        self.bound.append(coord)
        if coord.coord_type != self.coord_type:
            coord.translate(self.get)
        else:
            coord.set(self.get)

    def unbind(self):
        self.bound = None

    def translate(self, (x, y)):
        self.translate_coords((x, y))
        if self.bound is not None:
            for c in self.bound:
                c.set(self.get)
        if self.auto_position_owner:
            self.auto_position()

    def translate_coords(self, (x, y)):
        self.x = (x / Settings.SC_TILE_W)
        self.y = (y / Settings.SC_TILE_H)

    def add(self, coord):

        if isinstance(coord, Coord):
            cx, cy = coord.get
        else:
            cx, cy = coord
        x, y = self.get
        return x + cx, y + cy

