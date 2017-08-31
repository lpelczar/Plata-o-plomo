def read_map_from_file(filename):

    with open(filename) as f:
        read_data = f.read().splitlines()

    board = [list(x) for x in read_data]

    return board


def next_level(player_stats):
    player_stats[5] = True

    return player_stats
