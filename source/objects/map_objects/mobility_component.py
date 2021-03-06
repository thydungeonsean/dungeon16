import weakref


class MobilityComponent(object):

    dir_mods = {
        'up': (0, -1),
        'down': (0, 1),
        'right': (1, 0),
        'left': (-1, 0)
    }

    def __init__(self, owner):
        self.owner = weakref.ref(owner)
        self.level = None

        self.facing = 'down'

    def set_level(self, level):
        self.level = level

    def try_move(self, c):
        if isinstance(c, tuple):
            move = c
        else:
            move = self.get_dir_coord(c)
            self.set_facing(c)

        clear, blocker = self.move_is_clear(move)
        if clear:
            #self.move(move)
            return 'move', [move]
        else:
            if blocker is not None:
                #self.bump(blocker)
                return 'bump', [blocker]
        return None

    def get_dir_coord(self, c):
        dx, dy = MobilityComponent.dir_mods[c]
        x, y = self.owner().coord.get
        return dx + x, dy + y

    def set_facing(self, c):
        self.facing = c

    def move_is_clear(self, move):
        # returns boolean if move is successful or not
        # and if not, it gives the blocking entity as the second value
        # otherwise returns None as second value

        floor = self.level.base_map.get_tile_code(move) in ('.', '~')
        if not floor:
            return floor, None

        block = move not in self.level.base_map.block_map.block_coords
        if not block:
            return block, None

        feature = self.level.feature_map.feature_map.get(move)
        if feature is not None:
            if feature.block_move:
                return False, feature

        actor_ref = self.level.actor_list.actor_map.get(move)
        if actor_ref is not None:
            return False, actor_ref()

        return True, None

    def move(self, point):
        self.owner().move(point)

    def bump(self, target):
        self.owner().bump(target)

