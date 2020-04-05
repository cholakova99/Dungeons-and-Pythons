from dungeon import Dungeon
from hero import Hero
from weapon import Weapon

def get_player_move(dungeon):
    next_move = input()
    while next_move != 'w' and next_move != 'a' and next_move != 's' and next_move != 'd' and next_move != 'j':
        next_move = input()

    if next_move == 'w':
        return dungeon.move_hero('up')
    elif next_move == 's':
        return dungeon.move_hero('down')
    elif next_move == 'a':
        return dungeon.move_hero('left')
    elif next_move == 'd':
        return dungeon.move_hero('right')
    elif next_move == 'j':
        return dungeon.hero_attack()


def ask_to_continue():
    answer = input('Would you like to continue to the next level? ')
    if answer == 'y':
        return True
    elif answer == 'n':
        return False


def play_game():
    hero_name = input('What\'s your name? ')
    hero = Hero(name=hero_name, title='Vagabond', health=100, mana=100, mana_regeneration_rate=2)
    weapon = Weapon(name='Black cleaver', damage=50)
    hero.equip(weapon)

    for i in range(1, 3):
        file_name = f'level{i}.txt'
        dungeon = Dungeon(file_name)
        dungeon.create_treasures('treasures.txt')
        dungeon.spawn(hero)

        print(f'{hero.known_as()} entered dungeon {i}')

        dungeon.print_map()
        while hero.is_alive() and not dungeon.hero_is_at_gateway():
            if get_player_move(dungeon):
                dungeon.print_map()

        if not hero.is_alive():
            print('GAME OVER')
            break
        hero.level_up()

        if i != 2 and not ask_to_continue():
            break


def main():
    play_game()


if __name__ == '__main__':
    main()
