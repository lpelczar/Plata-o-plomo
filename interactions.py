import backpack
import tnt
import time
import random
import boss
import sys
import load_map


def take_quest(y, x, board, player_stats):
    """Check if player is near any available quest and take it
    Args:
        y, x: current coordinates of the player
        board: list of list representing our map
        player_stats: list of user statistics
    Returns:
        position, player_stats
    """
    interactions = ['?', '|', 'E', '$', ')', 'I']

    if board[y][x+1] in interactions or board[y][x-1] in interactions:
        interaction = (board[y][x+1], board[y][x-1])
        player_stats, interaction = check_encounter(player_stats, interaction)
        board[y][x+1] = interaction[0]
        board[y][x-1] = interaction[1]

    elif board[y+1][x] in interactions or board[y-1][x] in interactions:
        interaction = (board[y+1][x], board[y-1][x])
        player_stats, interaction = check_encounter(player_stats, interaction)
        board[y+1][x] = interaction[0]
        board[y-1][x] = interaction[1]

    elif board[y][x+1] == '(':
        tnt.ask_explode_intent(y, x, board, player_stats)

    elif board[y][x+1] == '<':
        tnt.ask_explode_intent(y, x, board, player_stats)

    elif board[y-1][x] == '=':
        guns_shop(player_stats)

    elif board[y][x+1] == 'l':
        if player_stats[4] >= 4:
            boss.start_fight()
        else:
            print('You need to kill 4 enemies to start fight with boss!')

    position = (y, x, board)

    return position, player_stats


def check_encounter(player_stats, interaction):
    """Check which quest user has encountered
    Args:
        player_stats: list of user statistics
        interaction: tuple with coordinates of the quest
    Returns:
        player_stats: list of user statistics
        interaction: tuple with coordinates of the quest
    """
    if interaction[0] == '?' or interaction[1] == '?':
        find_lab_part(player_stats)
        interaction = (' ', ' ')

    elif interaction[0] == '|' or interaction[1] == '|':
        repair_lab()

    elif interaction[0] == '$' or interaction[1] == '$':
        sell_drugs(player_stats)
        interaction = (' ', ' ')

    elif interaction[0] == 'E' or interaction[1] == 'E':
        defeat = False
        player_stats, defeat = fight_enemy(player_stats, defeat)
        if defeat:
            interaction = (' ', ' ')

    elif interaction[0] == ')' or interaction[1] == ')':
        collect_TNT(player_stats)

    elif interaction[0] == 'I' or interaction[1] == 'I':
        load_map.next_level(player_stats)

    return player_stats, interaction


def fight_enemy(player_stats, defeat):
    """Mechanics of fight with the enemy
    Args:
        player_stats: list of user statistics
        defeat: True if user defeated an enemy
    Returns:
        player_stats: list of user statistics
        defeat: True if user defeated an enemy
    """
    enemy_life = 100
    print('You have encounter an enemy.')
    while True:
        answer = input('Enter "a" to attack or "r" to run away: ')
        if answer == 'a':
            if player_stats[1] <= 10:
                enemy_life -= 20
                player_stats[2] -= 1
                print('You hitted for 20. You lost 1 armor. Enemy life:', enemy_life, 'Your armor:', player_stats[2])
            elif player_stats[1] > 10 and player_stats[1] <= 30:
                enemy_life -= 30
                player_stats[2] -= 1
                print('You hitted for 30. You lost 1 armor Enemy life:', enemy_life, 'Your armor:', player_stats[2])
            else:
                enemy_life -= 40
                player_stats[2] -= 1
                print('You hitted for 40. You lost 1 armor Enemy life:', enemy_life, 'Your armor:', player_stats[2])
            if enemy_life <= 0:
                print('You won!')
                defeat = True
                player_stats[4] += 1
                player_stats[3] += 100
                time.sleep(0.5)
                break
            if player_stats[2] <= 0:
                boss.display_screen('lose.txt')
                sys.exit()
        if answer == 'r':
            print('Run you fool!!!')
            time.sleep(0.5)
            break
    return player_stats, defeat


def guns_shop(player_stats):
    """Quest with gun shop - you can buy items there
    Args:
        player_stats: list of user statistics
    Returns:
        none
    """
    inventory = {}
    print('GUN MASTER: Welcome to my shop Pablo!')

    while True:
        buy = input('GUN MASTER: Do you want to buy something? ').lower()

        if buy == 'yes':

            while True:
                answer = input('GUN MASTER: What do you want to buy? I can offer AK-47 and M4-A1: ').upper()

                if answer == 'AK-47':
                    if player_stats[3] >= 200:
                        player_stats[3] -= 200
                        player_stats[1] += 100
                        inventory['AK-47'] = (25, 100, 'weapon')
                        backpack.add_item_to_backpack_file(inventory)
                        print('Take it!')
                        time.sleep(1)
                        break
                    else:
                        print('S*IT! I dont have money!')
                        time.sleep(1)
                        break
                elif answer == 'M4-A1':
                    if player_stats[3] >= 200:
                        player_stats[1] += 100
                        inventory['M4-A1'] = (30, 90, 'weapon')
                        backpack.add_item_to_backpack_file(inventory)
                        print('Take it!')
                        time.sleep(1)
                        break
                    else:
                        print('S*IT! I dont have money!')
                        time.sleep(1)
                        break
            break

        elif buy == 'no':
            break


