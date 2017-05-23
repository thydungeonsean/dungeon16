from turn_phase import TurnPhase


class MonsterPhase(TurnPhase):

    def __init__(self, level):
        TurnPhase.__init__(self, level)

    def is_available(self, actor):

        # when a monster actor needs to be given a turn
        # - filtering from actor list
        if not actor.profile['group'] == 'monster':
            return False
        if not actor.ai.state == 'active':
            return False

        return True

    def sort_available(self):  # nearest monsters to player act first
        self.available_actors = sorted(self.available_actors, key=lambda m: m.ai.dist_to_player, reverse=True)
