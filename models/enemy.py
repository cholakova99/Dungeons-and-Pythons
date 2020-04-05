from models import Character


class Enemy(Character):
    def __init__(self, *, health, mana, damage):
        super().__init__(health=health, mana=mana)
        self.damage = damage

    def attack(self, *, by):
        if by == 'weapon':
            if self.equiped_weapon is not None:
                return self.equiped_weapon.damage
        if by == 'spell':
            if super.can_cast():
                return self.equiped_spell.damage
        return self.damage
