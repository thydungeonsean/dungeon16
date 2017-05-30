from source.states.message_system.subscriber import Subscriber
from time import time


class DijkstraMap(object):

    def __init__(self, level, passable, source, source_args, subscriber_ids, subscription_tags, diag=False):

        self.w = level.base_map.w
        self.h = level.base_map.h

        self.level = level
        self.passable_func = passable
        self.source_func = source
        self.source_args = source_args

        self.subscriber = Subscriber(self, subscriber_ids, subscription_tags)

        self.diagonal = diag

        self.d_map = self.set_d_map()

        self.needs_update = True

        self.calculate()

    def receive_report(self):
        self.needs_update = True

    @property
    def all_coords(self):
        coords = []
        for y in range(self.h):
            for x in range(self.w):
                coords.append((x, y))
        return coords

    def set_d_map(self):

        return [[None for y in range(self.h)] for x in range(self.w)]

    def set_value(self, (x, y), value):
        self.d_map[x][y] = value

    def get_value(self, (x, y)):
        try:
            return self.d_map[x][y]
        except IndexError:
            return None

    def is_passable(self, (x, y)):
        return 0 <= x < self.w and 0 <= y < self.h and self.passable_func(self.level, (x, y))

    def add_source_values(self, batch, value):
        return filter(lambda p: self.get_value(p) > value, batch)

    def set_batch_values(self, batch, value):
        map(self.set_value, batch, [value for v in range(len(batch))])

    def calculate(self):
        source = self.source_func(self.level, *self.source_args)
        self.calculate_from_source(source)

    def calculate_from_source(self, r_source):

        source = self.parse_source(r_source)
        perimeter_value = min(source.keys())
        touched = set()

        perimeter = source[perimeter_value]

        # start_time = time()

        while perimeter:

            # if time() - start_time > .01:  #
            #     break

            if perimeter_value in source.keys():
                new_source = self.add_source_values(source[perimeter_value], perimeter_value)
                perimeter.update(new_source)
                touched.update(new_source)

            self.set_batch_values(perimeter, perimeter_value)

            perimeter_value += 1
            perimeter = self.get_perimeter(perimeter, touched, perimeter_value)

        self.needs_update = False

    def get_perimeter(self, batch, touched, value):

        perimeter = set()

        for point in batch:
            adj = self.get_adj(point, touched, value)

            touched.update(adj)
            perimeter.update(adj)

        return perimeter

    def get_adj(self, (x, y), touched, value):

        adj_coords = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        if self.diagonal:
            adj_coords.extend([(x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1)])

        adj = filter(lambda p: self.is_passable(p), adj_coords)
        return filter(lambda p: self.needs_new_value(p, touched, value), adj)

    def needs_new_value(self, p, touched, value):
        return p not in touched or self.get_value(p) > value

    @staticmethod
    def parse_source(r_source):

        if isinstance(r_source, tuple) and len(r_source) == 2:
            return {0: set(r_source)}
        elif isinstance(r_source, list):
            return {0: set(r_source)}
        elif isinstance(r_source, dict):
            return r_source

    def _print(self):

        for y in range(self.h):
            line = []
            for x in range(self.w):
                if self.get_value((x, y)) is None:
                    tag = ' '
                else:
                    tag = str(self.get_value((x, y)))

                gap = 3-len(tag)

                line.append(''.join([tag, ' '*gap]))
            print '  '.join(line)
