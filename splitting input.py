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
        a_str = some_string.split('\n\n')
        print(a_str[0])




splitting_input(string)
