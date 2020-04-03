from character import Character


class Enemy(Character):
    def __init__(self, * health, mana, damage):
        super().__init__(health=health, mana=mana)
        self.damage = damage

    def attack(self):
        spell_damage = 0
        weapon_damage = 0
        if self.can_cast():
            spell_damage = self.equiped_spell.damage
        if self.equiped_weapon is not None:
            weapon_damage = self.equiped_weapon.damage
        max_damage = max(spell_damage, weapon_damage, self.damage)

        return max_damage
