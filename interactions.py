import backpack
import tnt
import time
import random
import boss
import sys
enemies_killed = 0


def take_quest(y, x, board, player_stats):
    interactions = ['?', '|', 'E', '$']

    if board[y][x+1] in interactions or board[y][x-1] in interactions:
        interaction = (board[y][x+1], board[y][x-1])
        check_encounter(player_stats, interaction)

    elif board[y+1][x] in interactions or board[y-1][x] in interactions:
        interaction = (board[y+1][x], board[y-1][x])
        check_encounter(player_stats, interaction)

    elif board[y][x+1] == '(':
        tnt.ask_explode_intent(y, x, board, player_stats)

    elif board[y-1][x] == '=':
        guns_shop(player_stats)

    return player_stats


def check_encounter(player_stats, interaction):
    if interaction[0] == '?' or interaction[1] == '?':
        quest_1(player_stats)

    elif interaction[0] == '|' or interaction[1] == '|':
        repair_lab()

    elif interaction[0] == '$' or interaction[1] == '$':
        sell_drugs(player_stats)

    elif interaction[0] == 'E' or interaction[1] == 'E':
        fight_enemy(player_stats)

    return player_stats


def fight_enemy(player_stats):
    global enemies_killed
    enemy_life = 100
    print('You have encounter an enemy.')
    while True:
        answer = input('Enter "attack" to attack or "run" to run away: ')
        if answer == 'attack':
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
                enemies_killed += 1
                time.sleep(0.5)
                break
            if player_stats[2] <= 0:
                boss.display_screen('lose.txt')
                sys.exit()
        if answer == 'run':
            print('Run you fool!!!')
            time.sleep(0.5)
            break
    return player_stats


def guns_shop(player_stats):
    inventory = {}
    print('Welcome to my shop Pablo!')

    while True:
        buy = input('Do you want to buy something? ').lower()

        if buy == 'yes':

            while True:
                answer = input('What do you want to buy? I can offer AK-47 and M4-A1: ')

                if answer == 'AK-47':
                    player_stats[3] -= 200
                    player_stats[1] += 100
                    inventory['AK-47'] = (25, 100, 'weapon')
                    backpack.add_item_to_backpack_file(inventory)
                    print('Item added to your inventory!')
                    time.sleep(1)
                    break

                elif answer == 'M4-A1':
                    player_stats[3] -= 200
                    player_stats[1] += 100
                    inventory['M4-A1'] = (30, 90, 'weapon')
                    backpack.add_item_to_backpack_file(inventory)
                    print('Item added to your inventory!')
                    time.sleep(1)
                    break
            break

        elif buy == 'no':
            break


def quest_1(player_stats):
    inventory = {}
    print('PABLO: Hola José Rodríguez Gacha!')
    print('GACHA: Welcome Pablo!\nIf you want take a lost part for yor lab, you can buy it here. Its cost 800 $!')

    while True:
        answer = input('Do you want to buy it Pablo?\n').lower()

        if answer == 'yes':
            player_stats[3] -= 800
            inventory['lab_part'] = (0, 100, 'quest_item')
            backpack.add_item_to_backpack_file(inventory)
            break

        elif answer == 'no':
            break

    return player_stats


def repair_lab():
    inventory = backpack.open_backpack_file()

    if 'lab_part' in inventory:
        print('PABLO: Finally my laboratorium is work fine!\n Now you can make COCAINE! Lets get to work amigos!!!')
        del inventory['lab_part']

        time.sleep(2)
        print('YOU EARN 20KG COCAINE!')

        inventory['COCAINE'] = (0, 20, 'drugs')
        backpack.save_backpack_to_file(inventory)

    elif 'lab_part' not in inventory:
        print('PABLO: My laboratorium is destroied, I need to find lab part to fix it!')


def sell_drugs(player_stats):
    inventory = backpack.open_backpack_file()
    print('PABLO: Hi bastards! Do you want to buy some COCAINE?')

    while True:
        if 'COCAINE' in inventory:
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
                    print(cocain_left)
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
                print(cocain_left)
                inventory['COCAINE'] = (0, cocain_left, 'drugs')
                player_stats[3] += price_cocaine * amount
                break

        else:
            print('BASTARDS: You dont have COCAINE Pablo, hahahah! What happend with you RAT!')
            break
        backpack.save_backpack_to_file(inventory)
