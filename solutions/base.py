import abc


class Day(abc.ABC):
    day: int

    @abc.abstractmethod
    def part_1(self, input_file) -> None:
        pass

    @abc.abstractmethod
    def part_2(self, input_file) -> None:
        pass
