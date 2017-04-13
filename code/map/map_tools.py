

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
    def wall_casts_shadow(base_map, coord):
        adj = base_map.get_adj_tile_dict(coord)
        if 's' in adj['directions'] and adj['s'] == '.':
            return True
        return False
