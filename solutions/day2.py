from solutions.base import Day


class Day2(Day):

    def day(self):
        return 2

    def part_1(self, input_file):
        input = self._read_input(input_file)
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

    def part_2(self, input_file):
        input = self._read_input(input_file)
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
                player2 = self._get_keys_from_value(winning_pairs, player1)[0]
                points += 6
            points += points_mapping.get(player2)
        return points

    @classmethod
    def _get_keys_from_value(self, d, val):
        return [k for k, v in d.items() if v == val]

    @classmethod
    def _read_input(self, input_file):
        with open(input_file) as file:
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
