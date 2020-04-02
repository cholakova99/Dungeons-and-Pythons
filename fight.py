from hero import Hero
from enemy import Enemy

class Fight:
    def __init__(self,*, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def enemy_turn(self):
        dist = self.check_distance(self.enemy, self.hero)

        if dist != [0, 0]:
            if self.enemy.can_cast():
                self.enemy.curr_mana -= self.enemy.equiped_spell.mana_cost
                self.hero.take_damage(self.enemy.equiped_spell.damage)
                self.print_enemy_attack(by = 'spell')
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
            self.print_enemy_attack(by = 'spell')
        elif max_damage == self.enemy.equiped_weapon.damage:
            self.print_enemy_attack(by = 'weapon')
        else:
            self.print_enemy_attack(by = 'basic')

    def print_enemy_attack(self, *, by):
        if by == 'basic':
            message = f'Enemy hits hero for {self.enemy.damage} dmg.'
        if by == 'weapon':
            message = f'Enemy hits with {self.enemy.equiped_weapon.name} for {self.enemy.equiped_weapon.damage} dmg.'
        if by == 'spell':
            message = f'Enemy casts {self.enemy.equiped_spell.name}, hits enemy for {self.enemy.equiped_spell.damage} dmg.'

        message += f' Hero health is {self.hero.curr_health}.'

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