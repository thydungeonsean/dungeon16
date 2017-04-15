

class Coord(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.bound = None
        self.owner = None
        self.auto_position_owner = False

    def set_owner(self, owner):
        self.owner = owner

    def toggle_auto_position_owner(self):
        if self.auto_position_owner:
            self.auto_position_owner = False
        else:
            self.auto_position_owner = True

    def auto_position(self):
        self.owner.reset_pos()

    @property
    def get(self):
        return self.x, self.y
        
    def set(self, (x, y)):
        self.x = x
        self.y = y
        if self.bound is not None:
            self.bound.set((x, y))
        if self.auto_position_owner:
            self.auto_position()

    def bind(self, coord):
        self.bound = coord
        self.bound.set(self.get)

    def unbind(self):
        self.bound = None
