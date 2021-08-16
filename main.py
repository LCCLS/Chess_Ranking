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
    a_str = some_string.split('\n\n')
    for new_string in a_str:
        new_string = a_str[n].split()
        list.append(new_string)
        n += 1
    return list


print(splitting_input(string))
