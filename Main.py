import os
import sys
import tty
import termios


def read_map_from_file(filename):

    with open(filename) as f:
        read_data = f.read().splitlines()

    board = [list(x) for x in read_data]
    print(board)

    return board


def moving(y, x, board):

    board[y][x] = '@'
    wall = ['X']
    os.system('clear')
    print_map(board)

    while True:
        ch = getch()
        if ch == 'd' and board[y][x+1] not in wall:
            board[y][x] = ' '
            x = x + 1
            break
        elif ch == 'a' and board[y][x-1] not in wall:
            board[y][x] = ' '
            x = x - 1
            break
        elif ch == 'w' and board[y-1][x] not in wall:
            board[y][x] = ' '
            y = y - 1
            break
        elif ch == 's' and board[y+1][x] not in wall:
            board[y][x] = ' '
            y = y + 1
            break
        elif ch == 'q':
            sys.exit()

    os.system('clear')
    print_map(board)
    moving(y, x, board)


def interactions(y, x, board):

    if board[y][x] == 'A':
        ask = input('Welcome in my shop! Chose want do you want to do:\n')


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


def display_screen(filename):
    with open(filename) as f:
        read_data = f.read()
    print(read_data)


def menu_select():
    while True:
        answer = input('Choose option: ')
        if answer == "1":
            moving(5, 5, read_map_from_file('Map1.txt'))
        elif answer == "2":
            os.system('clear')
            display_screen('howtoplay_screen.txt')
            while True:
                back = input('Press \'z\' to go back: ')
                if back == 'z':
                    main()
        elif answer == "3":
            os.system('clear')
            display_screen('about_screen.txt')
            while True:
                back = input('Press \'z\' to go back: ')
                if back == 'z':
                    main()


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    map = read_map_from_file('Map1.txt')

    while True:
        moving(5, 5, map)


if __name__ == '__main__':
    main()
