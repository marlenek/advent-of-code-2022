import click

import solutions


@click.command()
@click.option('--day', default=9, help='Day(s) to run. ex.: 1')
@click.option('--test', default=False, help='add if you want to run test version')
def runner(day, test):
    days = [day]
    for day_class in solutions.__all__:
        day = day_class()
        if day.day in days:
            input_file = f"input/input{day.day}.txt" if not test else f"test_input/input{day.day}_test.txt"
            print(f"day {day.day} part 1: {day.part_1(input_file)}")
            print(f"day {day.day} part 2: {day.part_2(input_file)}")


if __name__ == '__main__':
    runner()
