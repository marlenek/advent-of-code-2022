from .base import Day


class Day6(Day):

    def day(self):
        return 6

    def part_1(self, input_file):
        return self._tuning_trouble(input_file, 4)

    def part_2(self, input_file):
        return self._tuning_trouble(input_file, 14)

    @classmethod
    def _tuning_trouble(self, input_file, n):
        with open(input_file) as file:
            line = file.readline()
        found = False
        i = 0
        while not found:
            found = True
            temp_array = line[i:i + n]
            for j in range(0, n):
                if temp_array.count(temp_array[j]) > 1:
                    found = False
            i += 1
        return i + n - 1
