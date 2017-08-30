import os
import player


def print_map(y, x, board, player_stats, appearance):
    os.system('clear')
    board[y][x] = appearance

    for row in board:
        print(''.join(row))

    player.display_stats(player_stats)
