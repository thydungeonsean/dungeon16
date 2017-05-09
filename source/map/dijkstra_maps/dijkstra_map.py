

class DijkstraMap(object):

    def __init__(self, w, h, base_map, is_passable):

        self.w = w
        self.h = h

        self.base_map = base_map
        self.passable_func = is_passable

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
        return self.passable_func(self.base_map, (x, y))

    def set_batch_values(self, batch, value):
        map(self.set_value, batch, [value for v in range(len(batch))])

    def calculate(self, r_source):

        source, perimeter_value = self.parse_source(r_source)

        touched = set(source[:])

        self.set_batch_values(source, perimeter_value)

        perimeter = source

        while perimeter:
            perimeter_value += 1

            perimeter = self.get_perimeter(perimeter, touched, perimeter_value)
            self.set_batch_values(perimeter, perimeter_value)

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
            return tuple([r_source]), 0
        elif isinstance(r_source, list):
            return r_source, 0

    def _print(self):

        for y in range(self.h):
            line = []
            for x in range(self.w):
                line.append(str(self.get_value((x, y))))
            print '  '.join(line)


class DijkstraMapOLD(object):
    def __init__(self, w, h, goals):
        self.xlim = w
        self.ylim = h

        self.map = {}
        self.load_map()

        self.goals = goals

        self.initialize_map()

    def print_map(self):

        for y in range(self.ylim):
            line = ''
            for x in range(self.xlim):
                if (x, y) in self.map.keys():
                    num = str(self.map[(x, y)])
                    if len(num) < 3:
                        num = ' %s' % num
                    if len(num) < 2:
                        num = '%s ' % num
                    line += num
                else:
                    line += '   '

            print line

    def load_map(self):

        for y in range(self.ylim):
            for x in range(self.xlim):
                self.map[(x, y)] = 999

    def initialize_map(self):

        active_points = []
        for point in self.goals:
            self.map[point] = 0
            active_points.append(point)

        complete = False

        active_points = self.run_dijkstra(active_points, start=True)

        while not complete:

            active_points = self.run_dijkstra(active_points)

            if not active_points:
                complete = True

    def run_dijkstra(self, checklist, start=False):

        next_points = []

        for point in checklist:
            change = False
            neighbours, neighbour_values = self.get_neighbour_points(point)
            lowest = min(neighbour_values)

            if self.map[point] >= lowest + 2:
                self.map[point] = lowest + 1
                change = True

            if change or start:
                next_points.extend(neighbours)

        return next_points

    def get_neighbour_points(self, (x, y)):

        points = ((x, y - 1),
                  (x, y + 1),
                  (x - 1, y),
                  (x + 1, y)
                  )
        neighbours = []
        values = []

        for point in points:

            try:
                values.append(self.map[point])
                neighbours.append(point)
            except KeyError:
                pass

        return neighbours, values
