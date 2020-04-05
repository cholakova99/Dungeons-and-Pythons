from models import WithEquipment


class Weapon(WithEquipment):
    def __init__(self, *, name, damage):
        super().__init__(name=name, damage=damage)

    def __eq__(self, other):
        return super().__eq__(other)

    def __str__(self):
        return f'{self.name} with {self.damage} damage'
