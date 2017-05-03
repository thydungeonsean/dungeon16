

class ObjectDrawManager(object):

    def __init__(self, state):

        self.state = state
        self.view = self.state.view

    def init(self):
        raise NotImplementedError

    def draw(self, surface):

        raise NotImplementedError
