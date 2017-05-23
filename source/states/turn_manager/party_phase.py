from turn_phase import TurnPhase
from source.controller.controller import Controller
from source.controller.move_control import MoveControl


class PartyPhase(TurnPhase):

    def __init__(self, level):
        TurnPhase.__init__(self, level)

    def is_available(self, actor):
        # actor is party member
        return actor.profile['group'] == 'party'

    def sort_available(self):
        self.available_actors = sorted(self.available_actors, key=lambda p: p.profile['party_rank'], reverse=True)
        return

    @staticmethod
    def party_order(party_member):
        return party_member.profile['party_rank']

    def initialize_phase(self):
        self.available_actors = self.get_available_actors()
        self.sort_available()  # player character must always have party rank 1

        MoveControl(self.available_actors[-1])  # binds movement keys to controlling party leader

    def deinitialize_phase(self):
        Controller.get_instance().turn_off_move_control()
