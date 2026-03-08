class Tournament:

    def __init__(self):
        self.teams = {}

    def add_team(self, name):
        if name not in self.teams:
            self.teams[name] = {
                "played": 0,
                "wins": 0,
                "draws": 0,
                "losses": 0,
                "points": 0
            }

    def add_result(self, team1, team2, score1, score2):

        self.teams[team1]["played"] += 1
        self.teams[team2]["played"] += 1

        if score1 > score2:
            self.teams[team1]["wins"] += 1
            self.teams[team1]["points"] += 3
            self.teams[team2]["losses"] += 1

        elif score2 > score1:
            self.teams[team2]["wins"] += 1
            self.teams[team2]["points"] += 3
            self.teams[team1]["losses"] += 1

        else:
            self.teams[team1]["draws"] += 1
            self.teams[team2]["draws"] += 1
            self.teams[team1]["points"] += 1
            self.teams[team2]["points"] += 1

    def get_table(self):

        return sorted(
            self.teams.items(),
            key=lambda x: x[1]["points"],
            reverse=True
        )
