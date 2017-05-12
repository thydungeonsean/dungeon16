

class DijkstraMap(object):

    # returns a new DijkstraMap with d_map values transformed - for flee map
    @classmethod
    def flee_map(cls, d_map, mod):

        new = cls(d_map.w, d_map.h, d_map.base_map, d_map.passable_func)

        transform = [[int(d_map.get_value((x, y)) * mod) for y in range(d_map.h)] for x in range(d_map.w)]
        lowest = 0

        coords = []

        for y in range(new.h):
            for x in range(new.w):
                coords.append((x, y))
                if transform[x][y] < lowest:
                    lowest = transform[x][y]

        flee_src = filter(lambda (x, y): transform[x][y] == lowest, coords)

        new.calculate(flee_src)

        return new

    def __init__(self, w, h, level, passable, source):

        self.w = w
        self.h = h

        self.level = level
        self.passable_func = passable
        self.source_func = source

        self.d_map = self.set_d_map()
        self.count = 0

    def set_d_map(self):

        return [[0 for y in range(self.h)] for x in range(self.w)]

    def set_value(self, (x, y), value):
        self.d_map[x][y] = value
        self.count += 1

    def get_value(self, (x, y)):
        return self.d_map[x][y]

    def is_passable(self, (x, y)):
        return self.passable_func(self.level, (x, y))

    def add_source_values(self, batch, value):
        return filter(lambda p: self.get_value(p) > value, batch)

    def set_batch_values(self, batch, value):
        map(self.set_value, batch, [value for v in range(len(batch))])

    def calculate(self):
        source = self.source_func()
        self.calculate_source(source)

    def calculate_source(self, r_source):

        source = self.parse_source(r_source)
        perimeter_value = min(source.keys())
        touched = set()

        perimeter = source[perimeter_value]

        while perimeter:

            if perimeter_value in source.keys():
                new_source = self.add_source_values(source[perimeter_value], perimeter_value)
                perimeter.update(new_source)

            self.set_batch_values(perimeter, perimeter_value)

            perimeter_value += 1
            perimeter = self.get_perimeter(perimeter, touched, perimeter_value)

    def get_perimeter(self, batch, touched, value):

        perimeter = set()

        for point in batch:
            adj = self.get_adj(point, touched, value)

            touched.update(adj)
            perimeter.update(adj)

        return perimeter

    def get_adj(self, (x, y), touched, value):
        adj = filter(lambda p: self.is_passable(p), ((x+1, y), (x-1, y), (x, y+1), (x, y-1)))
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
                tag = str(self.get_value((x, y)))
                gap = 3-len(tag)

                line.append(''.join([tag, ' '*gap]))
            print '  '.join(line)
