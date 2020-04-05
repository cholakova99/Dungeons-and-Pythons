class Fight:
    def __init__(self, *, hero, enemy):
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
                command = self.get_cast_or_move()
                if command == 'c':
                    self.hero_cast_spell()
                else:
                    self.move_character(self.hero, self.enemy, dist)
            else:
                print('The Hero can\'t cast a spell.')
                self.move_character(self.hero, self.enemy, dist)
        else:
            weapon_damage = self.hero.attack(by='weapon')
            spell_damage = self.hero.attack(by='spell')
            if weapon_damage != 0 and spell_damage != 0:
                command = self.get_cast_or_melee()
                if command == 'c':
                    self.hero_cast_spell()
                else:
                    self.hero_weapon_attack()
            elif weapon_damage != 0:
                print('Hero can\'t cast his spell.')
                self.hero_weapon_attack()
            elif spell_damage != 0:
                self.hero_cast_spell()
            else:
                self.print_action(self.hero, self.enemy, act='basic')

    def get_cast_or_move(self):
        print(f'You have enough mana to cast {self.hero.equiped_spell.name}')
        command = input('To cast the spell: Press c\n To move: Press m')
        while command != 'c' and command != 'm':
            command = input()
        return command

    def get_cast_or_melee(self):
        print(f'You have enough mana to cast {self.hero.equiped_spell.name}')
        command = input('To cast the spell: Press c\n To attack with weapon: Press a')
        while command != 'c' and command != 'a':
            command = input()
        return command

    def hero_weapon_attack(self):
        self.enemy.take_damage(self.hero.equiped_weapon.damage)
        self.print_action(self.hero, self.enemy, act='weapon')

    def hero_cast_spell(self):
        self.hero.curr_mana -= self.hero.equiped_spell.curr_mana
        self.enemy.take_damage(self.hero.equiped_spell.damage)
        self.print_action(self.hero, self.enemy, act='spell')

    def enemy_turn(self):
        dist = self.check_distance(self.enemy, self.hero)

        if dist != [0, 0]:
            if self.enemy.can_cast() and self.in_cast_range(dist, self.enemy):
                self.enemy_cast_spell()
            else:
                self.move_character(self.enemy, self.hero, dist)
        else:
            spell_damage = 0
            weapon_damage = self.enemy.attack(by='weapon')
            if self.in_cast_range(dist, self.enemy):
                spell_damage = self.enemy.attack(by='spell')
            max_damage = max(spell_damage, weapon_damage, self.enemy.damage)

            if max_damage == self.enemy.damage:
                self.enemy_basic_attack()
            elif max_damage == self.spell_damage:
                self.enemy_cast_spell()
            else:
                self.enemy_weapon_attack()

    def enemy_cast_spell(self):
        self.enemy.curr_mana -= self.enemy.equiped_spell.mana_cost
        self.hero.take_damage(self.enemy.equiped_spell.damage)
        self.print_action(self.enemy, self.hero, act='spell')

    def enemy_weapon_attack(self):
        self.hero.take_damage(self.enemy.equiped_weapon.damage)
        self.print_action(self.enemy, self.hero, act='weapon')

    def enemy_basic_attack(self):
        self.hero.take_damage(self.enemy.damage)
        self.print_action(self.enemy, self.hero, act='basic')

    def print_action(self, character, other, *, act):
        char_class = character.__class__.__name__
        other_class = other.__class__.__name__

        if act == 'move':
            message = f'{char_class} moves 1 step closer to the {other_class}.'
        else:
            if act == 'weapon':
                message = f'{char_class} hits with {self.hero.equiped_weapon.name}' +\
                    f' for {self.hero.equiped_weapon.damage} dmg.'
            if act == 'spell':
                message = f'{char_class} casts {self.hero.equiped_spell.name},' +\
                    f' hits {other_class.lower()} for {self.hero.equiped_spell.damage} dmg.' +\
                    f' {char_class} has {self.hero.curr_mana} mana left.'
            if act == 'basic':
                if char_class == 'Hero':
                    message = 'Hero tries to attack the enemy but fails miserably, dealing 0 dmg to the enemy.'
                else:
                    message = f'Enemy hits hero for {self.enemy.damage} dmg.'
            message += f' {other_class} health is {self.enemy.curr_health}'

        print(message)

    def print_start_of_fight(self):
        message = f'A fight is started between our Hero(health={self.hero.curr_health}, mana={self.hero.curr_mana}) ' +\
            f'and Enemey(health={self.enemy.curr_health}, ' +\
            f'mana={self.enemy.curr_mana}, damage={self.enemy.damage})'

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

    def in_cast_range(self, dist, character):
        return (dist[0] == 0 and abs(dist[1]) < character.equiped_spell.cast_range)\
            or (dist[1] == 0 and abs(dist[0]) < character.equiped_spell.cast_range)

    def move_character(self, character, other, distance):
        # have to move down
        if distance[0] > 0:
            character.position[0] -= 1
        # have to move up
        if distance[0] < 0:
            character.position[0] += 1
        # have to move left
        if distance[1] > 0:
            character.position[1] -= 1
        # have to move right
        if distance[1] < 0:
            character.position[1] += 1
        self.print_action(character, other, act='move')
