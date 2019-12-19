from computer import IntcodeComputer

with open("data/input.txt", "r") as f:
    data_raw = f.read()

data = [int(d) for d in data_raw.split(",")]

comp = IntcodeComputer(data)
comp.process()

print("=== PART A ===")
print(comp.outputs[-1])
print()

# ============================================================================

comp = IntcodeComputer(data, 5)
comp.process()
print("=== PART B ===")
print(comp.outputs[-1])
