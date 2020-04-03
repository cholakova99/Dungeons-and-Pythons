from withequipment import WithEquipment


class Weapon(WithEquipment):
    def __init__(self, *, name, damage):
        super().__init__(name=name, damage=damage)
