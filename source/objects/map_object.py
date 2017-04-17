from coord import Coord


class MapObject(object):

    def __init__(self, (x, y)):

        self.coord = Coord(x, y)

    def draw(self, surface):
        pass

    def on_bump(self):
        pass
