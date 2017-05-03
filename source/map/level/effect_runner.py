

class EffectRunner(object):

    def __init__(self, level):

        self.level = level

        self.effects = []

    def add_effect(self, effect):

        effect.set_level(self.level)
        effect.set_runner(self)

        self.effects.append(effect)

    def remove_effect(self, effect):

        self.effects.remove(effect)

    def run(self):

        for effect in self.effects:
            effect.run()
