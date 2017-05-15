from state import State
from source.image.map_image.map_image_generator import MapImageGenerator
from source.states.view import View
from source.states.settings import Settings

from source.objects.object_draw_managers.feature_draw_manager import FeatureDrawManager
from source.objects.object_draw_managers.actor_draw_manager import ActorDrawManager
from source.objects.object_draw_managers.shroud_draw_manager import ShroudDrawManager
from source.objects.object_draw_managers.effect_draw_manager import EffectDrawManager

from source.states.message_system.message_center import MessageCenter


class GameState(State):

    def __init__(self):
        State.__init__(self)
        self.level = None
        self.view = View(self)

        self.feature_manager = FeatureDrawManager(self)
        self.actor_manager = ActorDrawManager(self)
        self.shroud_manager = ShroudDrawManager(self)
        self.effect_draw = EffectDrawManager(self)

    def init_state(self):
        self.controller.bind_to_state(self)
        self.switch_screen_layout()

    def render(self):

        self.view.draw(self.screen)
        self.screen_layout.draw(self.screen)

    def run(self):

        MessageCenter.get_instance().run()

        self.level.effects.run()
        self.level.dijkstra_manager.run()

    def load_level(self, level):

        self.level = level

        self.view.set_map_image(self.level.map_image)

        self.view.init()

        self.feature_manager.init()
        self.actor_manager.init()
        self.shroud_manager.init()
        self.effect_draw.init()
