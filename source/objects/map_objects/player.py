from party_member import PartyMember


class Player(PartyMember):

    def __init__(self, point, sprite):

        PartyMember.__init__(self, point, sprite, 1)

    def set_ai_tag(self):
        return 'player'
