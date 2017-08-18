import os
import sys
import tty
import termios


def read_map_from_file(filename):

    with open(filename) as f:
        read_data = f.read().splitlines()

    board = [list(x) for x in read_data]

    return board


def moving(y, x, board):
    board[y][x] = '@'
    os.system('clear')
    print_map(board)
    while True:
        ch = getch()
        if ch == 'd':
            board[y][x] = ' '
            x = x + 1
            break
        elif ch == 'a':
            board[y][x] = ' '
            x = x - 1
            break
        elif ch == 'w':
            board[y][x] = ' '
            y = y - 1
            break
        elif ch == 's':
            board[y][x] = ' '
            y = y + 1
            break
    os.system('clear')
    print_map(board)
    moving(y, x, board)


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


def display_start_screen():
    with open('start_screen.txt') as f:
        read_data = f.read()
    print(read_data)


def menu_select():
    while True:
        answer = input('Choose option: ')
        if answer == "1":
            map = read_map_from_file('Map1.txt')
            moving(5, 5, map)


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_start_screen()
    menu_select()


if __name__ == '__main__':
    main()
