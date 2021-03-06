import numpy as np

data_raw = open("data/input.txt", 'r').readlines()[0].strip()

data = np.array(list(data_raw)).reshape(-1, 6, 25).astype(int)

n_zeros = np.array([
    np.sum(subarr == 0) for subarr in data
])

min_layer = np.argmin(n_zeros)

subarr = data[min_layer, : , :]

n_ones = np.sum(subarr == 1)
n_twos = np.sum(subarr == 2)

print("=== PART A ===")
print(n_ones * n_twos)
print()

#==============================================================================

# 0 = Black
# 1 = White
# 2 = Transparent

def get_num(arr):
    for val in arr:
        if val == 2:
            continue
        else:
            return val

res = np.apply_along_axis(get_num, 0, data)

import matplotlib.pyplot as plt
plt.imshow(res, cmap="Greys_r")
plt.show()





