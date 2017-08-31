def read_map_from_file(filename):
    """Read map from file and convert it to board list
    Args:
        filename: name of the file with the map
    Returns:
        board: list of lists representing our map
    """
    with open(filename) as f:
        read_data = f.read().splitlines()

    board = [list(x) for x in read_data]

    return board


def next_level(player_stats):
    """Set new level variable to True
    Args:
        player_stats: list of player stats
    Returns:
        player_stats: list of player stats
    """
    player_stats[5] = True

    return player_stats
