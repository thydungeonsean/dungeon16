import pygame


class Clock(object):

    instance = None

    frame_roll = 120

    half_point = frame_roll / 4
    third_point = frame_roll / 6
    quarter_point = frame_roll / 8

    speed = {
        2: half_point,
        3: third_point,
        4: quarter_point
    }

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.frame = 0

    def tick(self, fps):
        self.clock.tick(fps)
        self.increment_frame()

    def get_fps(self):
        return self.clock.get_fps()

    def increment_frame(self):
        self.frame += 1
        if self.frame > Clock.frame_roll:
            self.frame = 0

    def get_anikey(self, speed=2, mod=0):
        if self.frame == 0:
            return 'a'
        if (self.frame / (Clock.speed[speed]+mod)) % 2 == 0:
            return 'a'
        return 'b'
