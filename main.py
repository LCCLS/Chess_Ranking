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

new_list = []
list = []


def splitting_input(some_string):
    """splitting the input string on every empty tab"""
    n = 0
    a_str = some_string.split('\n\n')
    for _ in a_str:
        new_list = a_str[n].split()
        list.append(new_list)
        n += 1
    return list


splitting_input(string)



def creating_dictionary(some_list):
    """creating a dictionary of player names from a parsed list"""
    a_dict = dict.fromkeys(some_list, {'name', 'points', 'resistance_points', 'Sonnenborn_berger', 'black'})
    return a_dict

# connecting the dictionary to a class
#class Players:
    #def __init__(self, a_dict):
        #for key, value in a_dict.items():
            #setattr(self, key, value)


o = player_result('Anna', 1.0, 5.0, 0.50, 2)


def eval_input(list):
    creating_dictionary(list[0])




eval_input(list)
