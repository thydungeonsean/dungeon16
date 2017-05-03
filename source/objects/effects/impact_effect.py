from source.objects.effects.effect import Effect


class ImpactEffect(Effect):

    frame_dur = 3

    frame_seq = ('a', 'b', 'c')

    def __init__(self, point, effect_img):
        Effect.__init__(self, point, effect_img)

        self.ani_frame = 'a'
        self.i = 0
        self.end_tick = ImpactEffect.frame_dur * 3

    def get_image_key(self):
        return self.ani_frame

    def run_tick(self):
        cls = ImpactEffect
        if self.tick % cls.frame_dur == 0:
            self.next_frame()

    def next_frame(self):

        cls = ImpactEffect
        self.i += 1
        if self.i >= len(cls.frame_seq):
            self.i -= 1
        self.ani_frame = cls.frame_seq[self.i]
