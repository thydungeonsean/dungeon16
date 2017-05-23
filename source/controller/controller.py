import pygame
import sys
from mouse import Mouse
from pygame.locals import *


class Controller(object):

    key_bind = {
        'esc': K_ESCAPE,
        'ret': K_RETURN,
        'up': K_UP,
        'down': K_DOWN,
        'right': K_RIGHT,
        'left': K_LEFT,
        'wait': K_z
    }

    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance

    def __init__(self):

        self.mouse = Mouse.get_instance()
        self.state = None

        self.components = {}

    def bind_to_state(self, state):
        self.state = state
        self.mouse.bind_to_state(state)

    def unbind(self):
        self.state = None
        self.mouse.unbind()

    def add_component(self, component, c_id):
        self.components[c_id] = component

    def remove_component(self, c_id):
        del self.components[c_id]

    def turn_off_move_control(self):
        self.remove_component('move_control')

    def handle_input(self):

        mouse_moved = False

        for event in pygame.event.get():

            if event.type == QUIT:
                self.end_program()

            elif event.type == KEYDOWN:
                if event.key == self.key('esc'):
                    self.end_program()

                elif event.key == self.key('ret'):
                    pass

                else:
                    for component in self.components.values():
                        component.press(event.key)

            elif event.type == MOUSEBUTTONDOWN:

                if event.button == 1:
                    self.mouse.click()

                elif event.button == 3:
                    self.mouse.right_click()

            elif event.type == MOUSEMOTION:
                mouse_moved = True
                self.mouse.motion()

            elif event.type == MOUSEBUTTONUP:
                self.mouse.button_up()

        if not mouse_moved:
            self.mouse.hover()
        else:
            self.mouse.reset_hover()

    def key(self, k):
        cls = Controller
        return cls.key_bind[k]

    def end_program(self):
        pygame.quit()
        sys.exit()
