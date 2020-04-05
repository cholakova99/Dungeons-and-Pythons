from dungeon import Dungeon
from hero import Hero


def get_player_move(dungeon):
    next_move = input()
    while next_move != 'w' and next_move != 'a' and next_move != 's' and next_move != 'd' and next_move != 'j':
        next_move = input()

    if next_move == 'w':
        dungeon.move_hero('up')
    elif next_move == 's':
        dungeon.move_hero('down')
    elif next_move == 'a':
        dungeon.move_hero('left')
    elif next_move == 'd':
        dungeon.next_move('right')
    elif next_move == 'j':
        dungeon.hero_attack()


def play_game():
    hero_name = input('What\'s your name? ')
    hero = Hero(name=hero_name, title='Vagabond', health=100, mana=100, mana_regeneration_rate=2)
    for i in range(1, 4):
        file_name = f'level{i}.txt'
        dungeon = Dungeon(file_name)
        dungeon.spawn(hero)

        while hero.is_alive() and not dungeon.hero_is_at_gateway():
            get_player_move()

        if not hero.is_alive():
            break
        hero.level_up()


def main():
    play_game()


if __name__ == '__main__':
    main()
