def player_starting_bonus(starting_bonus, capacity=200, damage=10, armor=25, cash=1000, enemies_killed=0, level_2=0):
    """Define player stats list and add starting bonus values to the list
    Args:
        starting_bonus: string with bonus which user choosed
        capacity: capacity of the user backpack
        damage: user damage
        armor: user armor
        cash: user cash
        enemies_killed: enemies which user has killed
        level_2: variable to access second level
    Returns:
        player_stats: list which contains every user stats
    """
    player_stats = [capacity, damage, armor, cash, enemies_killed, level_2]

    if starting_bonus[1] == 'gun':
        player_stats[1] += 5

    elif starting_bonus[1] == 'backpack':
        player_stats[0] += 100

    elif starting_bonus[1] == 'shirt':
        player_stats[2] += 10

    return player_stats


def display_stats(player_stats):
    """Display user stats in a pretty table
    Args:
        player_stats: list which contains every user stats
    Returns:
        none
    """
    stats_name = ['Capacity:', 'Damage:', 'Armor:', 'Cash:']
    table_lenght = 10
    print(' _-', ' Pablo Escobar ', '-_')

    for name, line in zip(stats_name, player_stats):
        if name == 'enemies_killed':
            continue

        formated_line = '{:<10} {:<6}'.format(name, line)
        if name == 'Cash:':
            formated_line = '{:<10} {:<7}'.format(name, str(line)+' $')
            print('| ', formated_line, '|')
            continue
        print('| ', formated_line, ' |')

    print('|', ' _' * (table_lenght-1), ' |')
