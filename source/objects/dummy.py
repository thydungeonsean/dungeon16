from actor import Actor


class Dummy(Actor):

    def __init__(self, x, y):
        Actor.__init__(self, (x, y))
