import os
import random
import time


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_boss():
    with open('boss.txt') as f:
        read_data = f.read()
    print('\033[91m' + read_data + '\033[0m')


def play_cold_warm():
    user_guesses = 5
    correct_answer = generate_unique_number()
    while user_guesses > 0:
        user_input = get_user_input()
        feedback = compare_user_answer(user_input, correct_answer)
        print('Hint: ', end='')
        for i in feedback:
            print(i, end=' ')
        print('   Guesses left:', user_guesses - 1)
        if feedback == ['hot', 'hot', 'hot']:
            display_screen('win.txt')
            break
        user_guesses -= 1
        if user_guesses == 0:
            display_screen('lose.txt')
            break


def get_user_input():
    while True:
        user_input = input('Enter 3-digit unique number: ')
        if user_input.isdigit() and len(user_input) == 3 and len(set(user_input)) == len(user_input):
            break
        else:
            print('Number should have 3 unique digits!')
    return list(user_input)


def display_screen(filename):
    clear_console()
    with open(filename) as f:
        read_data = f.read()
    print(read_data)


def compare_user_answer(guess, correct_answer):
    hints = []
    for i in range(len(guess)):
        if guess[i] == correct_answer[i]:
            hints.insert(0, 'hot')
        elif guess[i] in correct_answer:
            hints.append('warm')
    if not hints:
        hints = ['cold']
    return hints


def generate_unique_number():
    unique_number_list = [str(x) for x in range(10)]
    random.shuffle(unique_number_list)
    return unique_number_list[:3]


def start_fight():
    yes = ['YES', 'yes', 'Yes']
    no = ['NO', 'no', 'No']
    clear_console()
    display_boss()
    while True:
        answer = input('Pershing: Pablo mi amigo! We were always good friends. Now you want to fight with me? ')
        if answer in yes:
            print('Pershing: As you wish, lets play cold/warm, I thought of 3 unique digit number, you have 10 guesses to guess it!')
            play_cold_warm()
            break
        if answer in no:
            print('Pershing: I thought so! Go home Pablo!')
            time.sleep(2)
            display_screen('lose.txt')
            break


if __name__ == '__main__':
    start_fight()
