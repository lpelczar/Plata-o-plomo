import csv
import os


def open_backpack_file():
    backpack = {}
    with open('backpack.txt', 'r') as f:
        f = csv.reader(f, delimiter=',')

        for line in f:
            try:
                backpack[line[0]] = (int(line[1]), int(line[2]), str(line[3]))
            except:
                continue

    return backpack


def backpack_items(backpak):
    pass


def display_backpack(backpack):

    os.system('clear')
    table_line = '_'
    table_lenght_armor = 16
    table_lenght_guns = 16
    armor_index = 1
    guns_index = 1

    print(' ', table_line*table_lenght_armor, ' CLOTHS ', table_line*table_lenght_armor)

    for key, value in backpack.items():
        if value[2] == 'cloths':
            formated_line = '{:>5} {:<5} {:>10} {:>10} {:<3}'.format('Armor:', value[0], key, 'Weight:', value[1])
            print('|', (str(armor_index)+'.'), formated_line, '|')
            armor_index += 1
    print('| ', table_line*(len(formated_line)+1), ' |')

    print(' ', table_line*table_lenght_guns, '  GUNS  ', table_line*table_lenght_guns)

    for key, value in backpack.items():
        if value[2] == 'weapon':
            formated_line = '{:>5} {:<5} {:>10} {:>10} {:<3}'.format('Damage:', value[0], key, 'Weight:', value[1], ' ')
            print('|', (str(guns_index)+'.'), formated_line, '|')
            guns_index += 1
    print('|', table_line*(len(formated_line)+3), '|')


def save_backpack_to_file(backapack):

    with open('backpack.txt', 'a') as f:
        w = csv.writer(f, delimiter=',')

        for key, value in backpack.items():
            w.writerow((key, value[0], value[1], value[2]))


backpack = open_backpack_file()
# save_backpack_to_file(backpack)
display_backpack(backpack)
