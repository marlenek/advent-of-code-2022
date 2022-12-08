from .base import Day


class DirectoryTree(object):
    def __init__(self, name='root', subdirectory=None, value=0):
        self.value = value
        self.name = name
        self.subdirectories = []
        self.parent = None
        if subdirectory is not None:
            for subdir in subdirectory:
                self.add_subdirectory(subdir)

    def add_subdirectory(self, subdir):
        assert isinstance(subdir, DirectoryTree)
        subdir.parent = self
        self.subdirectories.append(subdir)

    def go_to(self, name):
        for subdir in self.subdirectories:
            assert isinstance(subdir, DirectoryTree)
            if subdir.name == name:
                return subdir
        # todo add directory if not found in children

    def update_directory_size(self, value):
        self.value += value
        while self.parent is not None:
            self.parent.value += value
            self = self.parent

    def __repr__(self):
        return f"{self.name}, size: {self.value}: {self.subdirectories}"


class Day7(Day):

    def day(self):
        return 7

    def part_1(self, input_file):
        tree = self._read_input(input_file)
        return self._calculate_sum_100000(tree, 0)

    def part_2(self, input_file):
        tree = self._read_input(input_file)
        needed_space = 30000000
        total_space = 70000000
        unused_space = total_space - tree.value
        space_to_free = needed_space - unused_space
        sizes = self._directory_sizes(tree, [])
        for size in sizes:
            if space_to_free < size < total_space:
                current_size = size
        return current_size

    @classmethod
    def _read_input(self, input_file):
        home = DirectoryTree()
        with open(input_file) as file:
            current_folder: DirectoryTree = home
            for line in file:
                if line.startswith('$ cd /'):
                    current_folder = home
                if line.startswith('$ cd ..'):
                    current_folder = current_folder.parent
                elif line.startswith('$ cd') and not line.startswith('$ cd /'):
                    current_folder = current_folder.go_to(line.removeprefix('$ cd ').strip())
                elif line.startswith('dir'):
                    name = line.split(' ')[1].strip()
                    subdir = DirectoryTree(name)
                    current_folder.add_subdirectory(subdir)
                elif line[0].isnumeric():
                    value = int(line.split(' ')[0])
                    name = line.split(' ')[1].split()
                    file = DirectoryTree(name, None, value)
                    current_folder.add_subdirectory(file)
                    current_folder.update_directory_size(value)
        return home

    @classmethod
    def _calculate_sum_100000(self, t: DirectoryTree, sum):
        if len(t.subdirectories) == 0:
            return 0
        elif len(t.subdirectories) > 0 and t.value < int(100000):
            sum += t.value
        for subdir in t.subdirectories:
            sum += self._calculate_sum_100000(subdir, 0)
        return sum

    @classmethod
    def _directory_sizes(self, t: DirectoryTree, sizes_array):
        if len(t.subdirectories) > 0:
            sizes_array.append(t.value)
        for subdir in t.subdirectories:
            (self._directory_sizes(subdir, sizes_array))
        return sizes_array
