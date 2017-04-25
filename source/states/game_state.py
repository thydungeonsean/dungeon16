from state import State
from source.image.map_image.map_image_generator import MapImageGenerator
from source.states.view import View
from source.states.settings import Settings

from source.objects.object_managers.feature_manager import FeatureManager


class GameState(State):

    def __init__(self):
        State.__init__(self)
        self.level = None
        self.map_image = None
        self.view = View(self)

        self.feature_manager = FeatureManager(self)

    def init_state(self):
        self.controller.bind_to_state(self)
        self.switch_screen_layout()

    def render(self):

        self.view.draw(self.screen)
        self.screen_layout.draw(self.screen)

    def run(self):
        pass

    def load_level(self, level):
        self.level = level
        self.map_image = MapImageGenerator.generate_image(self.level, scale=Settings.SCALE)

        self.view.set_map_image(self.map_image)

        self.view.init()

        self.feature_manager.init()
