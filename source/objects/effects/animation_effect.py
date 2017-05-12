from effect import Effect
from source.states.settings import Settings


class AnimationEffect(Effect):

    def __init__(self, actor):

        self.actor = actor
        point = self.actor.coord.get

        Effect.__init__(self, point, None)
        self.drawable = False

    def set_images(self):
        return {}

    def run_tick(self):

        self.actor.pixel_coord.set_offsets(self.get_offset_for_frame())

    def get_offset_for_frame(self):
        raise NotImplementedError


class Bump(AnimationEffect):

    frame_duration = 1

    frame_sequence = (1, 2, 3, 5, 5, 3, 2, 1, 0)

    def __init__(self, actor, target):

        AnimationEffect.__init__(self, actor)
        self.i = 0
        cls = Shake
        self.end_tick = cls.frame_duration * len(cls.frame_sequence)
        self.frame_mod = self.set_frame_mod(target)

    def set_frame_mod(self):

        return

    def get_offset_for_frame(self):
        pass


class Shake(AnimationEffect):

    frame_duration = 2

    frame_sequence = (1, -1, 1, -1, 1, -1, 0)

    def __init__(self, actor):

        AnimationEffect.__init__(self, actor)
        self.i = 0
        cls = Shake
        self.end_tick = cls.frame_duration * len(cls.frame_sequence)

    def get_offset_for_frame(self):
        cls = Shake

        if self.tick % cls.frame_duration == 0:
            self.i += 1
            if self.i >= len(cls.frame_sequence):
                self.i -= 1

        return cls.frame_sequence[self.i]*Settings.SCALE, 0

