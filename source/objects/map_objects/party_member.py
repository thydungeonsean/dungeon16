from actor import Actor
from stat_component import get_monster_stats
from source.objects.effects.impact_effect import ImpactEffect
from source.states.message_system.message import Message
from source.objects.map_objects.ai.ai_archive import AIArchive


class PartyMember(Actor):

    def __init__(self, point, sprite, rank):

        self.party_rank = rank
        self.ai_tag = self.set_ai_tag()

        Actor.__init__(self, point, sprite)
        self.stat_component = get_monster_stats(self, sprite)

    def set_profile(self):
        return {'allegiance': 'friend', 'group': 'party', 'id': self.sprite, 'party_rank': self.party_rank}

    def set_ai_tag(self):
        return 'party'

    def init_ai(self):
        return AIArchive.get_ai(self, self.ai_tag)

    def report_move(self):
        Message('actor_move', *self.profile.items()).send()

    def hit_actor(self, actor):

        imp = 'burst_imp'

        p = actor.coord.get
        self.level.effects.add_effect(ImpactEffect(p, imp))

        self.stat_component.attack_target(actor.stat_component)
