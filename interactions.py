import backpack
import time


def take_quest(y, x, board, player_stats):
    interactions = ['?', '(', 'A', '|', '-']

    if board[y][x+1] in interactions or board[y][x-1] in interactions:
        interaction = (board[y+1][x], board[y-1][x])
        check_encounter(player_stats, interaction)

    elif board[y+1][x] in interactions or board[y-1][x] in interactions:
        interaction = (board[y+1][x], board[y-1][x])
        check_encounter(player_stats, interaction)

    return player_stats


def check_encounter(player_stats, interaction):
    if interaction[0] == '?' or interaction[1] == '?':
        quest_1(player_stats)

    elif interaction[0] == '|' or interaction[1] == '|':
        reapair_lab()

    return player_stats


def quest_1(player_stats):
    inventory = {}
    print('PABLO: Hola José Rodríguez Gacha!')
    print('GACHA: Welcome Pablo!\nIf you want take a lost part for yor lab, you can buy it here. Its cost 800 $!')

    while True:
        answer = input('Do you want to buy it Pablo?\n')

        if answer == 'yes':
            player_stats[3] -= 800
            inventory['lab_part'] = (0, 100, 'quest_item')
            backpack.add_item_to_backpack_file(inventory)
            break

        elif answer == 'no':
            break

    return player_stats


def reapair_lab():
    inventory = backpack.open_backpack_file()
    print(inventory)

    if 'lab_part' in inventory:
        print('PABLO: Finally my laboratorium is work fine!\n Now you can make COCAINE! Lets get to work amigos!!!')
        del inventory['lab_part']

        time.sleep(2)
        print('YOU EARN 20KG COCAINE!')

        inventory['COCAINE'] = (0, 20, 'drugs')
        print(inventory)
        backpack.save_backpack_to_file(inventory)

    elif 'lab_part' not in inventory:
        print('PABLO: My laboratorium is broken i need to find lab part to fix it!')
