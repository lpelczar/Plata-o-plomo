import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_screen(filename):
    with open(filename) as f:
        read_data = f.read()
    print(read_data)


def go_back():
    while True:
        back = input('Press \'z\' to go back: ')
        if back == 'z':
            menu_select()
            break


def menu_select():
    clear_console()
    display_screen('start_screen.txt')
    starting_bonus = ()
    while True:
        answer = input("Choose option: ")
        if answer == '1':
            starting_bonus = character_creation()
            break
        elif answer == '2':
            clear_console()
            display_screen('howtoplay_screen.txt')
            go_back()
            break
        elif answer == "3":
            clear_console()
            display_screen('about_screen.txt')
            go_back()
            break
    return starting_bonus


def character_creation():
    clear_console()
    symbols = ['@', '#', '&']
    while True:
        appearance = input('Select your appearance: @, # or & ')
        if appearance in symbols:
            break
    clear_console()
    while True:
        bonus = input('''Select one bunus:
                         1. Huge \033[91mBackpack\033[0m (capacity increased by 100)
                         2. \033[91mGun\033[0m (bigger damage for start)
                         3. Nice \033[91mshirt\033[0m (increase armor and personal charm, more money for drugs)
                         Type here: ''').upper()
        if bonus == '1':
            return appearance, 'backpack'
        elif bonus == '2':
            return appearance, 'gun'
        elif bonus == '3':
            return appearance, 'shirt'
