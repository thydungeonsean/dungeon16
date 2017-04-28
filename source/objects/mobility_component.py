

class MobilityComponent(object):

    dir_mods = {
        'up': (0, -1),
        'down': (0, 1),
        'right': (1, 0),
        'left': (-1, 0)
    }

    def __init__(self, owner):
        self.owner = owner
        self.level = None

        self.facing = 'down'

    def try_move(self, c):
        if isinstance(c, tuple):
            move = c
        else:
            move = self.get_dir_coord(c)
            self.set_facing(c)

        if self.move_is_clear(move):
            self.owner.coord.set(move)
        else:
            self.owner.bump(move)

    def get_dir_coord(self, c):
        dx, dy = MobilityComponent.dir_mods[c]
        x, y = self.owner.coord.get
        return dx + x, dy + y

    def set_facing(self, c):
        self.facing = c

    def move_is_clear(self, (x, y)):

        floor = self.level.base_map.get_tile_code((x, y)) == '.'

        feature = self.level.base_map.feature_map.feature_map.get((x, y))
        if feature is not None:
            feature = not feature.block_move
        else:
            feature = True



        return floor and feature
