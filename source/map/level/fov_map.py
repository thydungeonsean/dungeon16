from source.libtcod import libtcodpy as libtcod


class FOVMap(object):

    SIGHT_RADIUS = 8
    LIGHT_WALLS = True
    ALGO = 4

    def __init__(self, level):

        self.level = level

        self.w = level.base_map.w
        self.h = level.base_map.h

        self.map = libtcod.map_new(self.w, self.h)
        self.set_fov_map()

        self.recompute = True

        self.shroud = None
        self.explore_map = {}

    # init fov
    def set_fov_map(self):

        for point in self.level.base_map.all_coords:
            self.set_fov_map_point(point)

    def set_fov_map_point(self, (x, y)):
        libtcod.map_set_properties(self.map, x, y, self.point_transparent((x, y)), True)

    def point_transparent(self, point):

        wall = self.level.base_map.get_tile_code(point) == '#'
        if wall:
            return False

        feature = self.level.feature_map.feature_map.get(point)
        if feature is not None:
            if feature.block_view:
                return False

        return True

    # make single point fov changes on the fly (for open and close doors / abilities / spells)
    def update_point(self, point):
        self.set_fov_map_point(point)
        self.needs_recompute()

    # toggle recomputing, and recomputing
    def needs_recompute(self):
        self.recompute = True

    def recompute_fov(self, map_object, view):
        cls = FOVMap
        self.recompute = False
        x, y = map_object.coord.get
        libtcod.map_compute_fov(self.map, x, y, cls.SIGHT_RADIUS, cls.LIGHT_WALLS, cls.ALGO)

        self.update_shroud_points(view)

    ################################################
    # getting values from map
    def point_is_visible(self, (x, y)):
        return libtcod.map_is_in_fov(self.map, x, y)
    ################################################

    def update_shroud_points(self, view):

        tlx, tly = view.coord.get
        brx, bry = tlx + view.width, tly + view.height

        coords_in_view = []
        for y in range(tly, bry):
            for x in range(tlx, brx):
                coords_in_view.append((x, y))

        self.shroud = filter(lambda p: not self.point_is_visible(p), coords_in_view)
        self.explore_coords(list(filter(lambda p: self.point_is_visible(p), coords_in_view)))

    def explore_coords(self, points):
        for point in points:
            self.explore_map[point] = True

    def is_explored(self, point):
        return self.explore_map.get(point, False)
