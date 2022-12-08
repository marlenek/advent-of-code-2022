from solutions.base import Day


class Day3(Day):

    def day(self):
        return 3

    def part_1(self, input_file):
        input = self._read_input(input_file)
        sum = 0
        for line in input:
            (a, b) = line[:len(line) // 2], line[len(line) // 2:]
            for letter in a:
                if letter in b:
                    sum += self._get_item_value(letter)
                    break
        return sum

    def part_2(self, input_file):
        input = self._read_input(input_file)
        sum = 0
        sub_list = [input[n:n + 3] for n in range(0, len(input), 3)]
        for sub in sub_list:
            for letter in sub[0]:
                if letter in sub[1] and letter in sub[2]:
                    sum += self._get_item_value(letter)
                    break
        return sum

    @classmethod
    def _read_input(self, input_file):
        with open(input_file) as file:
            lines = [line.strip() for line in file]
        return lines

    @classmethod
    def _get_item_value(self, letter):
        return ord(letter) - 96 if letter.islower() else ord(letter) - 38
