

class TurnManager(object):

    phases = {1: 'party',
              2: 'npc',
              3: 'monster'}

    def __init__(self, level):

        self.level = level

        self.phase = TurnManager.phases[1]

    def run(self):
        pass
