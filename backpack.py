import csv
import os


def open_backpack_file():
    """Open backpack from file and append items to backpack dictionary
    Args:
        none
    Returns:
        backpack: dictionary with items read from file
    """
    backpack = {}
    with open('backpack.txt', 'r') as f:
        f = csv.reader(f, delimiter=',')

        for line in f:
            try:
                backpack[line[0]] = (int(line[1]), int(line[2]), str(line[3]))
            except:
                continue

    return backpack


def backpack_items(starting_item, backpack):
    """Add starting items to backpack dictionary
    Args:
        starting_item: item user choosed at the beginning of the game
        backpack: dictionary with user items
    Returns:
        backpack: dictionary with user items
    """
    if starting_item == 'gun':
        backpack['Glock'] = (5, 30, 'weapon')

    elif starting_item == 'shirt':
        backpack['Blue T-shirt'] = (10, 25, 'clothes')

    return backpack


def display_backpack(backpack):
    """Print backpack dictionary in a pretty table
    Args:
        backpack: dictionary with user items
    Returns:
        none
    """
    os.system('clear')
    table_line = '_'
    table_length = 16
    line_number = 1

    try:
        print(table_line*table_length, ' BACKPACK ', table_line*table_length)

        for key, value in backpack.items():
            if value[2] == 'clothes':
                formated_line = '{:>5} {:<5} {:>10} {:>10} {:<3}'.format('Armor:', value[0], key, 'Weight:', value[1])
                print('|', (str(line_number)+'.'), formated_line, '|')
                line_number += 1
            elif value[2] == 'weapon':
                formated_line = '{:>5} {:<5} {:>10} {:>9} {:<3}'.format('Damage:', value[0], key, 'Weight:', value[1])
                print('|', (str(line_number)+'.'), formated_line, '|')
                line_number += 1

            elif value[2] == 'quest_item' or value[2] == 'drugs' or value[2] == 'explode materials':
                formated_line = '{:>5} {:<5} {:>10} {:>10} {:<3}'.format('Power:', value[0], key, 'Weight:', value[1])
                print('|', (str(line_number)+'.'), formated_line, '|')
                line_number += 1

        print('| ', table_line*(len(formated_line)+1), ' |')
        print('Press w,a,s,d to back to game:')

    except:
        print('Empty')


def save_backpack_to_file(backpack):
    """Open file and save values of backpack dictionary to the file
    Args:
        backpack: dictionary with user items
    Returns:
        none
    """
    with open('backpack.txt', 'w') as f:
        w = csv.writer(f, delimiter=',')

        for key, value in backpack.items():
            w.writerow((key, value[0], value[1], value[2]))


def add_item_to_backpack_file(backpack):
    """Append item at the end of the file
    Args:
        backpack: dictionary with user items
    Returns:
        none
    """
    with open('backpack.txt', 'a') as f:
        w = csv.writer(f, delimiter=',')

        for key, value in backpack.items():
            w.writerow((key, value[0], value[1], value[2]))
