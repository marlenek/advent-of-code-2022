from collections import deque
import re

from solutions.base import Day


class Day5(Day):

    def day(self):
        return 5

    def part_1(self, input_file):
        list_of_stacks, instructions = self._read_input(input_file)
        for line in instructions:
            match = re.findall('\\d+', line.strip())
            for i in range(int(match[0])):
                item = list_of_stacks[int(match[1]) - 1].popleft()
                list_of_stacks[int(match[2]) - 1].appendleft(item)
                i += 1
        result = ''
        for d in list_of_stacks:
            result += d.popleft()
        return result

    def part_2(self, input_file):
        list_of_stacks, instructions = self._read_input(input_file)
        for line in instructions:
            match = re.findall('\\d+', line.strip())
            popped = deque()
            for i in range(int(match[0])):
                item = list_of_stacks[int(match[1]) - 1].popleft()
                popped.appendleft(item)
                i += 1
            for p in popped:
                list_of_stacks[int(match[2]) - 1].appendleft(p)
        result = ''
        for d in list_of_stacks:
            result += d.popleft()
        return result

    @classmethod
    def _read_input(self, input_file):
        list_of_stacks = []
        instructions = []
        image_part = True
        with open(input_file) as file:
            for line in file:
                if line.startswith('\n'):
                    image_part = False
                elif image_part:
                    j = 0
                    for x in [line[i:i + 4] for i in range(0, len(line), 4)]:
                        if len(list_of_stacks) < len(line) / 4:
                            if len(x) >= 3:
                                if x[1].isalpha():
                                    q = deque(x[1])
                                    list_of_stacks.append(q)
                                else:
                                    q = deque()
                                    list_of_stacks.append(q)
                        else:
                            if len(x) >= 3:
                                if x[1].isalpha():
                                    list_of_stacks[j].append(x[1])
                        j += 1

                else:
                    instructions.append(line)
        return list_of_stacks, instructions
