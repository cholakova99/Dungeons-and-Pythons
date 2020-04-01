class WithEquipment:
    def __init__ (self, *,name,damage):
        if type(name) is not str:
            raise TypeError('Only strings are allowed for names ')
        if type(damage) is not int or type(damage) is not float:
            raise TypeError('Only integers and floats are allowed for damage')
        self.name = name
        self.damage = damage

    def __eq__(self,other):
        return self.name == other.name and self.damage == other.damage

    def __str__(self):
        return self.__class__.name

    def __repr__(self):
        return self.__class__.name