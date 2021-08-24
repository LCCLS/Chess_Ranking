from pprint import pprint


class PlayerStatus:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.resistance_points = 0
        self.sonnenborn_berger = 0
        self.black = 0
        self.won_against = set()
        self.lost_against = set()
        self.tied_against = set()

    def __repr__(self):
        return (f'name={self.name}, '
                f'points={self.points}, '
                f'resistance={self.resistance_points}, '
                f'sonnenborn={self.sonnenborn_berger}, '
                f'black={self.black}, '
                f'won_against={self.won_against}, '
                f'lost_against={self.lost_against}, '
                f'tied_against={self.tied_against}, '
                f'opponents={self.opponents}')

    def __lt__(self, other):
        if self.points > other.points:
            return self.points > other.points
        elif self.points == other.points:
            return self.resistance_points > other.resistance_points
        elif self.resistance_points == other.resistance_points:
            return self.sonnenborn_berger > other.sonnenborn_berger
        elif self.sonnenborn_berger == other.sonnenborn_berger:
            return self.black > other.black

    @property
    def opponents(self):
        return self.lost_against.union(self.won_against).union(self.tied_against)


def splitting_input(input_: str):
    """splitting the input string on every empty tab"""
    data = [e.strip() for e in input_.split('\n\n')]
    names = data[0].split()
    rounds = []
    data = data[1:]
    data = [e.split('\n') for e in data]

    for round_ in data:
        rounds.append([match.split() for match in round_])
    return names, rounds


def creating_dictionary(player_list):
    """creating a dictionary of player names from a parsed list"""
    ret = {player_name: PlayerStatus(player_name) for player_name in player_list}
    return ret


def parse_data(rounds):
    for round_ in rounds:
        for match in round_:
            white = match[0]
            black = match[1]
            white_points = match[2]
            black_points = match[3]
            player_dict[black].black += 1

            if white_points > black_points:
                player_dict[white].won_against.add(black)
                player_dict[black].lost_against.add(white)
            elif white_points < black_points:
                player_dict[black].won_against.add(white)
                player_dict[white].lost_against.add(black)
            elif white_points == black_points:
                player_dict[white].tied_against.add(black)
                player_dict[black].tied_against.add(white)
            else:
                raise ValueError("Should not happen :O")


def points():
    for player in players:
        points = len(player_dict[player].won_against) + 0.5 * len(player_dict[player].tied_against)
        player_dict[player].points = points


def resistance_points():
    for player in players:
        for opponent in player_dict[player].opponents:
            player_dict[player].resistance_points += player_dict[opponent].points

        # player_dict[player]['resistance_points'] = sum(
        #     [player_dict[opponent]['points'] for opponent in player_dict[player]['opponents']]
        # )


def sonnenborn_points():
    for player in players:
        for opponents in player_dict[player].won_against:
            player_dict[player].sonnenborn_berger += 1 * player_dict[opponents].points
        for opponents in player_dict[player].tied_against:
            player_dict[player].sonnenborn_berger += 0.5 * player_dict[opponents].points


if __name__ == '__main__':
    with open('input_text.txt') as f:
        input_string = f.read()

    players, rounds = splitting_input(input_string)
    player_dict = creating_dictionary(players)

parse_data(rounds)
points()
resistance_points()
sonnenborn_points()
pprint(sorted(player_dict.values()))