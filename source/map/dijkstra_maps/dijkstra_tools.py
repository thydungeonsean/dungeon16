

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


def parse_range_tokens(tokens):

    min = int(tokens[1])
    i = 2
    if tokens[2].isdigit():
        max = int(tokens[2])
        i = 3
    else:
        max = min

    target = '_'.join(tokens[i:])
    return [target, min, max]


def parse_map_key(map_key):

    tokens = map_key.split('_')
    source = functions[tokens[0]]
    if tokens[0] == 'key-actor':
        source_args = tokens[1:-1]
    elif tokens[0] == 'flee':
        source_args = ['_'.join(tokens[1:])]
    elif tokens[0] == 'range':
        source_args = parse_range_tokens(tokens)
    else:
        source_args = []

    passable = functions[tokens[-1]]
    return passable, source, source_args


def get_subscription_tags(map_key):

    tokens = map_key.split('_')

    if tokens[0] == 'party':
        return ('actor_move', 'actor_die'), {('group', 'party')}

    elif tokens[0] == 'key-actor':
        return ('actor_move', 'actor_die'), {(tokens[1], tokens[2])}

    elif tokens[0] == 'flee':
        sub_key = '_'.join(tokens[1:])
        return get_subscription_tags(sub_key)

    elif tokens[0] == 'range':
        target, min, max = parse_range_tokens(tokens)
        return get_subscription_tags(target)


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
