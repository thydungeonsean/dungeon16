import pygame


class Clock(object):

    instance = None

    frame_roll = 60

    half_point = frame_roll / 2
    third_point = frame_roll / 3
    quarter_point = frame_roll / 4

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
