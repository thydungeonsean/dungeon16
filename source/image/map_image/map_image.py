from source.image.image import Image
from source.objects.map_image_coord import MapImageCoord
from source.states.settings import Settings

from source.states.clock import Clock


class MapImage(object):

    def __init__(self, w, h):

        self.coord = MapImageCoord()

        self.image_a = self.set_image(w, h)
        self.image_b = self.set_image(w, h)
        self.images = {
            'a': self.image_a,
            'b': self.image_b
            }

    @property
    def each_image(self):
        return [self.images[i] for i in self.images.keys()]

    def position(self, (x, y)):
        for image in self.each_image:
            image.position((x, y))

    def draw(self, surface):
        self.get_image(self.get_key()).draw(surface)

    def get_image(self, key):
        return self.images[key]

    def scale_up(self, scale=2):
        for image in self.each_image:
            image.scale_up(scale=scale)

    def set_image(self, w, h):
        pix_w = w * Settings.SC_TILE_W
        pix_h = h * Settings.SC_TILE_H
        i = Image(pix_w, pix_h)
        self.coord.bind(i.coord)
        return i

    def get_key(self):
        frame = Clock.get_instance().frame
        if frame <= Clock.half_point:
            return 'a'
        return 'b'
