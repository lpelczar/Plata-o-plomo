import os
import sys
import tty
import termios


def read_map_from_file(filename):

    board = []

    with open(filename) as f:
        read_data = f.read().splitlines()

    board = [list(x) for x in read_data]

    return board


def print_map(board):

    for row in board:
        print(''.join(row))
        # print(row)


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
    print_map(read_map_from_file('Map1.txt'))

    x = getch()
    print(x)


if __name__ == '__main__':
    main()
