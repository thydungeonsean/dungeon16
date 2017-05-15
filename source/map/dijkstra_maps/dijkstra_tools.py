

def walker_passable(level, point):
    return passable(level, point, ('.', '~'))


def floor_walker_passable(level, point):
    return passable(level, point, ('.',))


def flyer_passable(level, point):
    return passable(level, point, ('.', '~', '"'))


def swimmer_passable(level, point):
    return passable(level, point, ('~',))


def passable(level, point, valid_terrain):
    return level.base_map.get_tile_code(point) in valid_terrain


# functions - get_sources
def get_party_source(level, *args):
    actors = filter(lambda x: x.profile['group'] == 'party', level.actors.actors)
    return [x.coord.get for x in actors]


def get_flee_source(level, *args):
    map_key = args[0]
    mod = -1.2
    inverse_map = level.dijkstra_collection.access_map(map_key)
    inverse_map.calculate()  # temporary -- need to assert target map is up to date

    transform = [[invert_value(inverse_map.get_value((x, y)), mod) for y in range(inverse_map.h)]
                 for x in range(inverse_map.w)]
    lowest = 0

    for (x, y) in inverse_map.all_coords:
        if transform[x][y]is not None and transform[x][y] < lowest:
            lowest = transform[x][y]

    return filter(lambda (x, y): transform[x][y] == lowest, inverse_map.all_coords)


def invert_value(value, mod):
    if value is None:
        return None
    return int(value * mod)


def get_key_actor_source(level, *args):
    key = args[0]
    value = args[1]
    actors = filter(lambda x: x.profile[key] == value, level.actors.actors)
    return [x.coord.get for x in actors]


def get_range_source(level, *args):

    map_key = args[0]
    target_map = level.dijkstra_collection.access_map(map_key)
    target_map.calculate()

    min_range = args[1]
    max_range = args[2]

    return filter(lambda (x, y): min_range <= target_map.get_value((x, y)) <= max_range, target_map.all_coords)


functions = {

    'party': get_party_source,
    'flee': get_flee_source,
    'range': get_range_source,
    'key-actor': get_key_actor_source,

    'walker': walker_passable,
    'floor-walker': floor_walker_passable,
    'flyer': flyer_passable,
    'swimmer': swimmer_passable,

}
