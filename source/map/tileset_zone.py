from source.image.tilesets.tileset_archive import TileSetArchive


class TilesetZone(object):

    def __init__(self, point, w, h, set_type, set_id):
        self.point = point
        self.w = w
        self.h = h

        self.set_type = set_type

        self.tileset = TileSetArchive.get_tileset(set_id)

    def is_in_zone(self, (x, y)):
        px, py = self.point
        if px <= x < self.w + px and py <= y < self.h + py:
            return True
        return False
