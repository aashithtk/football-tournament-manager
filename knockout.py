def generate_knockout(table):

    teams = [team[0] for team in table]

    bracket = []

    for i in range(0, len(teams), 2):

        if i + 1 < len(teams):
            bracket.append((teams[i], teams[i+1]))

    return bracket
