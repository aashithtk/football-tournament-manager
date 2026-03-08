import random

def create_groups(teams, group_size):

    teams_copy = teams[:]
    random.shuffle(teams_copy)

    groups = []

    for i in range(0, len(teams_copy), group_size):
        group = teams_copy[i:i + group_size]
        groups.append(group)

    return groups
