from withequipment import Withequipment
class Spell(withequipment):
    def __init__(self, *, name,damage,mana_cost,cast_range):
        if type(damage) is not int or type(mana_cost) is not int or type(cast_range) is not int:
            raise TypeError('Only integers are allowed for damage,mana and cast!')
        super.__init__(name,damage)
        self.mana_cost = mana_cost
        self.cast_range = cast_range
