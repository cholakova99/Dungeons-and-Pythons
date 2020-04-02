import unittest
from dungeon import Dungeon

class TestDungeon(unittest.TestCase):
    def test_return_value(self):
        c = "text.txt"
        d = Dungeon(c)
        #answer = d.create_map()
        print(d.lines)
        print(d.possition)


if __name__ == '__main__':
    unittest.main()