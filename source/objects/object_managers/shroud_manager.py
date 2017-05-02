from source.image.tilesets.map_tileset_archive import MapTileSetArchive
from source.states.settings import Settings


class ShroudManager(object):

    def __init__(self, state):

        self.state = state
        self.view = state.view
        self.fov = None

    def init(self):
        self.fov = self.state.level.fov_map

    def draw(self, surface):

        vx, vy = self.view.coord.get

        shroud = MapTileSetArchive.get_tileset('shroud').get_tile_image('full')
        fog = MapTileSetArchive.get_tileset('shroud').get_tile_image('full_trans')

        for x, y in self.fov.shroud:
            tx = (x - vx) * Settings.SC_TILE_W
            ty = (y - vy) * Settings.SC_TILE_H

            if self.fov.is_explored((x, y)):
                fog.position((tx, ty))
                fog.draw(surface)
            else:
                shroud.position((tx, ty))
                shroud.draw(surface)

