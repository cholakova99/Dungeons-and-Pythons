import unittest

import sys
sys.path.append('.')

from logic import Dungeon
from models import Hero, Enemy



class TestDungeon(unittest.TestCase):
    def test_file(self):
        e = None
        c = "levels_and_treasures/map_for_tests2.txt"
        try:
            Dungeon(c)
        except ValueError as error:
            e = error
        self.assertIsNotNone(e)
        
    def test_spawn_enemy_not_herro(self):
        exp = None
        c = "levels_and_treasures/level1.txt"
        d = Dungeon(c)
        e = Enemy(health=100, mana=20, damage=10)
        try:
            d.spawn(e)
        except TypeError as error:
            exp = error
        self.assertIsNotNone(exp)

    def test_spawn_with_hero(self):
        c = "levels_and_treasures/level1.txt"
        d = Dungeon(c)
        h = Hero(name="Pesho", title="The Great One", health=100, mana=10, mana_regeneration_rate=30)
        d.spawn(h)
        answer = d.hero.known_as()
        self.assertEqual("Pesho known as The Great One", answer)

    def test_creation_of_treasure(self):
        c = "levels_and_treasures/level1.txt"
        d = Dungeon(c)
        h = Hero(name="Pesho", title="The Great One", health=100, mana=10, mana_regeneration_rate=30)
        d.spawn(h)
        d.create_treasures("levels_and_treasures/treasures.txt")
        self.assertEqual(len(d.treasures), 9)


if __name__ == '__main__':
    unittest.main()
