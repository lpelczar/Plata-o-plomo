import introduction


def player_starting_stats(capacity=200, damage=10, armor=15, cash=1000):
    player_stats = [capacity, damage, armor, cash]
    starting_bonus = introduction.menu_select()
    print(starting_bonus)
    print(player_stats)

    if starting_bonus[1] == 'gun':
        player_stats[1] += 5

    elif starting_bonus[1] == 'backpack':
        player_stats[0] += 100

    elif starting_bonus[1] == 'shirt':
        player_stats[2] += 10

    return player_stats


def display_stats(player_stats):  # capacity, damage, armor, cash):

    # player_stats = [capacity, damage, armor, cash]
    stats_name = ['Capacity:', 'Damage:', 'Armor:', 'Cash:']
    table_lenght = 10
    print(' _', ' Pablo Escobar ', '_')

    for name, line in zip(stats_name, player_stats):
        formated_line = '{:<10} {:<4}'.format(name, line)
        print('| ', formated_line, ' |')

    print('|', ' _' * (table_lenght-2), ' |')
