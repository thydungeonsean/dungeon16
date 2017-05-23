

class Action(object):

    def __init__(self, name):

        self.name = name

    def run(self):

        raise NotImplementedError

