from collections import deque
from itertools import permutations

from computer import IntcodeComputer

with open("data/input.txt", "r") as f:
    data_raw = f.read()

data = [int(d) for d in data_raw.split(",")]

def run_program(phase_setting):
    phase_setting = deque(phase_setting)
    output = 0
    while phase_setting:
        input_ = deque([phase_setting.popleft(), output])
        comp = IntcodeComputer(data, input_)
        comp.process()
        output = comp.outputs[-1]
    return output

outputs = []
for phase_setting in permutations(range(5), 5):
    outputs.append(run_program(phase_setting))

print("=== PART A ===")
print(max(outputs))
print()

# =============================================================================

phase_settings = dict(zip("ABCDE", [9, 8, 7, 6, 5]))

output_e = []
comp = IntcodeComputer(
    data,
    input_=deque([0]),
    copy=False
)

while len(comp.outputs) != 1:

    # Amp A
    comp.add_phase(phase_settings["A"])
    comp.add_input(output_e)
    comp.process()
    output_a = comp.outputs
    import pdb; pdb.set_trace()

    # Amp B
    comp.add_phase(phase_settings["B"])
    comp.add_input(output_a)
    comp.process()
    output_b = comp.outputs

    # Amp C
    comp.add_phase(phase_settings["C"])
    comp.add_input(output_b)
    comp.process()
    output_c = comp.outputs

    # Amp D
    comp.add_phase(phase_settings["D"])
    comp.add_input(output_c)
    comp.process()
    output_d = comp.outputs

    # Amp E
    comp.add_phase(phase_settings["E"])
    comp.add_input(output_d)
    comp.process()
    output_e = comp.outputs


print(comp.outputs)
