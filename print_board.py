import os
import player


def print_map(y, x, board, player_stats, appearance):
    """Print the current map to the console
    Args:
        y, x: current coordinates of the player
        board: list of list representing our map
        player_stats: list of user statistics
        appearance: user appearance
    Returns:
        none
    """
    os.system('clear')
    board[y][x] = appearance

    for row in board:
        print(''.join(row))

    player.display_stats(player_stats)
