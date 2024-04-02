import random

class Game:
    def __init__(self, teams):
        self.__teams = teams

    def ball_thrown(self, team, points):
        if self.__teams:
            self.__teams[team] += points
        else:
            self.__teams[team] = points

    def get_score(self):
        return tuple(self.__teams.values()) if self.__teams else (0, 0)

    def get_winner(self):
        if self.__teams and (tuple(self.__teams.values())[0] == tuple(self.__teams.values())[1]):
            return "Ничья"
        
        if self.__teams and self.__teams.values():
            return max(self.__teams, key=self.__teams.get)


game = Game({"Team1": 0, "Team2": 0})
for _ in range(random.randint(5, 10)):
    game.ball_thrown(random.choice(["Team1", "Team2"]), random.randint(1, 3))
    print(game.get_score())

print(game.get_winner())