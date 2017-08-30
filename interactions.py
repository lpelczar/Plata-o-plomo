import backpack


def take_quest(y, x, board, cash):

    if board[y][x+1] == '?':
        board[y][x] = board[y][x]
        quest_1(cash)

    elif board[y][x-1] == '?':
        board[y][x] = board[y][x]
        quest_1(cash)

    elif board[y+1][x] == '?':
        board[y][x] = board[y][x]
        quest_1(cash)

    elif board[y-1][x] == '?':
        board[y][x] = board[y][x]
        quest_1(cash)


def quest_1(cash):
    inventory = {}
    print('PABLO: Hola José Rodríguez Gacha!')
    print('GACHA: Welcome Pablo!\nIf you want take a lost part for yor lab, you can buy it here. Its cost 800 $!')

    while True:
        answer = input('Do you want to buy it Pablo?\n')

        if answer == 'yes':
            cash -= 800
            inventory['lab_part'] = (0, 100, 'quest_item')
            backpack.save_backpack_to_file(inventory)
            break

        elif answer == 'no':
            break

    return cash
