import pandas as pd


def read_input():
    with open("input2.txt") as file:
        lines = [line.strip().split(' ') for line in file]
    return lines


winning_pairs = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

mapping_of_letters = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

points_mapping = {
    'A': 1,
    'B': 2,
    'C': 3
}


def part1():
    points = 0
    for line in input:
        player1 = line[0]
        player2 = mapping_of_letters.get(line[1])
        if player1 == player2:
            points += 3
        elif winning_pairs.get(player1) != player2:
            points += 6
        points += points_mapping.get(player2)
    return points


def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]


def part2():
    points = 0
    for line in input:
        player1 = line[0]
        player2 = line[1]
        if player2 == 'X':
            player2 = winning_pairs.get(player1)
        elif player2 == 'Y':
            player2 = player1
            points += 3
        else:
            player2 = get_keys_from_value(winning_pairs, player1)[0]
            points += 6
        points += points_mapping.get(player2)
    return points


if __name__ == '__main__':
    input = read_input()
    print(part1())
    print(part2())
