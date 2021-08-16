person_database = {'ID' : ['Anna']}

class Players:
        def __init__(self, name):
                self.name = name

Player = []
for ID in person_database:
        personal_info = person_database[ID]
        Player.append(Players([0]))

Players.name


---------------

import json

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

a_str = string.split('\n\n')
names = a_str[0].split()
Player1 = {name, points, resistance, sonnenborg}
Player2 = {name, points, resistance, sonnenborg}
Player3 = {name, points, resistance, sonnenborg}


class Players:
    def __init__(self, name):
        self.name = name



print(person_database)

-------------------
class Players:
    def __init__(self, name, points, resistance):
        self.name = name
        self.points = points
        self.resistance = resistance


names = ['Bob', 'Anna', 'Femke']
keys = ['points', 'resistance', 'sonnenborg']
points = 3, 4
resistance = 2, 3
Player1 = {}
Player2 = {}
Player3 = {}

for i in ('name', 'points', 'resistance'):
    Players[i] = locals()[i]


print(Player1)


class Players:
    def __init__(self, name, points, resistance):
        self.name = name
        self.points = points
        self.resistance = resistance


