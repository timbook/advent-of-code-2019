from bodies import LunarSystem, Moon

#  lines = """<x=-1, y=0, z=2>
#  <x=2, y=-10, z=-7>
#  <x=4, y=-8, z=8>
#  <x=3, y=5, z=-1>""".split('\n')

#  lines = """<x=-8, y=-10, z=0>
#  <x=5, y=5, z=10>
#  <x=2, y=-7, z=3>
#  <x=9, y=-8, z=-3>""".split('\n')

with open("data/input.txt", 'r') as f:
    lines = f.readlines()

moons = LunarSystem()
for moon in lines:
    moons.add_moon(moon)

for _ in range(1000):
    moons.tick()

print(moons)
print(moons.calc_energy())
