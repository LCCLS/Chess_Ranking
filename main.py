class player_result:
    def __init__(self, name: str, points: float, resistance_points: float, sonnenborn_berger: float, black: int):
        self.name = name
        self.points = points
        self.resistance_points = resistance_points
        self.sonnenborn_berger = sonnenborn_berger
        self.black = black

    def __str__(self):
        return 'player_result(name=\'' + self.name + '\', points=' + str(self.points) + ', resistance_points=' + \
               str(self.resistance_points) + ', sonnenborn_berger=' + str(self.sonnenborn_berger) + \
               ', black=' + str(self.black) + ')'

    def __eq__(self, other):
        return self.name == other.name and self.points == other.points and \
               self.resistance_points == other.resistance_points and \
               self.sonnenborn_berger == other.sonnenborn_berger and self.black == other.black


string = """Anna
    Bob
    Charlotte
    Daniel
    Erik
    Femke

    Anna Femke 1 0
    Bob Erik 0 1
    Charlotte Daniel 0.5 0.5

    Erik Anna 1 0
    Femke Charlotte 0.5 0.5
    Daniel Bob 1 0

    Daniel Erik 0.5 0.5
    Charlotte Anna 1 0
    Bob Femke 1 0"""


def splitting_input(some_string):
    """splitting the input string on every empty tab"""
    n = 0
    list = []
    new_list = []
    a_str = some_string.split('\n\n')
    for _ in a_str:
        new_list = a_str[n].split('\n')
        list.append(new_list)
        n += 1

    names = [score.split() for score in list[0]]
    first_round = [score.split() for score in list[1]]
    second_round = [score.split() for score in list[2]]
    final_round = [score.split() for score in list[3]]
    player_inputs = [names, first_round, second_round, final_round]

    return player_inputs


name = splitting_input(string)
round0 = name[0]
round1 = name[1]
round2 = name[2]
round3 = name[3]
played_rounds = round1, round2, round3
new_player_input = name[0][0] + name[0][1] + name[0][2] + name[0][3] + name[0][4] + name[0][5]
n = 0


def creating_dictionary(some_list):
    """creating a dictionary of player names from a parsed list"""
    values = {'points': 0, 'resistance_points': 0, 'sonnenborn_berger': 0, 'black': 0}
    dictionary = {ver: {col: 0 for col in values} for ver in some_list}
    return dictionary


player_dict = creating_dictionary(new_player_input)


def main_points(input):
    list0 = []
    for rounds in input:
        Player1 = rounds[0]
        Player2 = rounds[1]
        player_dict[Player1]['points'] = player_dict[Player1]['points'] + float(rounds[2])
        player_dict[Player2]['points'] = player_dict[Player2]['points'] + float(rounds[3])

    return player_dict


def resistance_points(input):
    name_list = []
    list0 = []
    for name in new_player_input:
        print(name)
        for rounds in input:
            for round in rounds:

                Player1 = round[0]
                Player2 = round[1]
                if Player1 == name:
                    list0.append(Player2)
                elif Player2 == name:
                    list0.append(Player1)






    return list0


print(resistance_points(played_rounds))
