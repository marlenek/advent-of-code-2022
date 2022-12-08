import abc

class Day(abc.ABC):

    @abc.abstractmethod
    def day(self) -> int:
        pass

    @abc.abstractmethod
    def part_1(self, input_file) -> None:
        pass

    @abc.abstractmethod
    def part_2(self, input_file) -> None:
        pass