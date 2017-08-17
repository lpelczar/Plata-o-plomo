import os


def read_map_from_file(filename):
    with open(filename) as f:
        read_data = f.read()
    return read_data


def print_map(map):
    print(map)


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_map(read_map_from_file('Map1.txt'))


if __name__ == '__main__':
    main()
