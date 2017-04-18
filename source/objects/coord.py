

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
            if self.bound.coord_type != self.coord_type:
                self.bound.translate((self.x, self.y))
            else:
                self.bound.set((self.x, self.y))
        if self.auto_position_owner:
            self.auto_position()

    def set_coords(self, (x, y)):
        self.x = x
        self.y = y

    def bind(self, coord):
        self.bound = coord
        if self.bound.coord_type != self.coord_type:
            self.bound.translate((self.x, self.y))
        else:
            self.bound.set((self.x, self.y))

    def unbind(self):
        self.bound = None
