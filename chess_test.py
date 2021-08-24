from chess import player_result, determine_output

first_test_input = """Erik
Daniel
Charlotte
Anna
Bob
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

first_test_output = [
    player_result('Erik', 2.5, 4.0, 3.0, 2),
    player_result('Daniel', 2.0, 5.5, 3.25, 1),
    player_result('Charlotte', 2.0, 3.5, 2.25, 1),
    player_result('Anna', 1.0, 5.0, 0.5, 2),
    player_result('Bob', 1.0, 5.0, 0.5, 1),
    player_result('Femke', 0.5, 4.0, 1.0, 2)
]

if determine_output(first_test_input) == first_test_output:
    print('you passed the first test')
else:
    print("you didn't pass the first test")

second_test_input = """Trees
Erik
Udo
Ronald
Truus
Omar
Cornelis
Ria
Otto
Emma
Henk
Ulrich
Cor
Piet
Theo
Thea

Trees Erik 0.5 0.5
Udo Ronald 0.5 0.5
Truus Omar 1 0
Cornelis Ria 0 1
Otto Emma 0.5 0.5
Henk Ulrich 1 0
Cor Piet 1 0
Theo Thea 1 0

Ria Cor 0.5 0.5
Theo Truus 1 0
Ronald Henk 0.5 0.5
Emma Udo 0.5 0.5
Erik Otto 0.5 0.5
Ulrich Trees 1 0
Piet Thea 1 0
Omar Cornelis 0 1

Cor Theo 0 1
Ria Henk 0.5 0.5
Ronald Emma 0.5 0.5
Otto Udo 0.5 0.5
Ulrich Truus 0 1
Erik Cornelis 1 0
Piet Trees 0.5 0.5
Thea Omar 0 1

Henk Theo 1 0
Truus Ria 0.5 0.5
Udo Erik 0 1
Otto Ronald 0.5 0.5
Emma Cor 0.5 0.5
Cornelis Piet 1 0
Omar Ulrich 1 0
Trees Thea 1 0

Henk Erik 0.5 0.5
Theo Ria 1 0
Truus Cor 0 1
Cornelis Ronald 0.5 0.5
Trees Otto 0 1
Omar Emma 0.5 0.5
Udo Piet 0.5 0.5
Thea Ulrich 1 0"""

second_test_output = [
    player_result('Theo', 4.0, 12.5, 9.0, 2),
    player_result('Henk', 3.5, 13.5, 9.25, 2),
    player_result('Erik', 3.5, 13.0, 8.75, 3),
    player_result('Cor', 3.0, 13.5, 7.0, 3),
    player_result('Otto', 3.0, 12.5, 7.25, 2),
    player_result('Ria', 2.5, 15.5, 7.0, 3),
    player_result('Ronald', 2.5, 13.5, 6.75, 3),
    player_result('Emma', 2.5, 13.0, 6.5, 3),
    player_result('Cornelis', 2.5, 13.0, 5.75, 2),
    player_result('Truus', 2.5, 13.0, 4.75, 2),
    player_result('Omar', 2.5, 9.5, 3.25, 2),
    player_result('Udo', 2.0, 13.5, 5.0, 2),
    player_result('Trees', 2.0, 10.5, 3.75, 2),
    player_result('Piet', 2.0, 10.5, 3.0, 3),
    player_result('Ulrich', 1.0, 11.5, 2.0, 3),
    player_result('Thea', 1.0, 11.5, 1.0, 3)
]

if determine_output(second_test_input) == second_test_output:
    print('you passed the second test')
else:
    print("you didn't pass the second test")
    from pprint import pprint
    pprint([e for e in second_test_output][7:10])
    pprint([e for e in determine_output(second_test_input)][7:10])
