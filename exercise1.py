def count_calories():
    with open("input1.txt") as file:
        lines = [line.rstrip() for line in file]
    calories = []
    partial_cals = 0
    for line in lines:
        if line.isnumeric():
            partial_cals = partial_cals + int(line)
        else:
            calories.append(partial_cals)
            partial_cals = 0
    calories.append(partial_cals)
    return calories


def part1():
    return max(calories)


def part2():
    calories.sort(reverse=True)
    return calories[0] + calories[1] + calories[2]


if __name__ == '__main__':
    calories = count_calories()
    print(part1())
    print(part2())
