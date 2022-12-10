import numpy

from .base import Day


class Day8(Day):

    day = 8

    def part_1(self, input_file):
        grid, grid_size = self._read_grid(input_file)
        visible_trees = 0
        for i in range(0, grid_size, 1):
            for j in range(0, grid_size, 1):
                if self._check_vertical_and_horizontal(grid, grid_size, i, j):
                    visible_trees += 1
        return visible_trees

    def part_2(self, input_file):
        grid, grid_size = self._read_grid(input_file)
        visible_trees = []
        for i in range(0, grid_size, 1):
            for j in range(0, grid_size, 1):
                visible_trees.append(self._check_scenic_scores(grid, grid_size, i, j))
        return max(visible_trees)

    @classmethod
    def _read_grid(self, input_file):
        with open(input_file) as file:
            line = file.readline()
            grid_size = len(line.strip())
            grid = numpy.zeros((grid_size, grid_size))
        i = 0
        with open(input_file) as file:
            for line in file.readlines():
                j = 0
                for char in line.strip():
                    grid[i][j] = char
                    j += 1
                i += 1
        return grid, grid_size

    @classmethod
    def _check_scenic_scores(self, grid, grid_size, x, y):
        visible_up = 0
        visible_down = 0
        visible_left = 0
        visible_right = 0

        for i in range(y - 1, -1, -1):
            visible_left += 1
            if (grid[x][i]) >= grid[x][y]:
                break

        for i in range(y + 1, grid_size, 1):
            visible_right += 1
            if (grid[x][i]) >= grid[x][y]:
                break

        for i in range(x - 1, -1, -1):
            visible_up += 1
            if (grid[i][y]) >= grid[x][y]:
                break

        for i in range(x + 1, grid_size, 1):
            visible_down += 1
            if (grid[i][y]) >= grid[x][y]:
                break

        return visible_up * visible_down * visible_left * visible_right

    @classmethod
    def _check_vertical_and_horizontal(self, grid, grid_size, x, y):
        visible_up = True
        visible_down = True
        visible_left = True
        visible_right = True

        for i in range(0, y, 1):
            if (grid[x][i]) >= grid[x][y]:
                visible_left = False

        for i in range(y + 1, grid_size, 1):
            if (grid[x][i]) >= grid[x][y]:
                visible_right = False

        for i in range(0, x, 1):
            if (grid[i][y]) >= grid[x][y]:
                visible_up = False

        for i in range(x + 1, grid_size, 1):
            if (grid[i][y]) >= grid[x][y]:
                visible_down = False

        return visible_up or visible_down or visible_left or visible_right
