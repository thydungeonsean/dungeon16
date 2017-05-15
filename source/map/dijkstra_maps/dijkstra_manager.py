

class DijkstraManager(object):

    def __init__(self, level):

        self.level = level

    def run(self):

        for d_map in self.level.dijkstra_collection.collection.values():
            if d_map.needs_update:
                d_map.calculate()
