import boss
import random
import csv
from operator import itemgetter


def display_highscore():
    """Open highscore file and print it to the user
    Args:
        none
    Returns:
        none
    """
    with open('highscore.txt') as f:
        read_data = f.read()
    if not read_data:
        print('Empty!')
    else:
        print(read_data)


def add_score_to_file(score):
    """Open file and add every score to highscore list, then ask user for name and append
    user highscore at the end of the highscore list, then sort highscore
    Args:
        score: user score
    Returns:
        none
    """
    highscore = []
    with open('highscore.txt') as f:
        temp = f.read().splitlines()
    for i in temp:
        highscore.append(i.split(' '))

    name = input('Enter your name to add your score: ')
    value = [name, score]
    highscore.append(value)

    for i in range(len(highscore)):
        highscore[i][1] = int(highscore[i][1])
    highscore = sorted(highscore, key=itemgetter(1))
    save_highscore_to_file(highscore)


def save_highscore_to_file(highscore):
    """Save highscore list to the file
    Args:
        highscore: list with sorted highscores
    Returns:
        none
    """
    with open('highscore.txt', 'w') as f:
        for i in range(len(highscore)):
            f.write(" ".join([str(highscore[i][0]), str(highscore[i][1])]))
            f.write('\n')


if __name__ == '__main__':
    add_score_to_file()
