from party_phase import PartyPhase
from npc_phase import NPCPhase
from monster_phase import MonsterPhase


class TurnManager(object):

    def __init__(self, level):

        self.level = level

        self.step = 0
        self.phases = [PartyPhase(level), NPCPhase(level), MonsterPhase(level)]
        self.phase = self.phases[0]

        self.printout = ''

    def run(self):
        end = self.phase.run()

        if str(self.phase) != self.printout:
            self.printout = str(self.phase)
            print self.printout

        if end:
            self.step += 1
            if self.step == 3:
                self.step = 0
            self.phase = self.phases[self.step]
