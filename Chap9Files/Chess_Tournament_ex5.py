#
# Chess tournament ((python Inheritance example 4 ))
# Chess player will have points which increases for each win(random win)
# Chess Player will also have a rating. Used as a tie breaker if multiple players have same score.
# Each Player will play with each other player.
# Display the winner.
import random


class Player:
    def __init__(self, player_id, rating):
        self._id = player_id
        self._rating = rating
        self._points = 0

    def player_won(self):
        self._points += 1

    def get_rating(self):
        return self._rating

    def get_points(self):
        return self._points

    def get_id(self):
        return self._id

    def __str__(self):
        return f'id: {self._id} points: {self._points} ratings: {self._rating}'


class ChessTournament:
    def __init__(self):
        self._players = []

    def add_player(self, player):
        self._players.append(player)

    def start_tournament(self):
        for index1, player1 in enumerate(self._players):
            for index2 in range(index1 + 1, len(self._players)):
                player2 = self._players[index2]
                random_win = random.randint(0, 1)
                if random_win == 0:
                    player1.player_won()
                else:
                    player2.player_won()

    def get_leader_board(self):
        sorted_players = sorted(self._players, key=lambda player: (-player.get_points(), -player.get_rating()))
        return sorted_players


p1 = Player(1, 1200)
p2 = Player(2, 1400)
p3 = Player(3, 1800)
p4 = Player(4, 2200)

tournament = ChessTournament()
tournament.add_player(p1)
tournament.add_player(p2)
tournament.add_player(p3)
tournament.add_player(p4)

tournament.start_tournament()

leaderboards = tournament.get_leader_board()
for player in leaderboards:
    print(player)
