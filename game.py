import store, character, item


potion = item.item(name='potion', value=10, health_up=5)
super_potion = item.item(name='super_potion', value=20 ,health_up=10)

player_inventory = {potion:2, super_potion:2}
store_inventory = {potion:10, super_potion:10}

player = character.character(name="Bob", max_health=20, inventory=player_inventory,
                            stat_attack=3, stat_defence=1, gold=20)

wraith = character.character(name="Wraith", max_health=10, inventory=player_inventory,
                            stat_attack=2, stat_defence=1, gold=5)

mouse = character.character(name="mouse", max_health=1, inventory=player_inventory,
                            stat_attack=1, stat_defence=0, gold=0)

rat = character.character(name="rat", max_health=3, inventory=player_inventory,
                            stat_attack=1, stat_defence=1, gold=0)

ROUS = character.character(name="ROUS", max_health=5, inventory=player_inventory,
                            stat_attack=2, stat_defence=0, gold=2)

home_store = store.store(name="Ye Tiny Shop Over Yonder", inventory=store_inventory)


def wipe_screen():
    print('\n'*30)

def arena():
    print ('''welcome to the Aren, we have many opponents for you to fight.
who would you like to fight?
    1 - mouse
    2 - Rat
    3 - ROUS
    4 - Wraith''')

    opponent_choice = str(input('please select your opponent: '))

    if (opponent_choice == '1'):
        opponent = mouse
    elif (opponent_choice == '2'):
        opponent = rat
    elif (opponent_choice == '3'):
        opponent = ROUS
    elif (opponent_choice == '4'):
        opponent = wraith

    print(opponent.show_combat_stats())
    print(player.show_combat_stats())

    while player.alive and opponent.alive:
        print('what would you like to do?\n'
              '1 - Attack\n'
              '2 - Use item')

        player_choice = input("Your choice: ")
        if (player_choice == '1'):
            wipe_screen()
            player.combat(opponent)
            if not opponent.alive:
                break
            opponent.combat(player)
            if not player.alive:
                break


while True:
    print('''What would you like to test?
        1 - Enter the Arena
        2 - Show my stats
        3 - Show my gear
        4 - Enter the Store''')

    choice = str(input('Make your selection: '))

    print('You chose ' + choice)

    if (choice == '1'):
        wipe_screen()
        arena()
    elif (choice == '2'):
        wipe_screen()
        print(player.show_combat_stats())
    elif (choice == '3'):
        wipe_screen()
        print(player.show_items())
    elif (choice == '4'):
        wipe_screen()
        home_store.enter(player)
    elif (choice == 'x'):
        exit()