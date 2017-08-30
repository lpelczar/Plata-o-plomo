import time
import print_board


def ask_explode_intent(y, x, board, player_stats):
    yes = ['YES', 'yes', 'Yes']
    while True:
        answer = input('Do you want to blow up this wall? ')
        if answer in yes:
            explode(y, x, board, player_stats)
            break
        if answer in no:
            break


def explode(y, x, board, player_stats):
    time.sleep(2)
    board[y][x+1] = '*'
    print_board.print_map(y, x, board, player_stats, '@')
    time.sleep(0.4)

    board[y-1][x+1] = '*'
    board[y+1][x+1] = '*'
    board[y][x+2] = '*'
    board[y][x] = '*'
    print_board.print_map(y, x, board, player_stats, '@')
    time.sleep(0.4)

    board[y+1][x+2] = '*'
    board[y-1][x] = '*'
    board[y-1][x+2] = '*'
    board[y+1][x] = '*'
    print_board.print_map(y, x, board, player_stats, '@')
    time.sleep(0.4)
    clear_explosion(y, x, board)
    return board


def clear_explosion(y, x, board):
    board[y][x+1] = ' '
    board[y-1][x+1] = ' '
    board[y+1][x+1] = ' '
    board[y][x+2] = ' '
    board[y][x] = ' '
    board[y+1][x+2] = ' '
    board[y-1][x] = ' '
    board[y-1][x+2] = ' '
    board[y+1][x] = ' '
