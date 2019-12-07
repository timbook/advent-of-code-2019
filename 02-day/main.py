from itertools import product
from program import Program

with open("data/input.txt", 'r') as f:
    data = f.readline()

data = [int(d) for d in data.split(",")]

prog = Program(data, 12, 2)
prog.process()

print("=== PART A ===")
print(prog.get_output())

#===============================================================================

print("=== PART B ===")
desired_output = 19690720
for noun, verb in product(range(100), range(100)):
    prog = Program(data, noun, verb)
    prog.process()
    if prog.get_output() == desired_output:
        print("FOUND IT!!!")
        print(f"Noun = {noun}")
        print(f"Verb = {verb}")
        print(f"Soln = {100*noun + verb}")
