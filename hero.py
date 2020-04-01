from character import Character
class Hero(Character):
    def __init__(self, *, name, title, health,mana,mana_regeneration_rate):
        if type(name) is not str or type(title) is not str:
            raise TypeError('Only strings are allowed for name and title!')
        if type(health) is not int or type(mana) is not int or type(mana_regeneration_rate) is not int:
            raise TypeError('Only integers are allowed for health, mana and rate while creating hero')
        super.__init__(health,mana)
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate

    def __eq__(self,other):
        return self.name == other.name

    def known_as(self):
        return f'{self.name} known as {self.title}'

    def equip(self, weapon):
        if super().equiped_weapon is None and type(weapon) is Weapon:
            self.equiped_weapon = weapon
        elif super().equiped_spell is None and type(weapon) is Spell:
            self.equiped_spell = weapon
        else:
            return

    def learn(self,spell):
        if type(spell) != Spell:
            raise TypeError('You can only learn spells')
        if self.equiped_spell != None:
            ###### check if we will compare spells
            self.equiped_spell = None
        self.equiped_spell = spell

