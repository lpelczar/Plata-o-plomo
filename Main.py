import os
import print_board
import player
import backpack
import introduction
import interactions
import change_level
import load_map
import sys
import key_getch


def player_starting_position(y, x, board):
    position = (y, x)

    return position


def player_moving(y, x, board):

    wall = ['X', 'A', '_', '|', '=']
    position = ()

    while True:
        ch = key_getch.getch()

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


def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    introduction.menu_select()
    starting_bonus = introduction.character_creation()

    player_starting_stats = player.player_starting_bonus(starting_bonus)

    game_map = load_map.read_map_from_file('Map1.txt')
    position = player_starting_position(23, 50, game_map)
    print_board.print_map(position[0], position[1], game_map, player_starting_stats, starting_bonus[0])
    player_stats = player_starting_stats

    inventory = {}
    inventory = backpack.backpack_items(starting_bonus[1], inventory)
    backpack.save_backpack_to_file(inventory)

    while True:
        position = player_moving(position[0], position[1], game_map)
        print_board.print_map(position[0], position[1], game_map, player_stats, starting_bonus[0])
        position, player_stats = interactions.take_quest(position[0], position[1], game_map, player_stats)


if __name__ == '__main__':
    main()
