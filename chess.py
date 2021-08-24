from typing import Dict, List
from pprint import pprint

# DON'T MODIFY THIS CLASS
class player_result:
    def __init__(self, name: str, points: float, resistance_points: float, sonnenborn_berger: float, black: int):
        self.name = name
        self.points = points
        self.resistance_points = resistance_points
        self.sonnenborn_berger = sonnenborn_berger
        self.black = black

    def __repr__(self):
        return 'player_result(name=\'' + self.name + '\', points=' + str(self.points) + ', resistance_points=' + \
               str(self.resistance_points) + ', sonnenborn_berger=' + str(self.sonnenborn_berger) + \
               ', black=' + str(self.black) + ')'

    def __eq__(self, other):
        return self.name == other.name and self.points == other.points and \
               self.resistance_points == other.resistance_points and \
               self.sonnenborn_berger == other.sonnenborn_berger and self.black == other.black


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

    @property
    def opponents(self):
        return self.lost_against.union(self.won_against).union(self.tied_against)


def splitting_input(input_: str):
    """Split the input string on every double new line"""
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


def parse_data(player_dict, rounds):
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
    return player_dict


def points(player_dict, players):
    for player in players:
        player_points = (
                len(player_dict[player].won_against) +
                0.5 * len(player_dict[player].tied_against)
        )
        player_dict[player].points = player_points
    return player_dict


def resistance_points(player_dict, players):
    for player in players:
        for opponent in player_dict[player].opponents:
            player_dict[player].resistance_points += player_dict[opponent].points
    return player_dict


def sonnenborn_points(
        player_dict: Dict[str, PlayerStatus],
        players: List[str]
) -> Dict[str, PlayerStatus]:
    """Calculate Sonnenborn Points."""
    for player in players:
        for opponents in player_dict[player].won_against:
            player_dict[player].sonnenborn_berger += 1 * player_dict[opponents].points
        for opponents in player_dict[player].tied_against:
            player_dict[player].sonnenborn_berger += 0.5 * player_dict[opponents].points
    return player_dict


def determine_output(input_string: str):
    players, rounds = splitting_input(input_string)
    data = creating_dictionary(players)

    data = parse_data(player_dict=data, rounds=rounds)
    data = points(player_dict=data, players=players)
    data = resistance_points(player_dict=data, players=players)
    data = sonnenborn_points(player_dict=data, players=players)

    # So klappt es verlässlich. Wir übergeben der built-in sorted function einfach die
    # data.values() und sagen über das keyword-argument `key=` wie wir die Elemente in
    # der Liste sortiert haben wollen. `reversed=True` brauchen wir, weil Python
    # standardmäßig aufsteigend sortiert -- wir wollen aber tendenziell das größte (i.e.
    # höchste Punktzahlen) zuerst.
    #
    # Was genau lambda ist kannst du nachlesen (das sprengt etwas den Rahmen) aber im
    # Endeffekt sagen wir "Erstelle folgendes Tuple von jedem Element x:
    # (x.points, x.resistance_points, x.sonnenborn_berger, x.black)
    # Jetzt benutze diese Tuples um die Liste zu sortieren"
    #
    # Das klappt, weil Python Tuples schon genau so sortiert, wie man es intuitiv haben
    # will --> Erst anhand des ersten Elements, wenn die gleich sind anhand des zweiten,
    # usw. Tada, sortiert und Tests passen :)
    sorted_data = sorted(
            data.values(),
            key=lambda x: (x.points, x.resistance_points, x.sonnenborn_berger, x.black),
            reverse=True
    )

    result = []
    for player in sorted_data:
        result.append(
            player_result(
                name=player.name,
                points=player.points,
                resistance_points=player.resistance_points,
                sonnenborn_berger=player.sonnenborn_berger,
                black=player.black,
            )
        )

    return result


if __name__ == '__main__':
    with open('input_text.txt') as f:
        input_string = f.read()

    determine_output(input_string)
