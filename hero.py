from character import Character
class Hero(Character):
    def __init__(self, *, name, title, health,mana,mana_regeneration_rate):
        if type(name) is not str or type(title) is not str:
            raise TypeError('Only strings are allowed for name and title!')
        if type(health) is not int or type(mana) is not int or type(mana_regeneration_rate) is not int:
            raise TypeError('Only integers are allowed for health, mana and rate while creating hero')
        super().__init__(health=health,mana=mana)
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate

    def __eq__(self,other):
        return self.name == other.name

    def known_as(self):
        return f'{self.name} known as {self.title}'

    def attack(self, *, by):
        if by == 'weapon':
            if self.equiped_weapon != None:
                return self.equiped_weapon.damage
        if by == 'spell':
            if super.can_cast():
                return self.equiped_spell.damage
        return 0

    # def increase_mana(self,to_be_added_to_mana):
    #     super().mana += to_be_added_to_mana

    # def increase_health(self,to_be_added_to_health):
    #     self.health += to_be_added_to_health