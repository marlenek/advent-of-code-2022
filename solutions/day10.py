from solutions.base import Day
import numpy as np


class Day10(Day):
    day = 10

    @classmethod
    def _check_cycle_number(self, cycle):
        return cycle in [20, 60, 100, 140, 180, 220]

    def part_1(self, input_file) -> int:
        with open(input_file) as file:
            cycle = 0
            x = 1
            values = []
            for line in file.readlines():
                l = line.strip().split(' ')
                if l[0] == 'addx':
                    cycle += 1
                    if self._check_cycle_number(cycle): values.append(cycle * x)
                    cycle += 1
                    if self._check_cycle_number(cycle): values.append(cycle * x)
                    x += int(l[1])
                elif l[0] == 'noop':
                    cycle += 1
                    if self._check_cycle_number(cycle): values.append(cycle * x)
        return sum(values)

    @classmethod
    def _update_i_j(self, i, j):
        if i == 40:
            i = 0
            j += 1
        return i, j

    @classmethod
    def _update_screen(self, i, j, x, screen):
        if i in range(x - 1, x + 2, 1):
            screen[j][i] = '#'

    def part_2(self, input_file):
        screen = np.full((6, 40), ['.'], dtype=str)
        with open(input_file) as file:
            cycle = 0
            x = 1
            i = 0
            j = 0
            for line in file.readlines():
                l = line.strip().split(' ')
                if l[0] == 'addx':
                    run_cycles = 2
                    x_to_add = int(l[1])
                else:
                    run_cycles = 1
                    x_to_add = 0

                for k in range(0, run_cycles, 1):
                    cycle += 1
                    (i, j) = self._update_i_j(i, j)
                    self._update_screen(i, j, x, screen)
                    i += 1
                x += x_to_add

        for line in screen:
            print(''.join(line))
        return 0
