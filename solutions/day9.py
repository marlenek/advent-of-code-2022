from solutions.base import Day
import numpy


class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def is_touching(self, other):
        return not (abs(self.x - other.x) > 1 or abs(self.y - other.y) > 1)

    def abs_distance_x(self, other):
        return abs(self.x - other.x)

    def abs_distance_y(self, other):
        return abs(self.y - other.y)

    def get_x_follow_move(self, other):
        distance = self.x - other.x
        return self._get_follow_move(distance)

    def get_y_follow_move(self, other):
        distance = self.y - other.y
        return self._get_follow_move(distance)

    @classmethod
    def _get_follow_move(self, distance):
        if distance == 2:
            return 1
        elif distance == -2:
            return -1
        else:
            return distance

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"{self.x=}. {self.y=}"

    def __hash__(self):
        return hash((self.x, self.y))


class Day9(Day):
    day = 9

    def part_1(self, input_file) -> int:
        head_point = Point(0, 0)
        tail_point = Point(0, 0)
        tail_visits = set()
        tail_visits.add(tail_point)

        with open(input_file) as file:
            for line in file.readlines():
                l = line.strip().split(' ')
                move = l[0]
                steps = int(l[1])
                for step in range(0, steps, 1):
                    head_pos_before_move = Point(head_point.x, head_point.y)
                    if move == 'R':
                        head_point.x += 1
                    elif move == 'L':
                        head_point.x -= 1
                    elif move == 'U':
                        head_point.y += 1
                    elif move == 'D':
                        head_point.y -= 1
                    if not head_point.is_touching(tail_point):
                        tail_point = Point(head_pos_before_move.x, head_pos_before_move.y)
                        tail_visits.add(tail_point)
            return len(tail_visits)

    def debug_print(self, tail_points, head):
        grid_size = 18
        grid = numpy.zeros((grid_size, grid_size))
        i = 1
        grid[head.x][head.y] = -1
        for point in tail_points:
            grid[point.x][point.y] = i
            i += 1
        return grid

    def part_2(self, input_file) -> int:
        head_point = Point(0, 0)
        tail_points = [Point(0, 0)] * 9

        tail_visits = set()
        tail_visits.add(tail_points[8])

        with open(input_file) as file:
            for line in file.readlines():
                l = line.strip().split(' ')
                move = l[0]
                steps = int(l[1])
                for step in range(1, steps + 1, 1):
                    head_pos_before_move = Point(head_point.x, head_point.y)
                    if move == 'R':
                        head_point.x += 1
                    elif move == 'L':
                        head_point.x -= 1
                    elif move == 'U':
                        head_point.y += 1
                    elif move == 'D':
                        head_point.y -= 1

                    relative_head_pos = head_point
                    if not relative_head_pos.is_touching(tail_points[0]):
                        for i in range(0, 9, 1):
                            if not relative_head_pos.is_touching(tail_points[i]):
                                # move diagonally in a direction guided by heading point
                                if relative_head_pos.abs_distance_x(
                                        tail_points[i]) == 2 or relative_head_pos.abs_distance_y(tail_points[i]) == 2:
                                    head_pos_before_move = Point(tail_points[i].x, tail_points[i].y)

                                    tail_points[i] = Point(
                                        tail_points[i].x + relative_head_pos.get_x_follow_move(tail_points[i]),
                                        tail_points[i].y + relative_head_pos.get_y_follow_move(tail_points[i]))
                                    relative_head_pos = tail_points[i]
                                # move to the relative head's previous place
                                else:
                                    current_point = Point(tail_points[i].x, tail_points[i].y)
                                    tail_points[i] = Point(head_pos_before_move.x, head_pos_before_move.y)
                                    head_pos_before_move = current_point
                                    relative_head_pos = tail_points[i]
                            else:
                                relative_head_pos = tail_points[i]
                    tail_visits.add(tail_points[8])
            return len(tail_visits)
