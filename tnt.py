import time
import print_board
import backpack


def ask_explode_intent(y, x, board, player_stats):
    inventory = backpack.open_backpack_file()

    while True:
        answer = input('Do you want to blow up this wall? ').lower()
        if answer == 'yes' and 'TNT' in inventory:
            explode(y, x, board, player_stats)
            break
        else:
            print('PABLO: F*CK! I dont have TNT to blow up this wall!')
            time.sleep(2)
            break


def explode(y, x, board, player_stats):
    board[y][x+6] = '*'
    print_board.print_map(y, x, board, player_stats, '@')

    blow_y = 1
    while blow_y != 3:
        for i in range(7, 14):
            board[y][x+i] = '*'
            board[y+blow_y][x+i] = '*'
            board[y-blow_y][x+i] = '*'
            board[y][(x+14)-i] = '*'
            board[y+blow_y][(x+14)-i] = '*'
            board[y-blow_y][(x+14)-i] = '*'
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
