from dijkstra_map import DijkstraMap
from dijkstra_tools import parse_map_key, get_subscription_tags


class DijkstraCollection(object):

    def __init__(self, level):

        self.level = level
        self.collection = {}

    def access_map(self, map_key):
        if map_key not in self.collection.keys():
            self.collection[map_key] = self.generate_map(map_key)

        return self.collection[map_key]

    def generate_map(self, map_key):

        passable, source, source_args = parse_map_key(map_key)
        subscriber_ids, subscription_tags = get_subscription_tags(map_key)

        return DijkstraMap(self.level, passable, source, source_args, subscriber_ids, subscription_tags)
