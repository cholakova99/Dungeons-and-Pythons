import unittest
from dungeon import Dungeon
from hero import Hero

class TestDungeon(unittest.TestCase):
    def test_return_value(self):
        c = "text.txt"
        d = Dungeon(c)
        h = Hero(name="Pesho",title="The Great One",health=100,mana=10,mana_regeneration_rate=30)
        d.spawn(h)
        print(d.lines)
        print(d.hero_possition)


if __name__ == '__main__':
    unittest.main()