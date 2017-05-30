from actor import Actor
from stat_component import get_monster_stats
from source.objects.effects.impact_effect import ImpactEffect
from source.states.message_system.message import Message


class Monster(Actor):

    count = 0

    def __init__(self, point, sprite):

        Actor.__init__(self, point, sprite)
        self.stat_component = get_monster_stats(self, sprite)
        Monster.count += 1

    def set_profile(self):
        return {'allegiance': 'foe', 'group': 'monster', 'id': self.sprite+str(Monster.count)}

    def report_move(self):
        Message('actor_move', *self.profile.items()).send()

    def hit_actor(self, actor):

        imp = 'l_slash_imp'

        p = actor.coord.get
        self.level.effects.add_effect(ImpactEffect(p, imp))

        self.stat_component.attack_target(actor.stat_component)
