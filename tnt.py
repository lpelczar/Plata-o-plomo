import time
import print_board
import backpack


def ask_explode_intent(y, x, board, player_stats):
    """Ask the user if he want to explode the wall
    Args:
        y, x: current coordinates of the player
        board: list of list representing our map
        player_stats: list of user statistics
    Returns:
        none
    """
    inventory = backpack.open_backpack_file()

    while True:
        answer = input('Do you want to blow up this wall? ').lower()
        if answer == 'yes' and 'TNT' in inventory:
            if inventory['TNT'][1] == 160:
                explode(y, x, board, player_stats)
                amount_of_TNT = inventory['TNT'][1]
                amount_of_TNT -= 80
                inventory['TNT'] = (1500, amount_of_TNT, 'explode materials')
                break

            elif inventory['TNT'][1] == 80 and player_stats[4] > 0:
                explode(y, x, board, player_stats)
                amount_of_TNT = inventory['TNT'][1]
                amount_of_TNT -= 80
                inventory['TNT'] = (1500, amount_of_TNT, 'explode materials')
                break

            else:
                print('PABLO: F*CK! I need one more TNT to blow something in Warsaw!')
                break
        else:
            print('PABLO: F*CK! I dont have TNT to blow up this wall! And another one to blow something in Warsaw!')
            time.sleep(2)
            break
    backpack.save_backpack_to_file(inventory)


def explode(y, x, board, player_stats):
    """Animate explosion
    Args:
        y, x: current coordinates of the player
        board: list of list representing our map
        player_stats: list of user statistics
    Returns:
        board: list of lists representing our board
    """
    board[y][x+6] = '*'
    print_board.print_map(y, x, board, player_stats, '@')

    blow_y = 1
    # while blow_y != 3:
    #     for i in range(7, 14):
    #         board[y][x+i] = '*'
    #         board[y+blow_y][x+i] = '*'
    #         board[y-blow_y][x+i] = '*'
    #         board[y][(x+14)-i] = '*'
    #         board[y+blow_y][(x+14)-i] = '*'
    #         board[y-blow_y][(x+14)-i] = '*'
    #         print_board.print_map(y, x, board, player_stats, '@')
    #         time.sleep(0.05)
    #     blow_y += 1
    #
    clear_y = 1
    # while clear_y != 3:
    #     for i in range(7, 14):
    #         board[y][x+i] = ' '
    #         board[y+clear_y][x+i] = ' '
    #         board[y-clear_y][x+i] = ' '
    #         board[y][(x+14)-i] = ' '
    #         board[y+clear_y][(x+14)-i] = ' '
    #         board[y-clear_y][(x+14)-i] = ' '
    #         print_board.print_map(y, x, board, player_stats, '@')
    #         time.sleep(0.05)
    #     clear_y += 1
    blow_y = 1
    while blow_y != 3:
        for i in range(7, 14):
            board[y][x+i] = '*'  # srodek prawo

            board[y+blow_y][x+i] = '*'  # prawy gorny
            board[y-blow_y][(x+14)-i] = '*'  # lewy dolny
            print_board.print_map(y, x, board, player_stats, '@')

            for i in range(7, 14):
                board[y+blow_y][(x+14)-i] = '*'  # lewy gorny
                board[y-blow_y][x+i] = '*'  # prawy dolny

                board[y][(x+14)-i] = '*'  # srodek lewo

            print_board.print_map(y, x, board, player_stats, '@')

            time.sleep(0.05)
        blow_y += 1

    clear_y = 1
    while clear_y != 3:
        for i in range(7, 14):
            board[y][x+i] = ' '
            board[y+clear_y][x+i] = ' '
            board[y-clear_y][x+i] = ' '
            board[y][(x+14)-i] = ' '
            board[y+clear_y][(x+14)-i] = ' '
            board[y-clear_y][(x+14)-i] = ' '
            print_board.print_map(y, x, board, player_stats, '@')
            time.sleep(0.05)
        clear_y += 1

    return board
