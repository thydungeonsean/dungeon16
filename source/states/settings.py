

class Settings(object):

    SCALE = 1
    TILE_W = 16
    TILE_H = 16

    SC_TILE_W = TILE_W * SCALE
    SC_TILE_H = TILE_H * SCALE

    @classmethod
    def set_scate(cls, scale):
        cls.SCALE = scale
        # rescale all images