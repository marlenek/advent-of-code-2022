from .base import Day


class Day1(Day):
    day = 1

    def part_1(self, input_file):
        calories = self._count_calories(input_file)
        return max(calories)

    def part_2(self, input_file):
        calories = self._count_calories(input_file)
        calories.sort(reverse=True)
        return sum(calories[:3])

    @classmethod
    def _count_calories(cls, input_file):
        with open(input_file) as file:
            lines = [line.strip() for line in file]
        calories = []
        partial_cals = 0
        for line in lines:
            if line.isnumeric():
                partial_cals += int(line)
            else:
                calories.append(partial_cals)
                partial_cals = 0
        calories.append(partial_cals)
        return calories
