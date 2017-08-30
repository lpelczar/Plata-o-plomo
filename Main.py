import os
import sys
import tty
import termios
import player
import backpack
import introduction


def read_map_from_file(filename):

    with open(filename) as f:
        read_data = f.read().splitlines()

    board = [list(x) for x in read_data]

    return board


def player_starting_position(y, x, board):
    position = (y, x)

    return position


def player_moving(y, x, board):

    board[y][x] = '@'
    wall = ['X', 'A']
    position = ()

    while True:
        ch = getch()

        if ch == 'd' and board[y][x+1] not in wall:
            board[y][x] = ' '
            x = x + 1
            position = (y, x)
            break

        elif ch == 'a' and board[y][x-1] not in wall:
            board[y][x] = ' '
            x = x - 1
            position = (y, x)
            break

        elif ch == 'w' and board[y-1][x] not in wall:
            board[y][x] = ' '
            y = y - 1
            position = (y, x)
            break

        elif ch == 's' and board[y+1][x] not in wall:
            board[y][x] = ' '
            y = y + 1
            position = (y, x)
            break

        elif ch == 'b':
            inventory = backpack.open_backpack_file()
            backpack.display_backpack(inventory)

        elif ch == 'q':
            sys.exit()

    return position


def print_map(y, x, board, player_stats, appearance):
    os.system('clear')
    board[y][x] = appearance

    for row in board:
        print(''.join(row))

    player.display_stats(player_stats)  # Printuje staty gracza pod mapa


def getch():

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    introduction.menu_select()
    starting_bonus = introduction.character_creation()
    player_stats = player.player_starting_stats(starting_bonus)

    map1 = read_map_from_file('Map1.txt')
    position = player_starting_position(5, 5, map1)
    print_map(position[0], position[1], map1, player_stats, starting_bonus[0])

    while True:

        position = player_moving(position[0], position[1], map1)
        print_map(position[0], position[1], map1, player_stats, starting_bonus[0])
        # Interactions.shop(position[0], position[1], map1)


if __name__ == '__main__':
    main()
