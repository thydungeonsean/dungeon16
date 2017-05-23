from controller import Controller


class ControlComponent(object):

    def __init__(self, control_id):

        self.key_map = self.set_key_map()

        c = Controller.get_instance()
        c.add_component(self, control_id)

    def press(self, key):
        press_function = self.key_map.get(key)
        if press_function is not None:
            press_function()

    def set_key_map(self):
        return {}

