from code.image.tile_sheet_archive import TileSheetArchive as TSA
from code.image.tilesets.tile_set import TileSet


class MapTileSet(TileSet):

    def __init__(self, set_type, set_id):
        
        sheet_id = 'world'
        TileSet.__init__(self, sheet_id, set_type, set_id)
        self.set_type = set_type
        self.set_id = set_id

    def load_tile_sheet(self):
        if TSA.world_sheet is None:
            TSA.load_world_sheet()
        return TSA.world_sheet

    def get_base_tile(self, **kwargs):
        raise NotImplementedError

    def get_varied_tile(self, **kwargs):
        raise NotImplementedError


