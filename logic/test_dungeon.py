import unittest
import sys
sys.path.append('.')
from logic import Dungeon
from models import Hero, Enemy


class TestDungeon(unittest.TestCase):
    def test_file(self):
        e = None
        c = "wrong_example_map_for_tests.txt"
        try:
            Dungeon(c)
        except ValueError as error:
            e = error
        self.assertIsNotNone(e)

    def test_spawn_enemy_not_herro(self):
        exp = None
        c = "map_for_tests.txt"
        d = Dungeon(c)
        e = Enemy(health=100, mana=20, damage=10)
        try:
            d.spawn(e)
        except TypeError as error:
            exp = error
        self.assertIsNotNone(exp)

    def test_spawn_with_hero(self):
        c = "map_for_tests.txt"
        d = Dungeon(c)
        h = Hero(name="Pesho", title="The Great One", health=100, mana=10, mana_regeneration_rate=30)
        d.spawn(h)
        answer = d.hero.known_as()
        self.assertEqual("Pesho known as The Great One", answer)

    def test_creation_of_treasure(self):
        c = "text.txt"
        d = Dungeon(c)
        h = Hero(name="Pesho", title="The Great One", health=100, mana=10, mana_regeneration_rate=30)
        d.spawn(h)
        d.create_treasures("treasure.txt")
        self.assertEqual(len(d.treasures), 7)

    # def test_take_treasure(self):
    #     c = "map_for_tests.txt"
    #     d = Dungeon(c)
    #     h = Hero(name="Pesho", title="The Great One", health=50, mana=10, mana_regeneration_rate=30)
    #     d.spawn(h)
    #     d.create_treasures("treasure.txt")
    #     d.hero.take_damage(40)
    #     print("after damage = ", d.hero.curr_health)
    #     d.move_hero("right")
    #     d.move_hero("right")
    #     d.move_hero("down")
    #     d.move_hero("down")
    #     print(d.treasures)
    #     print(d.hero.equiped_spell)
    #     print(d.hero.equiped_weapon)
    #     print(d.hero.curr_health)
    #     print(d.hero.curr_mana)


if __name__ == '__main__':
    unittest.main()
