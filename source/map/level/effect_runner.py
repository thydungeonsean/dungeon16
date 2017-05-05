

class EffectRunner(object):

    def __init__(self, level):

        self.level = level

        self.effects = []
        self.drawable_effects = []

    def set_drawable_effects(self):
        self.drawable_effects = list(filter(lambda x: x.drawable, self.effects))

    def add_effect(self, effect):

        effect.set_level(self.level)
        effect.set_runner(self)

        self.effects.append(effect)
        if effect.drawable:
            self.drawable_effects.append(effect)

    def remove_effect(self, effect):

        self.effects.remove(effect)
        if effect.drawable:
            self.drawable_effects.remove(effect)

    def run(self):

        for effect in self.effects:
            effect.run()
