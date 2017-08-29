import csv


def open_backpack_file():
    backpack = {}
    with open('backpack.txt', 'r') as f:
        f = csv.reader(f, delimiter=',')

        for line in f:
            try:
                backpack[line[0]] = (int(line[1]), int(line[2]), str(line[3]))
            except:
                continue
    print(backpack)
    return backpack


def backpack_items(backpak):
    pass


def display_backpack(backpack):

    table_line = '_'
    table_lenght = 24

    for key, value in backpack.items():

        if value[2] == 'cloths':
            formated_line = '{:>5} {:<5} {:>15} {:>15} {:<5}'.format('Armor:', value[0], key, 'Weight:', value[1])
            print(table_line*table_lenght, 'CLOTHS', table_line*table_lenght)
            print('|', formated_line, '|')
            print(table_line*len(formated_line))

        if value[2] == 'weapon':
            print(table_line*table_lenght, 'GUNS', table_line*table_lenght)
            formated_line = '{:>3} {:<5} {:>15} {:>15} {:<3}'.format('Dmg:', value[0], key, 'Weight:', value[1])
            print('|', formated_line, '|')
            print(table_line*len(formated_line))


def save_backpack_to_file(backapack):

    with open('backpack.txt', 'a') as f:
        w = csv.writer(f, delimiter=',')

        for key, value in backpack.items():
            w.writerow((key, value[0], value[1], value[2]))


backpack = open_backpack_file()
# save_backpack_to_file(backpack)
display_backpack(backpack)
