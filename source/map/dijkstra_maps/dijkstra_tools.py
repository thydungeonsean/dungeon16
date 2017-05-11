

def walker_passable(self, point):
    return passable(self, point, ('.',))


def mover_passable(self, point):
    return passable(self, point, ('.', '~'))


def flyer_passable(self, point):
    return passable(self, point, ('.', '~', '"'))


def swimmer_passable(self, point):
    return passable(self, point, ('~',))


def passable(self, point, valid_terrain):
    return self.get_tile_code(point) in valid_terrain
