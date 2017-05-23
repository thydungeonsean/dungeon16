from action import Action


class MoveAction(Action):

    def __init__(self, *args):
        Action.__init__(self, 'move')
        self.complete = True
        self.owner = args[0]
        self.move = args[1]

    def run(self):

        if self.complete:
            self.complete_move()
            return 'complete'

    def complete_move(self):
        self.owner().mobility_component.move(self.move)

