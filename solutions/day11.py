from solutions.base import Day


class Monkey():
    monkey_number: int
    items: []
    test_number: int
    true_case: int
    false_case: int
    operation_string: str
    inspection_count: int

    def __init__(self, monkey_number, items, operation_str, test_number, true_case, false_case,
                 inspection_count_before_round=0):
        self.monkey_number = monkey_number
        self.items = items
        self.operation_string = operation_str
        self.test_number = test_number
        self.true_case = true_case
        self.false_case = false_case
        self.inspection_count = inspection_count_before_round

    def add_item(self, item):
        self.items.append(item)

    def do_operation(self, item):
        params = self.operation_string.split(' ')
        operator = params[0]
        if params[1] == 'old':
            n = item
        else:
            n = int(params[1])
        if operator == '+':
            return item + n
        elif operator == '*':
            return item * n

    def clear_items(self):
        self.items = []

    def is_divisible(self, item):
        return item % self.test_number == 0

    def monkey_bored(self, item):
        return int(item / 3)

    def __repr__(self):
        return f"{self.monkey_number=}\n{self.items=}\n{self.operation_string=}" \
               f"\n{self.test_number=}\n{self.true_case=}\n{self.false_case=}\n" \
               f"{self.inspection_count=}\n"


class Day11(Day):
    day = 11

    @classmethod
    def _read_input(self, input_file):
        with open(input_file) as file:
            lines = [line.strip() for line in file]
        return lines

    @classmethod
    def _read_monkeys(self, input_file):
        monkeys = []
        input = self._read_input(input_file)
        sub_list = [input[n:n + 7] for n in range(0, len(input), 7)]
        for sub in sub_list:
            monkey_number = int(sub[0].split(' ')[1].removesuffix(':'))
            string_items = sub[1].removeprefix("Starting items: ").split(", ")
            items = [int(numeric_string) for numeric_string in string_items]
            operation_str = sub[2].removeprefix('Operation: new = old ')
            test_number = int(sub[3].removeprefix('Test: divisible by '))
            true_case = int(sub[4].split(' ')[-1])
            false_case = int(sub[5].split(' ')[-1])
            monkey = Monkey(monkey_number, items, operation_str, test_number, true_case, false_case)
            monkeys.append(monkey)
        return monkeys

    def part_1(self, input_file) -> int:
        monkeys = self._read_monkeys(input_file)
        for n in range(1, 21, 1):
            for i in range(0, len(monkeys), 1):
                for item in monkeys[i].items:
                    monkey = monkeys[i]
                    item = monkey.do_operation(item)
                    item = monkey.monkey_bored(item)
                    if monkey.is_divisible(item):
                        monkeys[monkey.true_case].add_item(item)
                    else:
                        monkeys[monkey.false_case].add_item(item)
                    monkey.inspection_count += 1
                monkey.clear_items()
        return self._get_monkey_business(monkeys)

    @classmethod
    def _get_monkey_business(self, monkeys):
        monkey_activeness = []
        for monkey in monkeys:
            monkey_activeness.append(monkey.inspection_count)
        monkey_activeness.sort(reverse=True)
        return monkey_activeness[0] * monkey_activeness[1]

    def part_2(self, input_file) -> int:
        monkeys = self._read_monkeys(input_file)
        common_divider = 1
        for monkey in monkeys:
            common_divider *= monkey.test_number
        for n in range(1, 10001, 1):
            for i in range(0, len(monkeys), 1):
                for item in monkeys[i].items:
                    monkey = monkeys[i]
                    item = monkey.do_operation(item)
                    item = item % common_divider
                    if monkey.is_divisible(item):
                        monkeys[monkey.true_case].add_item(item)
                    else:
                        monkeys[monkey.false_case].add_item(item)
                    monkey.inspection_count += 1
                monkey.clear_items()
        return self._get_monkey_business(monkeys)
