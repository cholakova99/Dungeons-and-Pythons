import unittest
from dungeon import Dungeon
from hero import Hero


class TestDungeon(unittest.TestCase):
    def test_return_value(self):
        c = "text.txt"
        d = Dungeon(c)
        h = Hero(name="Pesho", title="The Great One", health=100, mana=10, mana_regeneration_rate=30)
        d.spawn(h)
        d.create_treasures("treasure.txt")
        print(d.hero.known_as())
        print(d.lines)
        print(d.hero_possition)
        d.move_hero("right")
        d.move_hero("down")
        d.move_hero("down")
        d.print_map()


if __name__ == '__main__':
    unittest.main()
