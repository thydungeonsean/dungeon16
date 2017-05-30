from party_member import PartyMember
from stat_component import get_invincible_stats


class Player(PartyMember):

    def __init__(self, point, sprite):

        PartyMember.__init__(self, point, sprite, 1)

    def set_ai_tag(self):
        return 'player'

    def set_stats(self):
        return get_invincible_stats(self)
