import numpy as np
from items import Node, Boundaries, Grid

with open("data/input.txt") as f:
    raw_a, raw_b = f.readlines()

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

g1 = Grid(raw_a, bound)
g2 = Grid(raw_b, bound)
g1.process_data_steps(crosses)
g2.process_data_steps(crosses)

steps = [g1.cross_steps[k] + g2.cross_steps[k] for k in g1.cross_steps.keys()]

print("=== PART B ===")
print(min(steps))



