from source.objects.map_objects.map_object import MapObject
from source.image.tilesets.sprite_archive import SpriteArchive


class Effect(MapObject):

    def __init__(self, (x, y), effect_img):

        self.effect_img = effect_img

        MapObject.__init__(self, (x, y))
        self.block_move = False

        self.runner = None
        self.tick = 0
        self.end_tick = 0

    def set_runner(self, runner):
        self.runner = runner

    def set_images(self):
        return SpriteArchive.get_effect_tileset(self.effect_img).tiles

    def increment(self):
        self.tick += 1
        self.run_tick()

    def run_tick(self):
        pass

    def run(self):
        self.increment()
        if self.tick > self.end_tick:
            self.end()
            self.end_effect()

    def end(self):
        self.runner.remove_effect(self)

    def end_effect(self):
        pass
