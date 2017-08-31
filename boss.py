import os
import random
import time
import sys
import highscore


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_boss():
    """Read from file and display ASCII ART with boss
    Args:
        none
    Returns:
        none
    """
    with open('boss.txt') as f:
        read_data = f.read()
    print('\033[91m' + read_data + '\033[0m')


def play_cold_warm():
    """Play hot warm cold with the boss, if user win display win screen and highscore,
        if user lose display lose screen
    Args:
        none
    Returns:
        none
    """
    user_guesses = 10
    correct_answer = generate_unique_number()
    print(correct_answer)
    while user_guesses > 0:
        user_input = get_user_input()
        feedback = compare_user_answer(user_input, correct_answer)
        print('Hint: ', end='')
        for i in feedback:
            print(i, end=' ')
        print('   Guesses left:', user_guesses - 1)
        if feedback == ['hot', 'hot', 'hot']:
            display_screen('win.txt')
            score = user_guesses * 111
            highscore.add_score_to_file(score)
            highscore.display_highscore()
            break
        user_guesses -= 1
        if user_guesses == 0:
            display_screen('lose.txt')
            sys.exit()


def get_user_input():
    """Ask user for a unique number of 3 digit length
    Args:
        none
    Returns:
        list of numbers casted to strings
    """
    while True:
        user_input = input('Enter 3-digit unique number: ')
        if user_input.isdigit() and len(user_input) == 3 and len(set(user_input)) == len(user_input):
            break
        else:
            print('Number should have 3 unique digits!')
    return list(user_input)


def display_screen(filename):
    """Read txt file and display the content to cleared console
    Args:
        filename: name of the file
    Returns:
        none
    """
    clear_console()
    with open(filename) as f:
        read_data = f.read()
    print(read_data)


def compare_user_answer(guess, correct_answer):
    """Compare user answer with correct answer and append hints to a list
    Args:
        guess: user guess
        correct_answer: answer which is correct
    Returns:
        hints: list of hints
    """
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
    """Generate number with 3 unique digits
    Args:
        none
    Returns:
        list of 3 unique numbers
    """
    unique_number_list = [str(x) for x in range(10)]
    random.shuffle(unique_number_list)
    return unique_number_list[:3]


def start_fight():
    """Ask user if he want to start fight with boss, if yes start fight, if no display lose screen.
    Args:
        none
    Returns:
        none
    """
    clear_console()
    display_boss()
    while True:
        answer = input('Pershing: Pablo mi amigo! We were always good friends. Now you want to fight with me? ').lower()
        if answer == 'yes':
            print('Pershing: As you wish, lets play cold/warm, I thought of 3 unique digit number, you have 10 guesses to guess it!')
            play_cold_warm()
            break
        if answer == 'no':
            print('Pershing: I thought so! Go home Pablo!')
            time.sleep(2)
            display_screen('lose.txt')
            break


if __name__ == '__main__':
    start_fight()
