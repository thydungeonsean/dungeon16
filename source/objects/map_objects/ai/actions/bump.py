from action import Action


class BumpAction(Action):

    def __init__(self, *args):
        Action.__init__(self, 'bump')
        self.complete = True
        self.owner = args[0]
        self.target = args[1]

    def run(self):
        if self.complete:
            self.complete_bump()
            return 'complete'

    def complete_bump(self):
        self.owner().mobility_component.bump(self.target)
