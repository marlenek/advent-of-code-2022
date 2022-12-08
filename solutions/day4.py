from solutions.base import Day


class Day4(Day):

    def day(self):
        return 4

    def part_1(self, input_file):
        input = self._read_input(input_file)
        sum = 0
        for line in input:
            elf1, elf2 = self._readElfes(line)
            if (elf1.a <= elf2.a and elf1.b >= elf2.b) or (elf2.a <= elf1.a and elf2.b >= elf1.b):
                sum += 1
        return sum

    def part_2(self, input_file):
        input = self._read_input(input_file)
        sum = 0
        for line in input:
            elf1, elf2 = self._readElfes(line)
            if (elf2.a <= elf1.b <= elf2.b) or (elf1.a <= elf2.b <= elf1.b):
                sum += 1
        return sum

    @classmethod
    def _read_input(self, input_file):
        with open(input_file) as file:
            lines = [line.strip() for line in file]
        return lines

    @classmethod
    def _readElfes(self, line):
        first_range = line.split(',')[0].split('-')
        elf1 = Elf(int(first_range[0]), int(first_range[1]))
        second_range = line.split(',')[1].split('-')
        elf2 = Elf(int(second_range[0]), int(second_range[1]))
        return elf1, elf2


class Elf:
    def __init__(self, rangeA, rangeB):
        self.a = rangeA
        self.b = rangeB
