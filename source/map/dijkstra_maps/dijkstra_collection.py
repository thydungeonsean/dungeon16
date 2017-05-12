

class DijkstraCollection(object):
    def __init__(self, level):
        self.level = level
        self.collection = {}

    def access_map(self, map_key):
        if map_key not in self.collection.keys():
            self.collection[map_key] = self.generate_map(map_key)

        return self.collection[map_key]

    def generate_map(self, map_key):
        pass
    # need source dict/list
    # need passable_func - from dijkstra_tools
    # "attack_party_walker"
