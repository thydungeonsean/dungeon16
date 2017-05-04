from random import randint
import weakref


class StatComponent(object):

    attack_v = {
        '-': 15,
        '*': 20,
        '+': 25
    }

    health_v = {
        '-': 35,
        '*': 50,
        '+': 80
    }

    defense_v = {'-': 5,
             '*': 10,
             '+': 15}

    will_v = {'-': 5,
            '*': 10,
            '+': 15}

    evade_v = {'*': 10}

    accuracy_v = {'-': 5,
                '*': 10,
                '+': 15}

    defaults = {
        'base_health': 0,
        'base_attack': 0,
        'health': 1,
        'attack': 1,
        'defense': 0,
        'will': 0,
        'evade': 0,
        'accuracy': 0,
        'attack_value': '*',
        'health_value': '*',
        'defense_value': '-',
        'will_value': '-',
        'evade_value': '*',
        'accuracy_value': '-'
    }

    def __init__(self, owner, **kwargs):

        self.owner = weakref.ref(owner)

        cls = StatComponent
        self.base_health = kwargs.get('base_health', cls.defaults['base_health'])
        self.base_attack = kwargs.get('base_attack', cls.defaults['base_attack'])

        self.health_points = kwargs.get('health', cls.defaults['health'])

        self.attack_points = kwargs.get('attack', cls.defaults['attack'])
        self.defense_points = kwargs.get('defense', cls.defaults['defense'])
        self.will_points = kwargs.get('will', cls.defaults['will'])
        self.evade_points = kwargs.get('evade', cls.defaults['evade'])
        self.accuracy_points = kwargs.get('accuracy', cls.defaults['accuracy'])

        self.health_value = kwargs.get('health_value', cls.defaults['health_value'])
        self.attack_value = kwargs.get('attack_value', cls.defaults['attack_value'])
        self.defense_value = kwargs.get('defense_value', cls.defaults['defense_value'])
        self.will_value = kwargs.get('will_value', cls.defaults['will_value'])
        self.evade_value = kwargs.get('evade_value', cls.defaults['evade_value'])
        self.accuracy_value = kwargs.get('accuracy_value', cls.defaults['accuracy_value'])

        self.current_health = self.max_health

    @property
    def max_health(self):
        return self.base_health + (self.health_points * StatComponent.health_v[self.health_value])

    @property
    def attack(self):
        cls = StatComponent
        return self.base_attack + (self.attack_points * StatComponent.attack_v[self.attack_value])

    @property
    def defense(self):
        return self.defense_points * StatComponent.defense_v[self.defense_value]

    @property
    def will(self):
        return self.will_points * StatComponent.will_v[self.will_value]

    @property
    def evade(self):
        return self.evade_points * StatComponent.evade_v[self.evade_value]

    @property
    def accuracy(self):
        return self.accuracy_points * StatComponent.accuracy_v[self.accuracy_value]

    def attack_target(self, target):

        if target.evade > 0:
            chance, crit = self.get_chance_to_hit(target)
            hit = self.roll_attack(chance)
        else:
            hit = True
            crit = self.accuracy

        if crit > 0:
            critical_hit = self.roll_crit(crit)
        else:
            critical_hit = False

        if critical_hit:
            self.critical_hit_target(target)
        elif hit:
            self.hit_target(target)

    def get_chance_to_hit(self, target):

        mod = target.evade - self.accuracy
        if mod < 0:
            mod = 0
        crit = self.accuracy - target.evade
        if crit < 0:
            crit = 0
        return 100 - mod, crit

    def roll_crit(self, crit):
        return randint(1, 100) < crit

    @staticmethod
    def roll_attack(chance):
        return randint(1, 100) < chance

    def hit_target(self, target):

        damage = self.attack

        for d in range(target.defense):
            if randint(0, 1) == 1:
                damage -= 1

        target.take_damage(damage)

    def critical_hit_target(self, target):

        damage = self.attack * 3

        for d in range(target.defense):
            if randint(0, 2) == 2:
                damage -= 1

        target.take_damage(damage)

    def take_damage(self, damage):

        if damage < 0:
            damage = 0

        self.current_health -= damage

        if self.current_health <= 0:
            self.current_health = 0
            self.die()

    def die(self):
        self.owner().die()

    def heal(self, heal):
        if heal < 0:
            heal = 0
        self.current_health += heal
        if self.current_health > self.max_health:
            self.current_health = self.max_health


def get_monster_stats(actor, sprite):
    return StatComponent(actor)
