import os
import player


def print_map(y, x, board, player_stats, appearance):
    os.system('clear')
    board[y][x] = appearance

    for row in board:
        row = color_map(row)
        print(''.join(row))

    player.display_stats(player_stats)


def color_map(row):

    colors = {'wall': ('\x1b[0;31;43m', '\x1b[0m'),
              'grass': ('\x1b[2;32;40m', '\x1b[0m'),
              'buildings': ('\x1b[0;33;40m', '\x1b[0m'),
              'explode': ('\x1b[1;31;40m', '\x1b[0m'),
              'entrance': ('\x1b[3;31;40m', '\x1b[0m')}

    format_wall = ''.join([colors['wall'][0], ' ', colors['wall'][1]])
    format_grass = ''.join([colors['grass'][0], ',', colors['grass'][1]])
    format_buildings = ''.join([colors['buildings'][0], '_', colors['buildings'][1]])
    format_explode = ''.join([colors['explode'][0], '*', colors['explode'][1]])
    format_entrance = ''.join([colors['entrance'][0], 'I', colors['entrance'][1]])

    # row = [format_wall if x == 'X' else x for x in row]

    row2 = []
    for x in row:
        if x == 'X':
            row2.append(format_wall)

        elif x == ' ':
            row2.append(format_grass)

        elif x == '_':
            row2.append(format_buildings)

        elif x == '*':
            row2.append(format_explode)

        elif x == '|' or x == 'I' or x == '(' or x == ')':
            row2.append(format_entrance)

        else:
            row2.append(x)

    return row2
