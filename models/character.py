class Character:
    def __init__(self, *, health, mana):
        self.max_health = health
        self.max_mana = mana
        self.curr_health = health
        self.curr_mana = mana
        self.equiped_weapon = None
        self.equiped_spell = None
        self.position = []

    def get_health(self):
        return self.curr_health

    def get_mana(self):
        return self.curr_mana

    def is_alive(self):
        return self.curr_health != 0

    def can_cast(self):
        if self.equiped_spell is not None:
            return self.curr_mana - self.equiped_spell.mana_cost >= 0
        return False

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        self.curr_health += healing_points
        if self.curr_health > self.max_health:
            self.curr_health = self.max_health
        return True

    def take_mana(self, mana_points):
        self.curr_mana += mana_points
        if self.curr_mana > self.max_mana:
            self.curr_mana = self.max_mana

    def take_damage(self, damage):
        self.curr_health -= damage
        if self.curr_health < 0:
            self.curr_health = 0

    def equip(self, weapon):
        self.equiped_weapon = weapon

    def learn(self, spell):
        self.equiped_spell = spell
