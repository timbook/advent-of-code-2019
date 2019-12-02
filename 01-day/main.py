def calc_gas(n):
    gas = int(n / 3) - 2
    return max(gas, 0)

with open("data/input.txt", 'r') as f:
    data = f.readlines()

data = [int(d.strip()) for d in data]

gas_needed = sum([calc_gas(d) for d in data])

print("=== PART A ===")
print(gas_needed)

#===============================================================================

def compound_gas(data):
    gas_needed = [calc_gas(d) for d in data]
    return sum(gas_needed), gas_needed

total_gas = 0
data_current = data.copy()

while True:
    gas_needed, data_current = compound_gas(data_current)
    total_gas += gas_needed
    if gas_needed == 0:
        break

print("=== PART B ===")
print(total_gas)
