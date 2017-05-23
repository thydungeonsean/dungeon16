from turn_phase import TurnPhase


class NPCPhase(TurnPhase):
    def __init__(self, level):
        TurnPhase.__init__(self, level)

    def is_available(self, actor):
        return actor.profile['group'] == 'NPC'

    def sort_available(self):
        self.available_actors = sorted(self.available_actors, key=lambda npc: npc.ai.dist_to_player, reverse=True)
