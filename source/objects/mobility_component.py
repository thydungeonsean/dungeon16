

class MobilityComponent(object):

    dir_mods = {
        'up': (0, -1),
        'down': (0, 1),
        'right': (1, 0),
        'left': (-1, 0)
    }

    def __init__(self, owner):
        self.owner = owner
        self.facing = 'down'

    def move(self, c):
        if isinstance(c, tuple):
            self.owner.coord.set(c)
        else:
            self.set_facing(c)
            c = self.get_dir_coord(c)
            self.owner.coord.set(c)

    def get_dir_coord(self, c):
        dx, dy = MobilityComponent.dir_mods[c]
        x, y = self.owner.coord.get
        return dx + x, dy + y

    def set_facing(self, c):
        self.facing = c
