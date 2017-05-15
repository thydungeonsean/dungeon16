from dijkstra_map import DijkstraMap
from dijkstra_tools import functions as d_funcs


class DijkstraCollection(object):
    def __init__(self, level):
        self.level = level
        self.collection = {}

    def access_map(self, map_key):
        if map_key not in self.collection.keys():
            self.collection[map_key] = self.generate_map(map_key)

        return self.collection[map_key]

    def generate_map(self, map_key):

        passable, source, source_args = self.parse_map_key(map_key)
        subscription_tags = self.get_subscription_tags(map_key)
        return DijkstraMap(self.level, passable, source, source_args, subscription_tags)

    def parse_map_key(self, map_key):

        tokens = map_key.split('_')
        source = d_funcs[tokens[0]]
        if tokens[0] == 'key-actor':
            source_args = tokens[1:-1]
        elif tokens[0] == 'flee':
            source_args = ['_'.join(tokens[1:])]
        elif tokens[0] == 'range':
            source_args = self.parse_range_tokens(tokens)
            print source_args
        else:
            source_args = []

        passable = d_funcs[tokens[-1]]
        return passable, source, source_args

    def parse_range_tokens(self, tokens):

        min = int(tokens[1])
        i = 2
        if tokens[2].isdigit():
            max = int(tokens[2])
            i = 3
        else:
            max = min

        target = '_'.join(tokens[i:])
        return [target, min, max]

    def get_subscription_tags(self, map_key):

        return {('group', 'party')}
