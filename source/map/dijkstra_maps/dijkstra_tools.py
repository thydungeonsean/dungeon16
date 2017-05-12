

def walker_passable(self, point):
    return passable(self, point, ('.', '~'))


def floor_walker_passable(self, point):
    return passable(self, point, ('.',))


def flyer_passable(self, point):
    return passable(self, point, ('.', '~', '"'))


def swimmer_passable(self, point):
    return passable(self, point, ('~',))


def passable(self, point, valid_terrain):
    return self.base_map.get_tile_code(point) in valid_terrain


# functions - get_sources
def get_party_source():
    pass


def get_flee_source():
    pass


def get_ally_source():
    pass


def get_range_source():
    pass


functions = {
    'walker': walker_passable,
    'floor_walker': floor_walker_passable,
    'flyer': flyer_passable,
    'swimmer': swimmer_passable,

    'party': get_party_source,
    'flee': get_flee_source,
    'range': get_range_source,
    'ally': get_ally_source
}
