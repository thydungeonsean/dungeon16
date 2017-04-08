from ..controller.controller import Controller
from clock import Clock
from screen_layout import ScreenLayout  # dummy layout


class State(object):
    
    def __init__(self):
        self.controller = Controller.get_instance()
        self.screen_layout = None

        self.clock = Clock.get_instance()

    def init_state(self):
        self.controller.bind_to_state(self)
        self.switch_screen_layout()

    def deinit_state(self):
        raise NotImplementedError

    def switch_screen_layout(self):
        self.screen_layout = ScreenLayout()
        self.screen_layout.init_state(self)

    def handle_input(self):
        self.controller.handle_input()

    def render(self):
        raise NotImplementedError

    def run(self):
        pass
