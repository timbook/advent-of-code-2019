import re
import numpy as np

class LunarSystem:
    def __init__(self):
        self.moons = []

    def add_moon(self, line):
        coords = re.findall(
            "<x=(.*?), y=(.*?), z=(.*?)>",
            line.strip()
        )[0]
        coords = np.array(coords).astype(int)
        self.moons.append(Moon(coords))

    def apply_gravity(self):
        # For each moon in set, setup gravity before application
        for moon in self.moons:
            moon.setup_gravity(self.moons)

        # For each moon, apply that setup gravity
        for moon in self.moons:
            moon.apply_gravity()

    def apply_velocity(self):
        for moon in self.moons:
            moon.apply_velocity()

    def tick(self):
        self.apply_gravity()
        self.apply_velocity()

    def calc_energy(self):
        return sum([moon.calc_energy() for moon in self.moons])

    def __repr__(self):
        return '\n'.join([moon.__repr__() for moon in self.moons])

class Moon:
    def __init__(self, coords):
        self.coords = coords
        self.vel = np.zeros(3, dtype=int)

    def setup_gravity(self, other_moons):
        self.temp_gravity = np.zeros(3, dtype=int)
        for other_moon in other_moons:
            self.temp_gravity += np.sign(other_moon.coords - self.coords)

    def apply_gravity(self):
        self.vel += self.temp_gravity

    def apply_velocity(self):
        self.coords += self.vel

    def calc_energy(self):
        pe = np.sum(np.abs(self.coords))
        ke = np.sum(np.abs(self.vel))
        return pe*ke

    def __repr__(self):
        return f"Moon(p={self.coords}, v={self.vel})"
