import csv


def open_backpack_file():
    backpack = {}
    with open('backpack.txt', 'r') as f:
        f = csv.reader(f, delimiter=',')

        for line in f:
            try:
                backpack[line[0]] = ('dmg:', int(line[1]), 'weight:', int(line[2]))
            except:
                continue
    print(backpack)
    return backpack


def backpack_items(backpak):
    pass


def display_backpack(backpack):
    pass


def save_backpack_to_file(backapack):
    save_list = []

    with open('backpack.txt', 'a') as f:
        f = csv.writer(f, delimiter=',')

        for key in backpack:
            save_list.append([key, backpack[key]])
        print(save_list)

        for data in save_list:
            f.writerow(save_list[data])


backpack = open_backpack_file()
save_backpack_to_file(backpack)
