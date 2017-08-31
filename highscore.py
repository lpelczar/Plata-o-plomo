import boss
import random
import csv
from operator import itemgetter


def display_highscore():
    with open('highscore.txt') as f:
        read_data = f.read()
    if not read_data:
        print('Empty!')
    else:
        print(read_data)


def add_score_to_file(score):
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
    with open('highscore.txt', 'w') as f:
        for i in range(len(highscore)):
            f.write(" ".join([str(highscore[i][0]), str(highscore[i][1])]))
            f.write('\n')


if __name__ == '__main__':
    add_score_to_file()
