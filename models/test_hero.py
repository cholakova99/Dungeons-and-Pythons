import unittest
import sys
sys.path.append('.')
from models import Hero, Weapon, Spell


class TestHero(unittest.TestCase):
    def test_known_as(self):
        h = Hero(name="Pesho", title="The Great One", health=100, mana=10, mana_regeneration_rate=30)
        answer = h.known_as()
        self.assertEqual("Pesho known as The Great One", answer)

    def test_take_damage(self):
        h = Hero(name="Pesho", title="The Great One", health=100, mana=10, mana_regeneration_rate=30)
        h.take_damage(20)
        self.assertEqual(80, h.curr_health)

    def test_take_healing(self):
        h = Hero(name="Pesho", title="The Great One", health=100, mana=10, mana_regeneration_rate=30)
        h.take_damage(70)
        h.take_healing(30)
        self.assertEqual(60, h.curr_health)

    def test_is_alive(self):
        h = Hero(name="Pesho", title="The Great One", health=100, mana=10, mana_regeneration_rate=30)
        h.take_damage(120)
        self.assertEqual(False, h.is_alive())

    def test_equip(self):
        h = Hero(name="Pesho", title="The Great One", health=100, mana=10, mana_regeneration_rate=30)
        w = Weapon(name="GUN", damage=35)
        h.equip(w)
        self.assertEqual(h.equiped_weapon.name, "GUN")

    def test_learn(self):
        h = Hero(name="Pesho", title="The Great One", health=100, mana=10, mana_regeneration_rate=30)
        s = Spell(name="Abrakadabra", damage=50, mana_cost=20, cast_range=4)
        h.learn(s)
        self.assertEqual(h.equiped_spell.name, "Abrakadabra")

    def test_take_mana(self):
        h = Hero(name="Pesho", title="The Great One", health=100, mana=10, mana_regeneration_rate=30)
        h.curr_mana = 0
        h.take_mana(5)
        self.assertEqual(h.curr_mana, 5)

    def test_cannot_cast(self):
        h = Hero(name="Pesho", title="The Great One", health=100, mana=10, mana_regeneration_rate=30)
        s = Spell(name="Abrakadabra", damage=50, mana_cost=20, cast_range=4)
        h.learn(s)
        self.assertEqual(False, h.can_cast())

    def test_can_cast(self):
        h = Hero(name="Pesho", title="The Great One", health=100, mana=10, mana_regeneration_rate=30)
        s = Spell(name="Abrakadabra", damage=50, mana_cost=2, cast_range=4)
        h.learn(s)
        self.assertEqual(True, h.can_cast())


if __name__ == '__main__':
    unittest.main()
