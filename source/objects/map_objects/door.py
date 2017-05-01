from map_object import MapObject
from source.image.tilesets.tileset_archive import TileSetArchive
from source.states.settings import Settings


class Door(MapObject):

    states = {0: 'closed', 1: 'open'}

    def __init__(self, coord, orientation, style):

        self.style = style
        self.orientation = orientation  # hor or ver
        MapObject.__init__(self, coord)

        self.state = 0
        self.block_view = True
        self.block_move = True

    def set_images(self):
        tileset = TileSetArchive.get_tileset(self.style)
        images = {}
        for k in ('closed', 'open'):
            key = '_'.join((self.orientation, k))
            images[k] = tileset.get_tile_image(key)
            if self.orientation == 'ver':
                top_key = '_'.join((self.orientation, k, 'top'))
                k2 = '_'.join((k, 'top'))
                images[k2] = tileset.get_tile_image(top_key)
        return images

    def get_image_key(self):
        return Door.states[self.state]

    @property
    def top_image_key(self):
        return '_'.join((self.get_image_key(), 'top'))

    def draw_to_map(self, surface, view):
        draw_coord = self.pixel_coord.subtract(view.pixel_coord)
        self.current_image.position(draw_coord)
        self.current_image.draw(surface)

        if self.orientation == 'ver':
            self.draw_top_to_map(surface, draw_coord)

    def draw_top_to_map(self, surface, (dx, dy)):

        image = self.images[self.top_image_key]
        top_coord = (dx, dy - Settings.SC_TILE_H)
        image.position(top_coord)
        image.draw(surface)

    def open(self):
        self.state = 1
        self.block_view = False
        self.block_move = False
        self.level.fov_map.update_point(self.coord.get)

    def close(self):
        self.state = 0
        self.block_move = True
        self.block_view = True
        self.level.fov_map.update_point(self.coord.get)

    def toggle(self):
        if self.state == 0:
            self.open()
        elif self.state == 1:
            self.close()

    def on_bump(self):
        if self.state == 0:
            self.open()

    def on_click(self):
        self.toggle()
