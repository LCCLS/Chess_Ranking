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

list = []


def splitting_input(some_string):
    """splitting the input string on every empty tab"""
    n = 0
    a_str = some_string.split('\n\n')
    for _ in a_str:
        new_string = a_str[n].split()
        list.append(new_string)
        n += 1
    return list


splitting_input(string)
name = list[0]


def creating_dictionary(some_list):
    a_dict = dict.fromkeys(some_list, 0)
    print(a_dict)


creating_dictionary(name)
