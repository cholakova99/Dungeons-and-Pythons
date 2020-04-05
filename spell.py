from withequipment import WithEquipment


class Spell(WithEquipment):
    def __init__(self, *, name, damage, mana_cost, cast_range):
        if type(damage) is not int or type(mana_cost) is not int or type(cast_range) is not int:
            raise TypeError('Only integers are allowed for damage,mana and cast!')
        super().__init__(name=name, damage=damage)
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    def __eq__(self, other):
        return super().__eq__(other)

    def __str__(self):
        return f'{self.name}: damage-{self.damage}, cost-{self.mana_cost}, range-{self.cast_range}'