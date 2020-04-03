from hero import Hero
from enemy import Enemy


class Fight:
    def __init__(self, * , hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def start(self):
        self.print_start_of_fight()
        while self.hero.curr_health > 0 and self.enemy.curr_health > 0:
            self.hero_turn()
            self.enemy_turn()

        self.print_result_of_fight()

    def hero_turn(self):
        dist = self.check_distance(self.hero, self.enemy)

        if dist != [0, 0]:
            if self.hero.can_cast():
                self.hero_cast_spell()
            else:
                self.move_character(self.hero, dist)
                print('Hero doesn\'t have enough mana to cast. Hero moves closer to the enemy')
        else:
            self.hero_attack()

    def hero_attack(self):
        weapon_damage = self.hero.attack(by='weapon')
        spell_damage = self.hero.attack(by='spell')
        if self.hero.can_cast() and spell_damage >= weapon_damage:
            self.hero_cast_spell()
        elif weapon_damage != 0:
            self.enemy.take_damage(weapon_damage)
            self.print_attack(self.hero, self.enemy, by='weapon')
        else:
            self.print_attack(self.hero, self.enemy, by='basic')

    def hero_cast_spell(self):
        self.hero.curr_mana -= self.hero.equiped_spell.curr_mana
        self.enemy.take_damage(self.hero.equiped_spell.damage)
        self.print_attack(self.hero, self.enemy, by='spell')

    def enemy_turn(self):
        dist = self.check_distance(self.enemy, self.hero)

        if dist != [0, 0]:
            if self.enemy.can_cast():
                self.enemy.curr_mana -= self.enemy.equiped_spell.mana_cost
                self.hero.take_damage(self.enemy.equiped_spell.damage)
                self.print_enemy_attack(by='spell')
            else:
                self.move_character(self.enemy, dist)
                print('Enemy can\'t cast a spell. Enemy moves closer to the Hero.')
        else:
            max_damage = self.enemy.attack()
            self.enemy_attack(max_damage)

    def enemy_attack(self, max_damage):
        self.hero.take_damage(max_damage)
        if max_damage == self.enemy.equiped_spell.damage and self.enemy.can_cast():
            self.enemy.curr_mana -= self.enemy.equiped_spell.mana_cost
            self.print_attack(self.enemy, self.hero, by='spell')
        elif max_damage == self.enemy.equiped_weapon.damage:
            self.print_attack(self.enemy, self.hero, by='weapon')
        else:
            self.print_attack(self.enemy, self.hero, by='basic')

    def print_attack(self, character, other, *, by):
        char_class = character.__class__.__name__
        other_class = other.__class__.__name__

        if by == 'weapon':
            message = f'{char_class} hits with {self.hero.equiped_weapon.name} for {self.hero.equiped_weapon.damage} dmg.'
        if by == 'spell':
            message = f'{char_class} casts {self.hero.equiped_spell.name}, hits {other_class.lower()} for {self.hero.equiped_spell.damage} dmg.'
            message += f' {char_class} has {self.hero.curr_mana} mana left.'
        if by == 'basic' and char_class == 'Hero':
            message = 'Hero tries to attack the enemy but fails miserably, dealing 0 dmg to the enemy.'
        else:
            message = f'Enemy hits hero for {self.enemy.damage} dmg.'

        message += f' {other_class} health is {self.enemy.curr_health}'

        print(message)

    def print_start_of_fight(self):
        message = f'A fight is started between our Hero(health={self.hero.curr_health}, mana={self.hero.curr_mana}) '
        message += f'and Enemey(health={self.enemy.curr_health}, mana={self.enemy.curr_mana}, damage={self.enemy.damage})'

        print(message)

    def print_result_of_fight(self):
        if not self.enemy.is_alive():
            message = 'Enemy is dead!'
        else:
            message = 'Hero has died :('
        print(message)

    def check_distance(self, character, other):
        return [
            character.position[0] - other.position[0],
            character.position[1] - other.position[1]
        ]

    def move_character(self, character, distance):
        #have to move down
        if distance[0] > 0:
            character.position[0] -= 1
        #have to move up
        if distance[0] < 0:
            character.position[0] += 1
        #have to move left
        if distance[1] > 0:
            character.position[1] -= 1
        #have to move right
        if distance[1] < 0:
            character.position[1] += 1
