import numpy as np
from scipy.sparse import lil_matrix

#  raw_a = "R8,U5,L5,D3"
#  raw_b = "U7,R6,D4,L4"

#  raw_a = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
#  raw_b = "U62,R66,U55,R34,D71,R55,D58,R83"

with open("data/input.txt") as f:
    raw_a, raw_b = f.readlines()

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def chrow(self, value):
        self.row += value

    def chcol(self, value):
        self.col += value

    def __repr__(self):
        return f"({self.row}, {self.col})"

    def to_array(self):
        return np.array([self.row, self.col])

class Boundaries:
    def __init__(self, data1, data2):
        data1 = data1.split(",")
        data2 = data2.split(",")
        self.L = max(self.max_of(data1, "L"), self.max_of(data2, "L"))
        self.R = max(self.max_of(data1, "R"), self.max_of(data2, "R"))
        self.U = max(self.max_of(data1, "U"), self.max_of(data2, "U"))
        self.D = max(self.max_of(data1, "D"), self.max_of(data2, "D"))

    def max_of(self, data, sym):
        return sum(int(d[1:]) for d in data if d[0] == sym)

class Grid:
    def __init__(self, raw_data, boundary):
        self.data = raw_data.split(",")
        self.center = Node(boundary.U, boundary.L)
        self.pointer = Node(boundary.U, boundary.L)
        self.grid = lil_matrix((boundary.U + boundary.D + 1, boundary.L + boundary.R + 1), dtype = np.int8)
        self.cross_steps = {}

    def process_data(self):
        for datum in self.data:
            self.add_wire(datum)
        self.one_max()

    def process_data_steps(self, crosses):
        steps = 0
        for datum in self.data:
            steps += int(datum[1:])
            self.add_wire(datum)
            for cross in crosses:
                if self.grid[cross[0], cross[1]] >= 1:
                    self.cross_steps[cross_str(cross)] = min(
                        steps - l1(self.pointer.to_array(), cross),
                        self.cross_steps.get(cross_str(cross), np.inf)
                    )
        self.one_max()

    def add_wire(self, datum):
        direction = datum[0]
        value = int(datum[1:])

        if direction == "R":
            self.grid[
                self.pointer.row,
                (self.pointer.col + 1):(self.pointer.col + value + 1)
            ] += np.ones(value)
            self.pointer.chcol(value)
        elif direction == "L":
            self.grid[
                self.pointer.row,
                (self.pointer.col - value):(self.pointer.col)
            ] += np.ones(value)
            self.pointer.chcol(-value)
        elif direction == "D":
            self.grid[
                (self.pointer.row + 1):(self.pointer.row + value + 1),
                self.pointer.col
            ] += np.ones((value, 1))
            self.pointer.chrow(value)
        elif direction == "U":
            self.grid[
                (self.pointer.row - value):(self.pointer.row),
                self.pointer.col
            ] += np.ones((value, 1))
            self.pointer.chrow(-value)

    def one_max(self):
        self.grid[self.grid > 1] = 1

bound = Boundaries(raw_a, raw_b)
g1 = Grid(raw_a, bound)
g2 = Grid(raw_b, bound)
g1.process_data()
g2.process_data()

g = g1.grid + g2.grid

l1 = lambda u, v: np.sum(np.abs(u - v))

crosses = np.argwhere(g == 2)
center = g1.center.to_array()
distances = [l1(center, cross) for cross in crosses]

print("=== PART A ===")
print(np.min(distances))

#==============================================================================

cross_str = lambda c: f"{c[0]},{c[1]}"

g1 = Grid(raw_a, bound)
g2 = Grid(raw_b, bound)
g1.process_data_steps(crosses)
g2.process_data_steps(crosses)

steps = [g1.cross_steps[k] + g2.cross_steps[k] for k in g1.cross_steps.keys()]

print("=== PART B ===")
print(min(steps))



