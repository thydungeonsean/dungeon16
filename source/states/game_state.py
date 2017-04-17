from state import State
import pygame
from source.image.map_image.map_image_generator import MapImageGenerator
from source.states.view import View


class GameState(State):

    def load_level(self, level):
        self.level = level
        self.map_image = MapImageGenerator.generate_image(self.level, scale=2)

    def __init__(self):
        State.__init__(self)
        self.level = None
        self.map_image = None
        self.view = View()

    def render(self):

        self.view.draw(self.screen)
        self.screen_layout.draw(self.screen)

    def run(self):
        pass