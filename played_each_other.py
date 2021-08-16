# class with updated logic (needs revision)
list1 = [10, 20]
list2 = [20, 30]


def run_update(Players):
    print(first_player.name, first_player.score)


class Players:

    def __init__(self, name, score):
        self.name = name
        self.score = score


first_player = Players('Anna', list1[0])
second_player = Players('John', list1[1])

run_update(first_player)

for scores in range(len(list1)):
    list1[scores] += list2[scores]


first_player = Players('Anna', list1[0])

run_update(first_player)
