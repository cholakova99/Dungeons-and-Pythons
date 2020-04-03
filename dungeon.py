from random import randint
from hero import Hero
from spell import Spell
from weapon import Weapon
allowed_symbols_for_map = ["#", "S", "T", "E", ".", "G"]


class Dungeon:
    def __init__(self, given_file):
        if type(given_file) is not str:
            raise ValueError('Wrong imput for file')
        self.given_file = given_file
        self.hero_possition = []
        self.treasures = []
        self.lines = self.create_map()
        # self.change_start_possition()
        self.rows = len(self.lines)
        self.columns = len(self.lines[0])
        self.hero = None

    def spawn(self, to_be_hero):
        if type(to_be_hero) != Hero:
            raise ValueError('Only hero allowed!')
        self.hero = to_be_hero
        self.hero.possition = self.hero_possition

    def change_possition_value(self, row_index, col_index, strng):
        self.lines[row_index] = self.lines[row_index][:col_index] + \
            strng + self.lines[row_index][col_index + 1:]

    def create_map(self):
        with open(self.given_file, 'r') as file:
            to_be_lines = file.readlines()
        for i in range(0, len(to_be_lines)):
            to_be_lines[i] = to_be_lines[i][:-1]
        if self.correct_form(to_be_lines) is False:
            raise ValueError('Text format cannot be parsed to map')
        return to_be_lines

    def correct_form(self, to_be_lines):
        first_met = False
        first_line_len = len(to_be_lines[0])
        for i in range(0, len(to_be_lines) - 1):
            if len(to_be_lines[i]) != first_line_len:
                return False
            for j in range(first_line_len):
                if to_be_lines[i][j] not in allowed_symbols_for_map:
                    return False
                if to_be_lines[i][j] == "S" and first_met is False:
                    first_met = True
                    self.hero_possition.append(i)
                    self.hero_possition.append(j)

        return True

    def print_map(self):
        for i in range(len(self.lines)):
            if i == self.hero_possition[0]:
                helper = ""
                for j in range(0, len(self.lines[i])):
                    if j == self.hero_possition[1]:
                        helper += "H"
                    else:
                        helper += self.lines[i][j]
        for i in range(0, len(self.lines)):
            if i == self.hero_possition[0]:
                print(helper)
            else:
                print(self.lines[i])

    def move_hero(self, direction):
        if direction == "up":
            if self.hero_possition[0] <= 0:
                return False
            helper = self.check_next_step(self.hero_possition[0] - 1, self.hero_possition[1])
            if helper == "path":
                self.change_possition_value(self.hero_possition[0], self.hero_possition[1], ".")
                self.hero_possition[0] -= 1
            elif helper == "enemy":
                self.change_possition_value(self.hero_possition[0], self.hero_possition[1], ".")
                self.hero_possition[0] -= 1
            elif helper == "gateway":
                pass
            elif helper == "treasure":
                self.change_possition_value(self.hero_possition[0], self.hero_possition[1], ".")
                self.hero_possition[0] -= 1
                self.take_treasure()
            else:
                return False

        elif direction == "down":
            if self.hero_possition[0] >= self.rows - 1:
                return False
            helper = self.check_next_step(self.hero_possition[0] + 1, self.hero_possition[1])
            if helper == "path":
                self.change_possition_value(self.hero_possition[0], self.hero_possition[1], ".")
                self.hero_possition[0] += 1
            elif helper == "enemy":
                self.change_possition_value(self.hero_possition[0], self.hero_possition[1], ".")
                self.hero_possition[0] += 1
            elif helper == "gateway":
                pass
            elif helper == "treasure":
                self.change_possition_value(self.hero_possition[0], self.hero_possition[1], ".")
                self.hero_possition[0] += 1
                self.take_treasure()
            else:
                return False

        elif direction == "left":
            if self.hero_possition[1] <= 0:
                return False
            helper = self.check_next_step(self.hero_possition[0], self.hero_possition[1] - 1)
            if helper == "path":
                self.change_possition_value(self.hero_possition[0], self.hero_possition[1], ".")
                self.hero_possition[1] -= 1
            elif helper == "enemy":
                self.change_possition_value(self.hero_possition[0], self.hero_possition[1], ".")
                self.hero_possition[1] -= 1
            elif helper == "gateway":
                pass
            elif helper == "treasure":
                self.change_possition_value(self.hero_possition[0], self.hero_possition[1], ".")
                self.hero_possition[1] -= 1
                self.take_treasure()
            else:
                return False

        elif direction == "right":
            if self.hero_possition[1] >= self.columns - 1:
                return False
            helper = self.check_next_step(self.hero_possition[0], self.hero_possition[1] + 1)
            if helper == "path":
                self.change_possition_value(self.hero_possition[0], self.hero_possition[1], ".")
                self.hero_possition[1] += 1
            elif helper == "enemy":
                self.change_possition_value(self.hero_possition[0], self.hero_possition[1], ".")
                self.hero_possition[1] += 1
            elif helper == "gateway":
                pass
            elif helper == "treasure":
                self.change_possition_value(self.hero_possition[0], self.hero_possition[1], ".")
                self.hero_possition[1] += 1
                self.take_treasure()
            else:
                return False
        else:
            return "Wrong direction"

    def check_next_step(self, row_index, col_index):
        if self.lines[row_index][col_index] == "G":
            return "gateway"
        elif self.lines[row_index][col_index] == "E":
            return "enemy"
        elif self.lines[row_index][col_index] == "#":
            return "obstacle"
        elif self.lines[row_index][col_index] == ".":
            return "path"
        elif self.lines[row_index][col_index] == "T":
            return "treasure"
        else:
            return "starting"

# WITH FILE
    def create_treasures(self, file_treasures):
        with open(file_treasures, 'r') as file_treasures:
            self.treasures = file_treasures.readlines()
        for i in range(len(self.treasures)):
            self.treasures[i] = self.treasures[i][:-1]
            self.treasures[i] = self.treasures[i].split("-")
            if len(self.treasures[i]) == 2:
                self.treasures[i][1] = int(self.treasures[i][1])
            if len(self.treasures[i]) > 2:
                for j in range(2, len(self.treasures[i])):
                    self.treasures[i][j] = int(self.treasures[i][j])

    def take_treasure(self):
        num = randint(0, len(self.treasures) - 1)
        if self.treasures[num][0] == "mana":
            self.hero.take_mana(self.treasures[num][1])
        if self.treasures[num][0] == "health":
            self.hero.take_healing(self.treasures[num][1])
        if self.treasures[num][0] == "weapon":
            w = Weapon(name=self.treasures[num][1], damage=self.treasures[num][2])
            self.hero.equip(w)
        if self.treasures[num][0] == "spell":
            s = Spell(name=self.treasures[num][1], damage=self.treasures[num][2],
                      mana_cost=self.treasures[num][3], cast_range=self.treasures[num][4])
            self.hero.learn(s)
