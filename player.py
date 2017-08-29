def player_stats(capacity, damage, armor, cash):
    pass


def display_stats(capacity, damage, armor, cash):

    stats = [capacity, damage, armor, cash]
    stats_name = ['Capacity:', 'Damage:', 'Armor:', 'Cash:']
    table_lenght = 10
    print(' _', ' Pablo Escobar ', '_')

    for name, line in zip(stats_name, stats):
        formated_line = '{:<10} {:<4}'.format(name, line)
        print('| ', formated_line, ' |')

    print('|', ' _' * (table_lenght-2), ' |')
