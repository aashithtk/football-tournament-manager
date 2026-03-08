import itertools

def generate_fixtures(teams):

    fixtures = []

    for match in itertools.combinations(teams, 2):
        team1, team2 = match
        fixtures.append((team1, team2))

    return fixtures
