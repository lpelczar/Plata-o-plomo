import time
import print_board
import backpack


def ask_explode_intent(y, x, board, player_stats):
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
            else:
                print('PABLO: F*CK! I need one more TNT to blow something in Warsaw!')
                break
        else:
            print('PABLO: F*CK! I dont have TNT to blow up this wall! And another one to blow something in Warsaw!')
            time.sleep(2)
            break
    backpack.save_backpack_to_file(inventory)


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
