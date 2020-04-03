from dungeon import Dungeon
from hero import Hero


def play_game():
    end = False
    name_of_the_file = input("Please, insert file name:")
    game_map = Dungeon(name_of_the_file)
    print("Let's create a hero")
    hero_name = input("Input hero name:")
    hero_title = input("Input hero title")
    hero_health = input("Input hero health")
    hero_mana = input("Input hero mana")
    hero_mana_reg = input("Input hero mana regeneration rate")
    hero = Hero(name=hero_name, title=hero_title, health=hero_health,
                mana=hero_mana, mana_regeneration_rate=hero_mana_reg)
    game_map.spawn(hero)
    instructions = "For moving up - press u \
        for moving down - press d \
        for moving left - press l \
        for moving right - press r"
    print(instructions)
    while end is False:
        movement = input("Move:")
        game_map.move_hero(movement)

def main():
    play_game()



if __name__ == '__main__':
    main()
