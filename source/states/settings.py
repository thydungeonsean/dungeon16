

class Settings(object):

    SCALE = 2
    TILE_W = 16
    TILE_H = 16

    SC_TILE_W = TILE_W * SCALE
    SC_TILE_H = TILE_H * SCALE

    MOVE_ANIMATION = True

    @classmethod
    def set_scate(cls, scale):
        cls.SCALE = scale
        # rescale all images