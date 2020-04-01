from character import Character

class Enemy(Character):
	def __init__(self, * health, mana, damage):
		super().__init__(health = health, mana = mana)
		self.damage = damage

	def attack(self):
		pass