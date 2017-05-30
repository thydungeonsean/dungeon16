from ai_component import AIComponent
from player_ai_component import PlayerAIComponent
from party_ai_component import PartyAIComponent


class AIArchive(object):

    @classmethod
    def get_ai(cls, owner, ai_key):

        if ai_key == 'basic':
            return AIComponent(owner)

        elif ai_key == 'player':
            return PlayerAIComponent(owner)

        elif ai_key == 'party':
            return PartyAIComponent(owner)

        raise Exception('invalid ai type requested')
