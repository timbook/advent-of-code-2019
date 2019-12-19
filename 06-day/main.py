with open("data/input.txt", "r") as f:
    raw_data = f.readlines()

def parse_line(line):
    l, r = line.split(")")
    return l.strip(), r.strip()

data = [parse_line(line) for line in raw_data]

class Node:
    def __init__(self, name, orbit):
        self.name = name
        self.orbit = orbit

    def explore_up(self):
        return 0 if not self.orbit else 1 + planets[self.orbit].explore_up()

    def find_up(self, other):
        if self.orbit == other:
            return 1
        else:
            return 1 + planets[self.orbit].find_up(other)

    def list_orbits(self):
        return [] if not self.orbit else [self.orbit] + planets[self.orbit].list_orbits()

planets = {"COM": Node("COM", None)}

for left, right in data:
    planets[right] = Node(right, left)

print("=== PART A ===")
orbit_counts = [planet.explore_up() for planet in planets.values()]
print(sum(orbit_counts))
print()

# ============================================================================

you_orbits = planets["YOU"].orbit
san_orbits = planets["SAN"].orbit

you_orbit_list = planets[you_orbits].list_orbits()
san_orbit_list = planets[san_orbits].list_orbits()

common_ancestors = []
for orbit in you_orbit_list:
    if orbit in san_orbit_list:
        common_ancestors.append(orbit)

nearest_ancestor = common_ancestors[0]

you_up = planets[you_orbits].find_up(nearest_ancestor)
san_up = planets[san_orbits].find_up(nearest_ancestor)

print("=== PART B ===")
print(you_up + san_up)
