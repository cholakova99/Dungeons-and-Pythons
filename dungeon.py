from random import randint
from hero import Hero
from enemy import Enemy
from spell import Spell
from weapon import Weapon
from fight import Fight
allowed_symbols_for_map = ["#", "S", "T", "E", ".", "G"]


class Dungeon:
    def __init__(self, given_file):
        if type(given_file) is not str:
            raise ValueError('Wrong imput for file')
        self.given_file = given_file
        self.treasures = []
        self.enemies = []
        self.lines = self.create_map()
        self.rows = len(self.lines)
        self.columns = len(self.lines[0])
        self.hero = None

    def hero_is_at_gateway(self):
        return self.lines[self.hero.position[0]][self.hero.position[1]] == "G"

    def find_spawn_point(self):
        for i in range(len(self.lines)):
            for j in range(len(self.lines[i])):
                if self.lines[i][j] == 'S':
                    return [i, j]

    def spawn(self, to_be_hero):
        if type(to_be_hero) is not Hero:
            raise TypeError('Only hero allowed!')
        self.hero = to_be_hero
        self.hero.position = self.find_spawn_point()
        self.create_enemies()

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
        first_line_len = len(to_be_lines[0])
        for i in range(0, len(to_be_lines) - 1):
            if len(to_be_lines[i]) != first_line_len:
                return False
            for j in range(first_line_len):
                if to_be_lines[i][j] not in allowed_symbols_for_map:
                    return False
        return True

    def print_map(self):
        for line in self.lines:
            print(line)

    def make_move_changes(self, helper):
        if helper == 'enemy':
                for enemy in self.enemies:
                    if enemy.position == self.hero.position:
                        fight = Fight(hero=self.hero, enemy=enemy)
                        fight.start()
        if helper == 'treasure':
            self.take_treasure()
        if not helper == 'gateway' and self.hero.is_alive():
            self.change_possition_value(self.hero.position[0], self.hero.position[1], "H")
        self.hero.take_mana(self.hero.mana_regeneration_rate)

    def move_hero(self, direction):
        if direction == "up":
            if self.hero.position[0] <= 0:
                return False
            helper = self.check_next_step(self.hero.position[0] - 1, self.hero.position[1])
            if helper == 'obstacle':
                return False
            self.change_possition_value(self.hero.position[0], self.hero.position[1], ".")
            self.hero.position[0] -= 1
            self.make_move_changes(helper)

        elif direction == "down":
            if self.hero.position[0] >= self.rows - 1:
                return False
            helper = self.check_next_step(self.hero.position[0] + 1, self.hero.position[1])
            if helper == 'obstacle':
                return False
            self.change_possition_value(self.hero.position[0], self.hero.position[1], ".")
            self.hero.position[0] += 1
            self.make_move_changes(helper)

        elif direction == "left":
            if self.hero.position[1] <= 0:
                return False
            helper = self.check_next_step(self.hero.position[0], self.hero.position[1] - 1)
            if helper == 'obstacle':
                return False
            self.change_possition_value(self.hero.position[0], self.hero.position[1], ".")
            self.hero.position[1] -= 1
            self.make_move_changes(helper)

        elif direction == "right":
            if self.hero.position[1] >= self.columns - 1:
                return False
            helper = self.check_next_step(self.hero.position[0], self.hero.position[1] + 1)
            if helper == 'obstacle':
                return False
            self.change_possition_value(self.hero.position[0], self.hero.position[1], ".")
            self.hero.position[1] += 1
            self.make_move_changes(helper)
        return True

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

    def create_enemies(self):
        for i in range(len(self.lines)):
            for j in range(len(self.lines[i])):
                if self.lines[i][j] == 'E':
                    hero_hp = self.hero.max_health
                    hero_mana = self.hero.max_mana
                    # hero_dmg = max(self.hero.attack(by='weapon'), self.hero.attack(by='spell'))
                    enemy_hp = randint(hero_hp * 0.75, hero_hp * 1.25)
                    enemy_mana = randint(hero_mana * 0.5, hero_mana * 2)
                    enemy_dmg = 10  # randint(hero_dmg - (hero_dmg % 10), hero_dmg + (hero_dmg % 10))
                    enemy = Enemy(health=enemy_hp, mana=enemy_mana, damage=enemy_dmg)
                    enemy.position = [i, j]
                    # Here we can add a chance to equip weapon or learn a spell
                    self.enemies.append(enemy)

    def check_for_enemies_in_range(self):
        spell_range = self.hero.equiped_spell.cast_range
        row, col = self.hero.position
        # Look up
        for i in range(spell_range):
            if row - i >= 0:
                if self.lines[row - i][col] == 'E':
                    for enemy in self.enemies:
                        if enemy.position == [row - i, col]:
                            return enemy
                if self.lines[row - i][col] != '.':
                    break
        # Look down
        for i in range(spell_range):
            if row + i < self.rows:
                if self.lines[row + i][col] == 'E':
                    for enemy in self.enemies:
                        if enemy.position == [row + i, col]:
                            return enemy
                if self.lines[row + i][col] != '.':
                    break
        # Look left
        for i in range(spell_range):
            if col - i >= 0:
                if self.lines[row][col - i] == 'E':
                    for enemy in self.enemies:
                        if enemy.position == [row, col - i]:
                            return enemy
                if self.lines[row][col - i] != '.':
                    break
        for i in range(spell_range):
            if col + i < self.columns:
                if self.lines[row][col + i] == 'E':
                    for enemy in self.enemies:
                        if enemy.position == [row, col + i]:
                            return enemy
                if self.lines[row][col + i] != '.':
                    break

    def hero_attack(self):
        if self.hero.can_cast():
            enemy = self.check_for_enemies_in_range()
            if enemy is not None:
                self.change_possition_value(self.hero.position[0], self.hero.position[1], ".")
                pre_fight_enemy_pos = enemy.position

                fight = Fight(self.hero, enemy)
                fight.start()

                if not enemy.is_alive():
                    self.change_possition_value(pre_fight_enemy_pos[0], pre_fight_enemy_pos[1], ".")
                if self.hero.is_alive():
                    self.change_possition_value(self.hero.position[0], self.hero.position[1], "H")
                return True
            else:
                print(f'Nothing in cast range {self.hero.equiped_spell.cast_range}.')
        else:
            print('You can\'t cast a spell.')
        return False

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
            print(f'Found mana potion: {self.treasures[num][1]}')
            print(f'Hero current mana: {self.hero.curr_mana}')
        if self.treasures[num][0] == "health":
            self.hero.take_healing(self.treasures[num][1])
            print(f'Found health potion: {self.treasures[num][1]}')
            print(f'Hero current health: {self.hero.curr_health}')
        if self.treasures[num][0] == "weapon":
            w = Weapon(name=self.treasures[num][1], damage=self.treasures[num][2])
            if self.hero.equiped_weapon is not None:
                print(f'Equiped: {str(self.hero.equiped_weapon)}')
                print(f'Offered: {str(w)}')
                answer = input('Would you like to change weapon? ')
                if answer == 'y':
                    self.hero.equip(w)
            else:
                self.hero.equip(w)
        if self.treasures[num][0] == "spell":
            s = Spell(name=self.treasures[num][1], damage=self.treasures[num][2],
                      mana_cost=self.treasures[num][3], cast_range=self.treasures[num][4])
            if self.hero.equiped_spell is not None:
                print(f'Learned: {str(self.hero.equiped_spell)}')
                print(f'Offered: {str(s)}')
                answer = input('Would you like to learn the new spell? ')
                if answer == 'y':
                    self.hero.learn(s)
            else:
                self.hero.learn(s)
