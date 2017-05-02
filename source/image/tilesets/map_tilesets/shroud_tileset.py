from source.image.tilesets.tileset import TileSet
from source.image.image import Image


class ShroudTileSet(TileSet):

    def __init__(self):
        TileSet.__init__(self, 'shroud', 'shroud', 'shroud')

    def set_tile_image(self, key):

        alpha = False
        if key.endswith('_trans'):
            alpha = 165

        colorkey = self.colorkey
        if key.startswith('full'):
            colorkey = None

        tile = Image(self.tile_w, self.tile_h, colorkey=colorkey, alpha=alpha, auto_scale=False)
        tx, ty = self.tileset_pos_dict[key]
        tile.image.blit(self.tilesheet, (0, 0), (tx*self.tile_w, ty*self.tile_h, self.tile_w, self.tile_h))
        tile.auto_scale()
        return tile