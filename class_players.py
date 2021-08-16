# this way i can dynamically update the instances of the class
# by changing the lists which serve as input for the instances
# e.g. by updating list2, i can update the number of times that player1
# played black


strings = ['Anna', 'Louise']
list3 = [i.split() for i in strings]
list2 = [1, 1, 0, 0, 1]


class Players:

    def __init__(self, name, black):
        self.name = name
        self.black = black


Player1 = Players(list3[0], sum(list2))
print(Player1.name)
