from ai_component import AIComponent
from player_ai import PlayerAI


class AIArchive(object):

    @classmethod
    def get_ai(cls, owner, ai_key):

        if ai_key == 'basic':
            return AIComponent(owner)

        elif ai_key == 'player':
            return PlayerAI(owner)

        elif ai_key == 'party':
            return AIComponent(owner)
            return  #PartyAI(owner)

        raise Exception('invalid ai type requested')
