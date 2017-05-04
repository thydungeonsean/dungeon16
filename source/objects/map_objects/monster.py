from actor import Actor
from stat_component import get_monster_stats
from source.objects.effects.impact_effect import ImpactEffect


class Monster(Actor):

    def __init__(self, point, sprite):

        Actor.__init__(self, point, sprite)
        self.stat_component = get_monster_stats(self, sprite)

    def hit_actor(self, actor):

        imp = 'blunt_a_imp'

        p = actor.coord.get
        self.level.effects.add_effect(ImpactEffect(p, imp))

        self.stat_component.attack_target(actor.stat_component)