def find_lab_part(player_stats):
    """Quest with laboratory, you can buy lab part there
    Args:
        player_stats: list of user statistics
    Returns:
        none
    """
    inventory = {}
    print('PABLO: Hola José Rodríguez Gacha!')
    print('GACHA: Welcome Pablo!\nIf you want take a lost part for yor lab, you can buy it here. Its cost 800 $!')

    while True:
        answer = input('Do you want to buy it Pablo?\n').lower()

        if answer == 'yes':
            if player_stats[3] > 800:
                player_stats[3] -= 800
                inventory['lab_part'] = (0, 100, 'quest_item')
                backpack.add_item_to_backpack_file(inventory)
                print('YOU GOT LAB PART, NOW YOU CAN FIX YOU LABORATORY!')
                break
            else:
                print('GACHA: Come back with money Pablo!')
                break

        elif answer == 'no':
            break

    return player_stats


def repair_lab():
    """Quest with repairing the laboratory
    Args:
        none
    Returns:
        none
    """
    inventory = backpack.open_backpack_file()

    if 'lab_part' in inventory:
        print('PABLO: Finally my laboratorium is work fine!\n Now you can make COCAINE! Lets get to work amigos!!!')
        del inventory['lab_part']

        time.sleep(2)
        print('YOU EARN 20KG COCAINE!')

        inventory['COCAINE'] = (0, 20, 'drugs')
        backpack.save_backpack_to_file(inventory)

    elif 'lab_part' not in inventory:
        print('PABLO: My laboratorium is destroyed, I need to find lab part to fix it!')


def sell_drugs(player_stats):
    """Mechanics of selling drugs to the encountered people
    Args:
        player_stats: list of user statistics
    Returns:
        none
    """
    inventory = backpack.open_backpack_file()
    print('PABLO: Hi bastards! Do you want to buy some COCAINE?')

    while True:
        if 'COCAINE' in inventory:
            try:
                price_cocaine = int(input('BASTARDS: Hola Pablo! Ofcourse we need it! Tell me the price for 1kg?\n'))

                if price_cocaine > 500:
                    price = random.randint(100, 300)
                    print('\nBASTARDS: Thats not fair Pablo! I can pay', price, '$.')
                    amount = random.randint(1, 5)
                    print('And I want ', amount, 'kg of COCAINE.')
                    amount_answer = input('Is it fine for you amoigo?!').lower()

                    if amount_answer == 'yes':
                        amount_of_cocain = inventory.get('COCAINE')
                        cocain_left = amount_of_cocain[1] - amount
                        inventory['COCAINE'] = (0, cocain_left, 'drugs')
                        player_stats[3] += price * amount
                        break

                    else:
                        print('Plata o plomo!')
                        break
                else:
                    print('BASTARDS: Ok Pablo, this is fair price! Lets trade.')

                    amount_of_cocain = inventory.get('COCAINE')
                    amount = random.randint(1, 5)

                    print('I want ', amount, 'kg of COCAINE.')

                    cocain_left = amount_of_cocain[1] - amount
                    inventory['COCAINE'] = (0, cocain_left, 'drugs')
                    player_stats[3] += price_cocaine * amount
                    break

            except ValueError:
                continue

        else:
            print('BASTARDS: You dont have COCAINE Pablo, hahahah! What happend with you RAT!')
            break
    backpack.save_backpack_to_file(inventory)


def collect_TNT(player_stats):
    """Quest where you can buy the tnt bomb
    Args:
        player_stats: list of user statistics
    Returns:
        none
    """
    inventory = backpack.open_backpack_file()

    print('FABIO OCHOA: Hola Pablo! Welcome in my shop!')
    time.sleep(1)
    print('PABLO ESCOBAR: Hola Fabio')

    while True:

        ask_for_buy = input('FABIO OCHOA: You looking for some explode materials Pablo?\nPABLO: ').lower()

        if ask_for_buy == 'yes':
            TNT_price = 800

            if player_stats[3] > TNT_price:
                player_stats[3] -= TNT_price
                if 'TNT' in inventory:
                    amount_of_TNT = inventory['TNT'][1]
                    amount_of_TNT += amount_of_TNT
                    inventory['TNT'] = (1500, amount_of_TNT, 'explode materials')
                    time.sleep(1)
                    print('YOU GET TNT! NOW YOU CAN HAVE SOME FUN!')
                    break
                else:
                    inventory['TNT'] = (1500, 80, 'explode materials')
                    time.sleep(1)
                    print('YOU GET TNT! NOW YOU CAN HAVE SOME FUN!')
                    break

            else:
                print('FABIO OCHOA: Im sorry Pablo but you dont have enough money')
                break
        else:
            print('FABIO OCHOA: For what you came here fool! Go away!')
            break
    backpack.save_backpack_to_file(inventory)
