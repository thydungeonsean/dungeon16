from controller import Controller


class ControlComponent(object):

    def __init__(self):

        self.key_map = self.set_key_map()

        c = Controller.get_instance()
        c.add_component(self)

    def press(self, key):
        try:
            self.key_map[key]()
        except KeyError:
            pass

    def set_key_map(self):
        return {}

    def delete(self):
        c = Controller.get_instance()
        c.remove_component(self)
