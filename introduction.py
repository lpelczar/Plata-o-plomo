import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_screen(filename):
    with open(filename) as f:
        read_data = f.read()
    print(read_data)


def menu_select():

    while True:
        clear_console()
        display_screen('start_screen.txt')
        answer = input("Choose option: ")

        if answer == '1':
            break

        elif answer == '2':
            clear_console()
            display_screen('howtoplay_screen.txt')
            input('\nPress any key to go back')

        elif answer == '3':
            clear_console()
            display_screen('about_screen.txt')
            input('\nPress any key to go back')


def character_creation():
    clear_console()
    symbols = ['@', '#', '&']
    display_screen('intro.txt')
    while True:
        appearance = input('Select your appearance: @, # or & ')
        if appearance in symbols:
            break
    print('')

    while True:
        bonus = input('''Select starting bonus:
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
