from random import choice


class MapTools(object):

    @staticmethod
    def wall_is_isolate(adj):
        for d in adj['directions']:
            if adj[d] != '#':
                return False
        return True

    @staticmethod
    def wall_is_single_width(adj):

        profile = []
        directions = ('n', 's', 'e', 'w')
        for d in directions:
            if d in adj['directions']:
                if adj[d] == '#':
                    profile.append(1)
                else:
                    profile.append(0)
            else:
                if d == 's':
                    profile.append(1)
                else:
                    profile.append(0)
        if profile == [1, 1, 0, 0] or profile == [0, 0, 1, 1]:
            return True

        return False

    @staticmethod
    def floor_is_corner(adj):

        adj_walls = set(filter(lambda x: adj[x] == '#', adj['directions']))
        if 'n' in adj_walls and ('e' in adj_walls or 'w' in adj_walls):
            return True
        elif 'e' in adj_walls and 's' in adj_walls:
            return True
        elif 's' in adj_walls and 'w' in adj_walls:
            return True
        else:
            return False

    @staticmethod
    def filter_corners(base_map, floor):
        m = MapTools
        return list(filter(lambda x: m.floor_is_corner(base_map.get_adj_tile_dict(x)), floor))

    @staticmethod
    def get_corner_id(base_map, point):
        adj = base_map.get_adj_tile_dict(point)
        adj_walls = set(filter(lambda x: adj[x] == '#', adj['directions']))
        possible = []
        if 'n' in adj_walls and 'e' in adj_walls:
            possible.append('_tr')
        if 'n' in adj_walls and 'w' in adj_walls:
            possible.append('_tl')
        if 's' in adj_walls and 'e' in adj_walls:
            possible.append('_br')
        if 's' in adj_walls and 'w' in adj_walls:
            possible.append('_bl')
        return choice(possible)

    @staticmethod
    def wall_casts_shadow(base_map, coord):
        adj = base_map.get_adj_tile_dict(coord)
        if 's' in adj['directions'] and adj['s'] == '.':
            return True
        return False

    @staticmethod
    def wall_valid_for_torch(base_map, deco_map, coord):

        adj = base_map.get_adj_tile_dict(coord)

        if 's' in adj['directions'] and adj['s'] in ('.', '"', '~') and adj['s_coord'] not in deco_map.deco_map.keys() \
                and base_map.tile_id_map.tile_id_map[coord][1] != 'hor_d':
            return True
        else:
            return False

    @staticmethod
    def all_floors(base_map):
        return list(filter(lambda x: base_map.get_tile_code(x) == '.', base_map.all_coords))

    @staticmethod
    def all_walls(base_map):
        return list(filter(lambda x: base_map.get_tile_code(x) == '#', base_map.all_coords))

    @staticmethod
    def all_water(base_map):
        return list(filter(lambda x: base_map.get_tile_code(x) == '~', base_map.all_coords))
