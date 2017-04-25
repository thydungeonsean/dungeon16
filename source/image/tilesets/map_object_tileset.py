from tileset import TileSet


class MapObjectTileSet(TileSet):

    def __init__(self, set_type, set_id):
        sheet_id = self.set_sheet_id()
        TileSet.__init__(self, sheet_id, set_type, set_id)
        self.set_type = set_type
        self.set_id = set_id

    def set_sheet_id(self):
        raise NotImplementedError
