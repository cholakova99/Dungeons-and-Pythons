from withequipment import Withequipment
class Weapon(Withequipment):
    def __init__(self,*,name,damage):
        super.__init__(name,damage)
